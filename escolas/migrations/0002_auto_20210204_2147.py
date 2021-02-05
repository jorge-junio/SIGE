# Generated by Django 3.1.5 on 2021-02-05 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contem',
            name='codigoDisciplina',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.disciplina'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigoEscola',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='escolas.escola'),
        ),
    ]