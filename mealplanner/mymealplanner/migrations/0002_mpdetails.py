# Generated by Django 4.2.1 on 2023-07-06 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymealplanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymealplanner.mpstrategy')),
            ],
        ),
    ]