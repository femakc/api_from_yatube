from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Объявляем Класс/Модель Group."""
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок сообщест'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Адрес для страницы с постами',
        help_text='Адрес сообщест'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание сообщест'
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Post(models.Model):
    """Объявляем Класс/Модель Post."""
    text = models.TextField(
        verbose_name="Пост",
        help_text='Текст нового поста'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='post',
        verbose_name="Автор поста",
        help_text='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name="Группа",
        help_text='Группа, к которой будет относиться пост'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    """Объявляем Класс/Модель Comment."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Автор поста",
        help_text='Автор'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Пост",
        help_text='Пост к которому относится коментарий'
    )
    text = models.TextField(
        verbose_name="Комментарий",
        help_text='Текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return "Комментарий"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Follow(models.Model):
    """Объявляем Класс/Модель Follow."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name="Подписчик",
        help_text='тот кто подписывается '
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name="Блогер",
        help_text='тот на кого подписываются'
    )

    def __str__(self):
        return f'{self.user.username} подписан на {self.following.username}'

    class Meta:
        verbose_name = 'follow'
        verbose_name_plural = 'follows'
        unique_together = ('user', 'following',)
