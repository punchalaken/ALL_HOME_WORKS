# Generated by Django 4.2.7 on 2023-11-13 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_scope_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='articles.tag'),
        ),
    ]