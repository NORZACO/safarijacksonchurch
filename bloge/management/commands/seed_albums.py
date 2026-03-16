import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from faker import Faker

from bloge.models import Album


fake = Faker()


class Command(BaseCommand):
    help = "Generate fake album data"

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=10,
            help='Number of fake albums to create'
        )

    def handle(self, *args, **kwargs):

        total = kwargs['total']

        users = list(User.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR(
                "No users found. Create users first."))
            return

        categories = [
            "Church Events",
            "Community",
            "Worship",
            "Youth",
            "Outreach"
        ]

        for i in range(total):

            title = fake.sentence(nb_words=4)

            album = Album.objects.create(
                title=title,
                description=fake.text(max_nb_chars=600),
                image= fake."blog_posts/images/sample.jpg",
                avatar="blog_posts/images/avatar.jpg",
                category=random.choice(categories),
                author=random.choice(users),
                publish_date=timezone.now(),
                status=random.choice(['published', 'draft']),
                slug=slugify(title) + "-" + str(random.randint(1, 9999))
            )

            # random likes
            like_users = random.sample(users, random.randint(0, len(users)))

            for user in like_users:
                album.likes.add(user)

            self.stdout.write(self.style.SUCCESS(
                f"Created album: {album.title}"))

        self.stdout.write(self.style.SUCCESS(
            f"\n{total} fake albums created."))
