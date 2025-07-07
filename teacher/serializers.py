from rest_framework import serializers
from .models import Chapter, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_doc', 'topic_desc', 'topic_time']

class ChapterSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ['name', 'topics']

    def create(self, validated_data):
        topics_data = validated_data.pop('topics')
        chapter = Chapter.objects.create(name=validated_data['name'])
        for topic_data in topics_data:
            topic, created = Topic.objects.get_or_create(**topic_data)
            chapter.topics.add(topic)
        return chapter