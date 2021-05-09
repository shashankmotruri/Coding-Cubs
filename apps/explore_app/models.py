from django.db import models

# Create your models here.
class Feedback(models.Model):

    RATING_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    name = models.CharField(max_length=64)
    email = models.EmailField()
    rating = models.CharField(max_length=32, choices=RATING_CHOICES)
    comment = models.TextField(blank=True)

class explore(models.Model):
    CATEGORY_CHOICES = (
        ('Array','Array'),
        ('Matrix','Matrix'),
        ('String','String'),
        ('Searching & Sorting','Searching & Sorting'),
        ('LinkedList','LinkedList'),
        ('Binary Trees','Binary Trees'),
        ('Binary Search Trees','Binary Search Trees'),
        ('Greedy','Greedy'),
        ('BackTracking','BackTracking'),
        ('Stacks & Queues','Stacks & Queues'),
        ('Heap','Heap'),
        ('Graph','Graph'),
        ('Trie','Trie'),
        ('Dynamic Programming','Dynamic Programming'),
        ('Bit Manipulation','Bit Manipulation')
    )

    topic = models.CharField(max_length=128)
    category = models.CharField(blank=True, max_length=32, choices=CATEGORY_CHOICES)
    source = models.CharField(blank=True, max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.category + " " + self.topic
