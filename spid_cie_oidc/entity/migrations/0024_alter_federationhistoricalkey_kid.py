# Generated by Django 4.2.1 on 2023-07-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spid_cie_oidc_entity", "0023_alter_federationhistoricalkey_jwk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="federationhistoricalkey",
            name="kid",
            field=models.CharField(max_length=128),
        ),
    ]