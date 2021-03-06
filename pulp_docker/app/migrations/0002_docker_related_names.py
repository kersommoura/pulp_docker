# Generated by Django 2.2.4 on 2019-08-19 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blob',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='dockerdistribution',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='dockerremote',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='manifest',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterField(
            model_name='blob',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='docker_blob', serialize=False, to='core.Content'),
        ),
        migrations.AlterField(
            model_name='dockerdistribution',
            name='basedistribution_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='docker_dockerdistribution', serialize=False, to='core.BaseDistribution'),
        ),
        migrations.AlterField(
            model_name='dockerdistribution',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docker_dockerdistribution', to='core.Repository'),
        ),
        migrations.AlterField(
            model_name='dockerdistribution',
            name='repository_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docker_dockerdistribution', to='core.RepositoryVersion'),
        ),
        migrations.AlterField(
            model_name='dockerremote',
            name='remote_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='docker_dockerremote', serialize=False, to='core.Remote'),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='blobs',
            field=models.ManyToManyField(related_name='docker_manifest', through='docker.BlobManifest', to='docker.Blob'),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='docker_manifest', serialize=False, to='core.Content'),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='listed_manifests',
            field=models.ManyToManyField(related_name='docker_manifest', through='docker.ManifestListManifest', to='docker.Manifest'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='docker_tag', serialize=False, to='core.Content'),
        ),
    ]
