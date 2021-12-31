from rest_framework import serializers
from movieapp.models import Tweet


def validate_name(value):
    if(len(value) < 2):
        raise serializers.ValidationError('Too Short')


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[validate_name])
    tweet = serializers.CharField()
    date = serializers.DateField()

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tweet = validated_data.get('tweet', instance.tweet)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    def validate(self, data):

        if data['name'] == data['tweet']:
            raise serializers.ValidationError(
                "Name should not be equal to tweet")
        return data
