# Experiment 12: Seminar, Workshop & Hackathon File Dashboard

# Declare file and their records
filename = "academic_events.txt"
events = [("Seminar","AI & Data Science",120),
("Workshop","Python Programming",80),
("Hackathon","Innovation Challenge",150),
("Seminar","Machine Learning",100),
("Workshop","CyberSecurity",75)]

# Open the file to write the records in it
with open(filename,"w") as f:
    for evt,title,p in events:
        f.write(f"{evt},{title},{p}\n")

counts = {"Seminar":0,"Workshop":0,"Hackathon":0}
total = 0

# Open the file to read the records and counts the events & participants
with open(filename,"r") as f:
    for line in f:
        evt,title,p = line.strip().split(",")
        counts[evt] += 1
        total += int(p)

# Display records on the Dashboard
print("="*50)
print(f"{'SEMINAR / WORKSHOP / HACKATHON DASHBOARD':^50}")
print("="*50)
print(f"{'Seminars: '}{counts["Seminar"]}")
print(f"{'Workshops: '}{counts["Workshop"]}")
print(f"{'Hackathons: '}{counts["Hackathon"]}")
print(f"{'Total Participants: '}{total}")
print("="*50)