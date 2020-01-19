# Generated by Django 3.0.2 on 2020-01-19 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200119_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weightage', models.PositiveIntegerField()),
                ('Answer_text', models.CharField(max_length=255)),
                ('Question_related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_domain', to='quiz.DomainQuestion')),
                ('from_Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_domain_in_specific', to='quiz.Domain')),
            ],
        ),
    ]
