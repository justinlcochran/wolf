import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


class Role(models.Model):
	game_score = models.IntegerField()
	role_title = models.CharField(max_length=200)
	role_description = models.CharField(max_length=400)
	role_type = models.CharField(max_length=200)
	role_alignment = models.CharField(max_length=200)

	def __str__(self):
		return self.role_title


class Player(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class WolfNumber(models.Model):
	number = models.IntegerField()


class RoleAssignment(models.Model):
	role_score = models.IntegerField()
	role_title = models.CharField(max_length=200)
	player_name = models.CharField(max_length=200)
	role_alignment = models.CharField(max_length=200)

	def __str__(self):
		return self.role_title
