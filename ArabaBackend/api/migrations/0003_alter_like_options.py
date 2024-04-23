from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
    ]
