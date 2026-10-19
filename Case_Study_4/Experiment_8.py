# Experiment 8: Job Mela Candidate Selection Dashboard

# Function to check Eligibility
def eligible(p):
    return p >= 60

# Candidate list
candidate = [("Taha",90) , ("Ahmad",80) , ("Zeeshan",65) , ("Adnan",40) , ("Sabir",85)]

# Selected Candidate list
selected = ({'name':n , 'percentage':p} for n,p in candidate  if eligible(p))

# Sorting Selected Candidates by percentage
selected = sorted(selected, key=lambda  x: x["percentage"] , reverse=True)

# Print Dashboard
print("="*50)
print(f"{'JOB MELA DASHBOARD':^50}")
print("="*50)
print(f"{'Total Candidates: '} {len(candidate)}")
print(f"{'Eligible: '} {len(selected)}")
for i,c in enumerate(selected , 1):
    print(f"{i} {c['name']} - {c['percentage']} %")
print("="*50)