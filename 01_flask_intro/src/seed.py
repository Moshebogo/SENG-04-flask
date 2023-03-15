from models import db, Pet, Owner
from faker import Faker
import random
from app import app

fake = Faker()

if __name__ == '__main__':

    with app.app_context():
        Pet.query.delete()
        Owner.query.delete()

        owners = []
        for x in range(20):
            owner = Owner(first_name=fake.first_name(),
                            last_name=fake.last_name())
            owners.append(owner)
        db.session.add_all(owners)     

        pets = []
        species = ['dog', 'cat', 'horse', 'fish', 'dolphin', 'lion', 'eagle']
        for x in range(100):
            pet = Pet(name=fake.name(),
                        species=random.choice(species),
                        owner=random.choice(owners))
            pets.append(pet)
        db.session.add_all(pets)  

        db.session.commit()