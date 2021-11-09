from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Content, Cv, Post, Section, PostSection, PostParagraph


class ContentSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.content

    class Meta:
        model = Content
        fields =  ('content', )

class SectionSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)
    class Meta:
        model = Section
        fields = ('name', 'content', )

class CvSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True)
    class Meta:
        model = Cv
        fields = ('name', 'section') 

    def create(self, validated_data):
        subCv = Cv.objects.create(
            name = validated_data.get('name', None)
        )

        for section in validated_data.get('section', []):
            section_obj = Section.objects.create(
                name = section.get('name', None)
            )
            for content in section.get('content', []):
                content_content = content.get('content', None)
                content_obj = Content.objects.create(
                    content = content_content
                )
                section_obj.content.add(content_obj)
            section_obj.cv = subCv  
            section_obj.save()
            
        return subCv
        
# //////////////////////////////////////////////////////////////////////////////////////

class PostParagraphSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.paragraph
    class Meta:
        model = PostParagraph
        fields = ('paragraph',)

class PostSectionSerializer(serializers.ModelSerializer):
    post_paragraph = PostParagraphSerializer(many=True)
    class Meta:
        model = PostSection
        fields = ('name', 'post_paragraph', )

class PostBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'brief_content', )

class PostSerializer(serializers.ModelSerializer):
    post_section = PostSectionSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'brief_content', 'post_section', )
        extra_kwargs = {
            'brief_content': {'write_only': True},
        }
    
    def create(self, validated_data):

        post = Post.objects.create( 
            title = validated_data['title'],
            brief_content = validated_data.get('brief_content', None)
        )

        for post_section in validated_data.get('post_section', None):
            post_section_obj = PostSection.objects.create( name = post_section.get('name', None))

            for post_paragraph in post_section.get('post_paragraph', None):
                post_paragraph_obj = PostParagraph.objects.create( paragraph =  post_paragraph.get('paragraph', None))

                post_paragraph_obj.section = post_section_obj
                post_paragraph_obj.save()
            
            post_section_obj.post = post
            post_section_obj.save()

        return post


