# Generated by Django 3.1.5 on 2021-05-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Array', 'Array'), ('Matrix', 'Matrix'), ('String', 'String'), ('Searching & Sorting', 'Searching & Sorting'), ('LinkedList', 'LinkedList'), ('Binary Trees', 'Binary Trees'), ('Binary Search Trees', 'Binary Search Trees'), ('Greedy', 'Greedy'), ('BackTracking', 'BackTracking'), ('Stacks & Queues', 'Stacks & Queues'), ('Heap', 'Heap'), ('Graph', 'Graph'), ('Trie', 'Trie'), ('Dynamic Programming', 'Dynamic Programming'), ('Bit Manipulation', 'Bit Manipulation')], max_length=32)),
                ('question', models.TextField()),
                ('testinputs', models.CharField(blank=True, max_length=32)),
                ('answersource', models.TextField()),
            ],
        ),
    ]
