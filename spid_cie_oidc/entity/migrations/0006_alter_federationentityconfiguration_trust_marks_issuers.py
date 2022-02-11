# Generated by Django 4.0.2 on 2022-02-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0005_alter_trustchain_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='federationentityconfiguration',
            name='trust_marks_issuers',
            field=models.JSONField(blank=True, default=dict, help_text='Only usable for Trust Anchors and intermediates. Which issuers are allowed to issue trust marks for the descendants. Example: {"https://www.spid.gov.it/certification/rp": ["https://registry.spid.agid.gov.it", "https://intermediary.spid.it"],"https://sgd.aa.it/onboarding": ["https://sgd.aa.it", ]}'),
        ),
    ]