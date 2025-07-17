from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        locations = ['Lagos', 'Abuja', 'Nairobi', 'Accra']
        Listing.objects.all().delete()

        for i in range(10):
            Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='A wonderful place to stay!',
                location=random.choice(locations),
                price_per_night=random.uniform(30, 200),
                available=True
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings.'))
