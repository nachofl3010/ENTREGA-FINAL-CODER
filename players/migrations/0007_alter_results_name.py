# Generated by Django 4.1.4 on 2023-01-29 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_alter_results_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='players.players'),
        ),
    ]
