# Generated by Django 4.0.2 on 2022-03-02 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_provider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oidcsession',
            name='user_claims',
        ),
    ]
