import pandas as pd
import base64
import random
import string

# Set a seed for reproducibility
seed = 202310
random.seed(seed)

# generate a random password using base64 encoding
def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Load the CSV file
csv_file = 'sv_roster_2023_prod.csv'
df = pd.read_csv(csv_file)

num_users = df.shape[0]  
password_length = 8  

# Generate passwords for each user and update the 'password' column
df['password'] = [generate_password(password_length) for _ in range(num_users)]

# Save the updated DataFrame back to the CSV file
df.to_csv(csv_file, index=False)
