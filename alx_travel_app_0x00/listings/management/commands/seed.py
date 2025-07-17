from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = [
            "Cozy Cabin in the Woods", "Luxury City Apartment", "Beachfront Bungalow",
            "Mountain Retreat", "Modern Studio Downtown"
        ]

        Listing.objects.all().delete()

        for title in titles:
            listing = Listing.objects.create(
                title=title,
                description=f"{title} is a great place to stay!",
                location=random.choice(['Lagos', 'Abuja', 'Nairobi', 'Cape Town', 'Accra']),
                price_per_night=random.uniform(50.0, 300.0),
                available=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
