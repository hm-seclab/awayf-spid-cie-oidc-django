# Generated by Django 4.0.2 on 2022-02-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0003_trustchain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trustchain',
            options={'verbose_name': 'Trust Chain', 'verbose_name_plural': 'Trust Chains'},
        ),
    ]