import csv
from faker import Faker

fake = Faker()
records = 1000000

with open('large_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write Header
    writer.writerow(['id', 'name', 'email', 'city', 'created_at'])
    
    for i in range(1, records + 1):
        writer.writerow([
            i, 
            fake.name(), 
            fake.email(), 
            fake.city(), 
            "2026-04-04"
        ])
        
        # Optional: Print progress every 100k rows
        if i % 100000 == 0:
            print(f"Generated {i} rows...")
