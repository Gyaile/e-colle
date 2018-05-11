# Generated by Django 2.0.5 on 2018-05-09 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0004_auto_20180506_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='app_mobile',
            field=models.BooleanField(default=False, verbose_name='Application mobile'),
        ),
        migrations.AlterField(
            model_name='config',
            name='default_modif_col',
            field=models.BooleanField(default=False, verbose_name='Modification du colloscope par défaut pour tous les enseignants'),
        ),
        migrations.AlterField(
            model_name='config',
            name='default_modif_groupe',
            field=models.BooleanField(default=False, verbose_name='Modification des groupes par défaut pour tous les enseignants'),
        ),
        migrations.AlterField(
            model_name='config',
            name='ects',
            field=models.BooleanField(default=False, verbose_name='Gestion des fiches de crédits ECTS'),
        ),
        migrations.AlterField(
            model_name='config',
            name='mathjax',
            field=models.BooleanField(default=True, verbose_name='Mise en forme des formules mathématiques avec Mathjax'),
        ),
        migrations.AlterField(
            model_name='config',
            name='modif_prof_col',
            field=models.BooleanField(default=True, verbose_name='Modification du colloscope par les enseignants'),
        ),
        migrations.AlterField(
            model_name='config',
            name='modif_prof_groupe',
            field=models.BooleanField(default=True, verbose_name='Modification des groupes par les enseignants'),
        ),
        migrations.AlterField(
            model_name='config',
            name='modif_secret_col',
            field=models.BooleanField(default=False, verbose_name='Modification du colloscope par le secrétariat'),
        ),
        migrations.AlterField(
            model_name='config',
            name='modif_secret_groupe',
            field=models.BooleanField(default=False, verbose_name='Modification des groupes par le secrétariat'),
        ),
        migrations.AlterField(
            model_name='semaine',
            name='lundi',
            field=models.DateField(choices=[(datetime.date(2017, 7, 31), '31 juillet 2017'), (datetime.date(2017, 8, 7), '07 août 2017'), (datetime.date(2017, 8, 14), '14 août 2017'), (datetime.date(2017, 8, 21), '21 août 2017'), (datetime.date(2017, 8, 28), '28 août 2017'), (datetime.date(2017, 9, 4), '04 septembre 2017'), (datetime.date(2017, 9, 11), '11 septembre 2017'), (datetime.date(2017, 9, 18), '18 septembre 2017'), (datetime.date(2017, 9, 25), '25 septembre 2017'), (datetime.date(2017, 10, 2), '02 octobre 2017'), (datetime.date(2017, 10, 9), '09 octobre 2017'), (datetime.date(2017, 10, 16), '16 octobre 2017'), (datetime.date(2017, 10, 23), '23 octobre 2017'), (datetime.date(2017, 10, 30), '30 octobre 2017'), (datetime.date(2017, 11, 6), '06 novembre 2017'), (datetime.date(2017, 11, 13), '13 novembre 2017'), (datetime.date(2017, 11, 20), '20 novembre 2017'), (datetime.date(2017, 11, 27), '27 novembre 2017'), (datetime.date(2017, 12, 4), '04 décembre 2017'), (datetime.date(2017, 12, 11), '11 décembre 2017'), (datetime.date(2017, 12, 18), '18 décembre 2017'), (datetime.date(2017, 12, 25), '25 décembre 2017'), (datetime.date(2018, 1, 1), '01 janvier 2018'), (datetime.date(2018, 1, 8), '08 janvier 2018'), (datetime.date(2018, 1, 15), '15 janvier 2018'), (datetime.date(2018, 1, 22), '22 janvier 2018'), (datetime.date(2018, 1, 29), '29 janvier 2018'), (datetime.date(2018, 2, 5), '05 février 2018'), (datetime.date(2018, 2, 12), '12 février 2018'), (datetime.date(2018, 2, 19), '19 février 2018'), (datetime.date(2018, 2, 26), '26 février 2018'), (datetime.date(2018, 3, 5), '05 mars 2018'), (datetime.date(2018, 3, 12), '12 mars 2018'), (datetime.date(2018, 3, 19), '19 mars 2018'), (datetime.date(2018, 3, 26), '26 mars 2018'), (datetime.date(2018, 4, 2), '02 avril 2018'), (datetime.date(2018, 4, 9), '09 avril 2018'), (datetime.date(2018, 4, 16), '16 avril 2018'), (datetime.date(2018, 4, 23), '23 avril 2018'), (datetime.date(2018, 4, 30), '30 avril 2018'), (datetime.date(2018, 5, 7), '07 mai 2018'), (datetime.date(2018, 5, 14), '14 mai 2018'), (datetime.date(2018, 5, 21), '21 mai 2018'), (datetime.date(2018, 5, 28), '28 mai 2018'), (datetime.date(2018, 6, 4), '04 juin 2018'), (datetime.date(2018, 6, 11), '11 juin 2018'), (datetime.date(2018, 6, 18), '18 juin 2018'), (datetime.date(2018, 6, 25), '25 juin 2018'), (datetime.date(2018, 7, 2), '02 juillet 2018'), (datetime.date(2018, 7, 9), '09 juillet 2018'), (datetime.date(2018, 7, 16), '16 juillet 2018'), (datetime.date(2018, 7, 23), '23 juillet 2018'), (datetime.date(2018, 7, 30), '30 juillet 2018'), (datetime.date(2018, 8, 6), '06 août 2018'), (datetime.date(2018, 8, 13), '13 août 2018'), (datetime.date(2018, 8, 20), '20 août 2018'), (datetime.date(2018, 8, 27), '27 août 2018'), (datetime.date(2018, 9, 3), '03 septembre 2018'), (datetime.date(2018, 9, 10), '10 septembre 2018'), (datetime.date(2018, 9, 17), '17 septembre 2018'), (datetime.date(2018, 9, 24), '24 septembre 2018'), (datetime.date(2018, 10, 1), '01 octobre 2018'), (datetime.date(2018, 10, 8), '08 octobre 2018'), (datetime.date(2018, 10, 15), '15 octobre 2018'), (datetime.date(2018, 10, 22), '22 octobre 2018'), (datetime.date(2018, 10, 29), '29 octobre 2018'), (datetime.date(2018, 11, 5), '05 novembre 2018'), (datetime.date(2018, 11, 12), '12 novembre 2018'), (datetime.date(2018, 11, 19), '19 novembre 2018'), (datetime.date(2018, 11, 26), '26 novembre 2018'), (datetime.date(2018, 12, 3), '03 décembre 2018'), (datetime.date(2018, 12, 10), '10 décembre 2018'), (datetime.date(2018, 12, 17), '17 décembre 2018'), (datetime.date(2018, 12, 24), '24 décembre 2018'), (datetime.date(2018, 12, 31), '31 décembre 2018'), (datetime.date(2019, 1, 7), '07 janvier 2019'), (datetime.date(2019, 1, 14), '14 janvier 2019'), (datetime.date(2019, 1, 21), '21 janvier 2019'), (datetime.date(2019, 1, 28), '28 janvier 2019'), (datetime.date(2019, 2, 4), '04 février 2019'), (datetime.date(2019, 2, 11), '11 février 2019'), (datetime.date(2019, 2, 18), '18 février 2019'), (datetime.date(2019, 2, 25), '25 février 2019'), (datetime.date(2019, 3, 4), '04 mars 2019'), (datetime.date(2019, 3, 11), '11 mars 2019'), (datetime.date(2019, 3, 18), '18 mars 2019'), (datetime.date(2019, 3, 25), '25 mars 2019'), (datetime.date(2019, 4, 1), '01 avril 2019'), (datetime.date(2019, 4, 8), '08 avril 2019'), (datetime.date(2019, 4, 15), '15 avril 2019'), (datetime.date(2019, 4, 22), '22 avril 2019'), (datetime.date(2019, 4, 29), '29 avril 2019'), (datetime.date(2019, 5, 6), '06 mai 2019'), (datetime.date(2019, 5, 13), '13 mai 2019'), (datetime.date(2019, 5, 20), '20 mai 2019'), (datetime.date(2019, 5, 27), '27 mai 2019'), (datetime.date(2019, 6, 3), '03 juin 2019'), (datetime.date(2019, 6, 10), '10 juin 2019'), (datetime.date(2019, 6, 17), '17 juin 2019'), (datetime.date(2019, 6, 24), '24 juin 2019')], default=datetime.date(2018, 5, 7), unique=True),
        ),
    ]
