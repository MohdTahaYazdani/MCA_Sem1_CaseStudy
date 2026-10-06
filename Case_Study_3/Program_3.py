#  Event Email Audit & VIP Entry


# Email ID of registered users
registered = ["zara@gmail.com","arjun@gmail.com","meera@gmail.com","kabir@gmail.com","riya@gmail.com","zara@gmail.com","dev@gmail.com","anaya@gmail.com","rohan@gmail.com","isha@gmail.com",
                "vihaan@gmail.com","tara@gmail.com","aditya@gmail.com","naina@gmail.com","kiaan@gmail.com","meera@gmail.com","aryan@gmail.com","siya@gmail.com","rahul@gmail.com","avni@gmail.com",
                "rehan@gmail.com","diya@gmail.com","yash@gmail.com","myra@gmail.com","zayn@gmail.com","kabir@gmail.com","aarav@gmail.com","sara@gmail.com","ishaan@gmail.com","kiara@gmail.com",
                "vivaan@gmail.com","anvi@gmail.com","krish@gmail.com","aisha@gmail.com","dhruv@gmail.com","rohan@gmail.com","tanvi@gmail.com","shaurya@gmail.com","navya@gmail.com","advik@gmail.com",
                "pari@gmail.com","atharv@gmail.com","saanvi@gmail.com","vihaan@gmail.com","arham@gmail.com","mira@gmail.com","reyansh@gmail.com","isha@gmail.com","samaira@gmail.com","rudra@gmail.com",
                "zoya@gmail.com","aaryan@gmail.com","mahira@gmail.com","darsh@gmail.com","kavya@gmail.com","dev@gmail.com","arnav@gmail.com","suhana@gmail.com","ved@gmail.com","aanya@gmail.com",
                "laksh@gmail.com","rhea@gmail.com","manav@gmail.com","anika@gmail.com","om@gmail.com","tara@gmail.com","parth@gmail.com","mishti@gmail.com","ritvik@gmail.com","alina@gmail.com",
                "ayush@gmail.com","sanaya@gmail.com","varun@gmail.com","shreya@gmail.com","harsh@gmail.com","naina@gmail.com","rohit@gmail.com","anaya@gmail.com","kunal@gmail.com","lavanya@gmail.com",
                "madhav@gmail.com","isha@gmail.com","priya@gmail.com","nakul@gmail.com","simran@gmail.com","yuvan@gmail.com","aarti@gmail.com","karan@gmail.com","navya@gmail.com","neel@gmail.com",
                "shagun@gmail.com","aman@gmail.com","tanya@gmail.com","rishabh@gmail.com","aisha@gmail.com","siddharth@gmail.com","pihu@gmail.com","vansh@gmail.com","manya@gmail.com","abhay@gmail.com",
                "isha@gmail.com","rohan@gmail.com","aarav@gmail.com","zoya@gmail.com","meera@gmail.com","kabir@gmail.com","riya@gmail.com","dev@gmail.com","anaya@gmail.com","vihaan@gmail.com",
                "tara@gmail.com","naina@gmail.com","shreya@gmail.com","arjun@gmail.com","kiara@gmail.com","yash@gmail.com","siya@gmail.com","dhruv@gmail.com","zara@gmail.com","rahul@gmail.com"]
# Email ID who attained the program
checked_in = ['kabir@gmail.com','madhav@gmail.com','priya@gmail.com', "vansh@gmail.com",
                    'avni@gmail.com', 'aryan@gmail.com','sara@gmail.com', 'krish@gmail.com',
                    'aaryan@gmail.com', 'abhay@gmail.com', 'manya@gmail.com', 'alina@gmail.com',
                    'yash@gmail.com', 'aditya@gmail.com', 'om@gmail.com', 'shreya@gmail.com',
                    'nakul@gmail.com', 'mishti@gmail.com', 'sanaya@gmail.com', 'neel@gmail.com',
                    'rudra@gmail.com', 'rhea@gmail.com', 'manav@gmail.com', 'rehan@gmail.com',
                    'tara@gmail.com', 'vihaan@gmail.com', 'isha@gmail.com', 'zayn@gmail.com',
                    'advik@gmail.com', 'laksh@gmail.com', 'ayush@gmail.com', 'shagun@gmail.com',
                    'ishaan@gmail.com', 'aarav@gmail.com', 'siddharth@gmail.com', 'zoya@gmail.com',
                    'dhruv@gmail.com', 'simran@gmail.com', 'naina@gmail.com', 'aisha@gmail.com',
                    'parth@gmail.com', 'varun@gmail.com', 'suhana@gmail.com', 'siya@gmail.com',
                    'rahul@gmail.com', 'ved@gmail.com', 'arham@gmail.com', 'navya@gmail.com',
                    'myra@gmail.com', 'arnav@gmail.com', 'ritvik@gmail.com', 'samaira@gmail.com',
                    'shaurya@gmail.com', 'dev@gmail.com', 'vivaan@gmail.com']
# Email ID of VIP users
vip_list =["anaya@gmail.com","riya@gmail.com","aisha@gmail.com","yash@gmail.com",
            "kiara@gmail.com","pari@gmail.com","darsh@gmail.com","rohan@gmail.com",
            "rohit@gmail.com","arnav@gmail.com" ,'abhay@gmail.com','siddharth@gmail.com']


# Task-1 Converting raw registrants int unique using "set"
unique_registered = set(registered)
unique_checked_in = set(checked_in)
unique_vip = set(vip_list)


# Task-2 Intersection to identify attending VIPs
vip_present =  unique_checked_in.intersection(unique_vip)

# Task-3 Difference to get Absentees
absentees = unique_registered - unique_checked_in

attendance_rate = float(len(unique_checked_in) / len(unique_registered)) * 100

# Task-4 Verify user Email who have registered
user = input("Enter user mail if registered: ").lower().strip()

if user in unique_registered:
# (Dashboard Report)
    print("="*50)
    print(f"{'EVENT CHECK-IN ANALYTICS DASHBOARD':^50}")
    print("="*50)
    print(f"{'Metric':<30} | {'count':<20}")
    print("-"*50)
    print(f"{'Total Unique Registrations':<30} | {len(unique_registered)}")
    print(f"{'Actual Check-ins':<30} | {len(unique_checked_in)}")
    print(f"{'Absentees':<30} | {len(absentees)}")
    print(f"{'VIP Guests Present':<30} | {len(vip_present)}")
    print("-"*50)
    print(f"{'Attendance Rate':<30} : {attendance_rate:.2f} %")
    print("="*50)
else:
    print("Invalid! User has not registered")
