from django.db import models
from django.contrib.auth.models import User



#class PublishedManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(status='published')


class Question(models.Model):

    objects = models.Manager()  # Менеджер по умолчанию.

    #published = PublishedManager()  # Наш новый менеджер.
    #STATUS_CHOICES = (
   #     ('draft', 'Draft'),
   #     ('published', 'Published'),
   # )
    title = models.CharField(max_length=250)
   # tags = TaggableManager()
   # slug = models.SlugField(max_length=250, unique_for_date='publish')
   # author = models.ForeignKey(User, on_delete=models.CASCADE,
   #                            related_name='blog_posts')
    body = models.TextField()
    #publish = models.DateTimeField(default=timezone.now)
   # created = models.DateTimeField(auto_now_add=True)
   # updated = models.DateTimeField(auto_now=True)
   # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

   # def get_absolute_url(self):
   #     return reverse('blog:post_detail', args=[self.publish.year,
   #                                              self.publish.month, self.publish.day, self.slug])

   # class Meta:
   #     ordering = ('-publish',)

    def __str__(self):
        return self.body


class Answers(models.Model):
    question = models.ForeignKey(Question,
                             on_delete=models.CASCADE,
                             related_name='answers')
    name = models.CharField(max_length=80)
    body = models.TextField()
    active = models.BooleanField(default=True)
    correct_answer = models.BooleanField(default=False)


    def __str__(self):
        return self.body

class users_Answer(models.Model):
    #user = models.ForeignKey(User, on_delete=models.PROTECT)
    given_answer = models.TextField ()
    body = models.TextField()
    active = models.BooleanField(default=True)
    correct_answer = models.BooleanField(default=False)


'''
    @property
    def is_correct(self):
        if self.given_answer and self.correct_answer and self.given_answer > self.correct_answer:
            return True
        return False

    def __str__(self):
        return self.body
# Create your models here.
'''