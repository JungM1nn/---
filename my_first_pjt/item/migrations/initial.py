import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('price', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='가격')),
                ('description', models.TextField(verbose_name='설명')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='이미지')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('likes', models.ManyToManyField(related_name='liked_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]