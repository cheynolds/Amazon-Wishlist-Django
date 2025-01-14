# Generated by Django 5.1.2 on 2024-10-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
