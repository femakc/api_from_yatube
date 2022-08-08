from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели Post."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели Group."""

    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели Comment."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def create(self, validated_data):
        print(validated_data)
        user = validated_data.get('user')
        following = validated_data.get('following')
        if user == following:
            raise serializers.ValidationError('подписка сам на себя !!!')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('подписка существует !!!')
        return Follow.objects.create(**validated_data)
