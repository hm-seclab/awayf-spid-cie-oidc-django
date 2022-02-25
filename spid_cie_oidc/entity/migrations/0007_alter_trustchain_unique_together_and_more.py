# Generated by Django 4.0.2 on 2022-02-25 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0006_remove_trustchain_resultant_metadata_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trustchain',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='trustchain',
            name='trust_anchor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spid_cie_oidc_entity.fetchedentitystatement'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trustchain',
            name='iat',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='trustchain',
            unique_together={('sub', 'type', 'trust_anchor')},
        ),
    ]
