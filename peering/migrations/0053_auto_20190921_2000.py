# Generated by Django 2.2.5 on 2019-09-21 18:00

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("peering", "0052_auto_20190818_1926"),
        ("utils", "0005_tag_taggeditem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autonomoussystem",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="bgpgroup",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="community",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="directpeeringsession",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="internetexchangepeeringsession",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="router",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="routingpolicy",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="template",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="utils.TaggedItem",
                to="utils.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
