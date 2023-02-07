# Generated by Django 4.1.4 on 2023-01-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
        ('players', '0007_alter_results_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.players'),
        ),
        migrations.AlterField(
            model_name='results',
            name='result',
            field=models.CharField(choices=[('WINNER', 'WINNER'), ('RUNNER-UP', 'RUNNER-UP'), ('SEMI-FINALIST', 'SEMI-FINALIST'), ('QUARTER-FINALIST', 'QUARTER-FINALIST'), ('ROUND OF 16', 'ROUND OF 16'), ('ROUND OF 32', 'ROUND OF 32'), ('ROUND OF 64', 'ROUND OF 64'), ('ROUND OF 128', 'ROUND OF 128')], max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournaments'),
        ),
    ]
