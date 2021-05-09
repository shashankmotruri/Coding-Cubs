from django.db import models

# Create your models here.
class practice(models.Model):
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
    category = models.CharField(blank=True, max_length=32, choices=CATEGORY_CHOICES)
    question = models.TextField()
    testinputs = models.CharField(blank=True, max_length=32)
    answersource = models.TextField()

    def __str__(self):
        return self.category + " " + self.question