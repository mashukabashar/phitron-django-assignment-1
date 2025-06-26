import os
import django
from faker import Faker
import random
from events.models import Participant, Event, Category

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

# Function to populate the database


def populate_db():
    fake = Faker()


    category = [Category.objects.create(
        name=fake.bs().capitalize(),
        description=fake.paragraph(),
    ) for _ in range(5)]
    print(f"Created {len(category)} categories.")


    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.unique.email()
    ) for _ in range(10)]
    print(f"Created {len(participants)} participants.")

 
    events = []
    for _ in range(20):
        event = Event.objects.create(name=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            date=fake.date_this_year(),
            time=fake.time(),
            location=fake.address(),
            category=random.choice(category)
        )
        event.guests.set(random.sample(participants, random.randint(1, 3)))
        events.append(event)
    print(f"Created {len(events)} events.")


