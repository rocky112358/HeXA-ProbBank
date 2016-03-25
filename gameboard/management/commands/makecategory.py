from django.core.management import BaseCommand
from gameboard.models import Categories

class Command(BaseCommand):
    help = "Create problem category"

    def add_arguments(self, parser):
        parser.add_argument('title', nargs='+', type=str)
        parser.add_argument('color', nargs='+', type=str)

    def handle(self, *args, **options):
        if options["title"]:
            title = options["title"][0]

        if options["color"]:
            color = options["color"][0]

        category, created = Categories.objects.update_or_create(title=title, defaults={"color": color})
        if created:
            print "[ProbBank] Category %s (color: %s) is created" % (title, color)
        else:
            print "[ProbBank] Category %s (color: %s) is updated" % (title, color)
    
