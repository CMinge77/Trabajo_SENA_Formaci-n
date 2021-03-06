# Generated by Django 3.2.5 on 2021-08-19 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='servicio',
            name='categorias',
            field=models.ManyToManyField(to='servicios.Categoria_servicios'),
        ),
    ]
