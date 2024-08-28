# Generated by Django 5.1 on 2024-08-28 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayaate', '0005_alter_video_description_product_affiliate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='posts/')),
                ('views', models.PositiveIntegerField(default=0)),
                ('reactions', models.JSONField(blank=True, default=dict)),
                ('status', models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='ayaate.category')),
                ('products', models.ManyToManyField(blank=True, related_name='posts', to='ayaate.product')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='ayaate.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ayaate.post')),
            ],
        ),
    ]
