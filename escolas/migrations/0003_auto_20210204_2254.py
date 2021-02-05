# Generated by Django 3.1.4 on 2021-02-05 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0002_auto_20210204_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contem',
            name='codigoDisciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.disciplina'),
        ),
        migrations.AlterField(
            model_name='contem',
            name='codigoTurma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.turma'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='codigoAluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.aluno'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='codigoTurma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.turma'),
        ),
        migrations.AlterField(
            model_name='ministra',
            name='codigoDisciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.disciplina'),
        ),
        migrations.AlterField(
            model_name='ministra',
            name='codigoProfessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.professor'),
        ),
        migrations.AlterField(
            model_name='promove',
            name='codigoDisciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.disciplina'),
        ),
        migrations.AlterField(
            model_name='promove',
            name='codigoHabilidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.habilidade'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigoEscola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escolas.escola'),
        ),
    ]
