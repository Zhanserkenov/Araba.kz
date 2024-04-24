from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.TextField()),
                ('liked', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='api.Category')),  # Изменено
            ],
        ),
    ]
