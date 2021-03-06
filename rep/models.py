from django.db import models


class Song(models.Model):
	title=models.CharField(max_length=50)
	composer=models.ForeignKey('Composer')
	collection=models.CharField(max_length=75, null=True)
	language=models.CharField(max_length=50)
	librettist_first_name=models.CharField(max_length=75, null=True, blank=True)
	librettist_last_name=models.CharField(max_length=75, null=True, blank=True)
	slug=models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title 


class Program(models.Model):
	name=models.CharField(max_length=200)
	songs=models.ManyToManyField(Song, through='ProgramSong')
	create_date=models.DateField()
	perf_date=models.DateField()
	slug=models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Composer(models.Model):
	first_name=models.CharField(max_length=25,)
	last_name=models.CharField(max_length=25)
	birth_year=models.IntegerField(max_length=4)
	death_year=models.IntegerField(max_length=4, null=True, blank=True, default=0)

	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)

class ProgramSong(models.Model):
	song=models.ForeignKey(Song)
	program=models.ForeignKey(Program)
	order=models.IntegerField(blank=True, null=True, default=0)

	def __str__(self):
		return self.song.title

class Artist(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	website=models.CharField(max_length=75, null=True, blank=True,)

	def __str__(self):
		return '%s, %s' % (self.first_name, self.last_name)