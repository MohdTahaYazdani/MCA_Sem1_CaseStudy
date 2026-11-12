#  Fitness Tracker Activity Analytics

# TASK 1: 7 days of logs (list of dictionaries)
activity_log = [
    {'day': 'Mon', 'steps': 10200, 'calories': 450, 'goal_met': True},
    {'day': 'Tue', 'steps': 8500,  'calories': 380, 'goal_met': True},
    {'day': 'Wed', 'steps': 4300,  'calories': 200, 'goal_met': False},
    {'day': 'Thu', 'steps': 11000, 'calories': 500, 'goal_met': True},
    {'day': 'Fri', 'steps': 9100,  'calories': 410, 'goal_met': True},
    {'day': 'Sat', 'steps': 12400, 'calories': 560, 'goal_met': True},
    {'day': 'Sun', 'steps': 6800,  'calories': 310, 'goal_met': False},
]


# TASK 2: Cumulative steps and calories using +=
def compute_totals():
    total_steps = 0
    total_calories = 0
    for entry in activity_log:
        total_steps += entry['steps']
        total_calories += entry['calories']
    return total_steps, total_calories


# TASK 3: Count days the goal was met
def count_goal_days():
    goal_days = 0
    for entry in activity_log:
        if entry['goal_met']:
            goal_days += 1
    return goal_days


# TASK 4: Average daily steps, cast to int
def average_steps(total_steps):
    average = total_steps / len(activity_log)   # float division
    return int(average)                         # whole number for clean display


# TASK 5: Dashboard
def print_dashboard():
    total_steps, total_calories = compute_totals()
    goal_days = count_goal_days()
    avg_steps = average_steps(total_steps)
    completion_rate = (goal_days / len(activity_log)) * 100

    print("=" * 50)
    print("WEEKLY FITNESS ANALYTICS REPORT")
    print("=" * 50)
    print(f"{'Day':<4}| {'Steps':<7}| {'Calories (kcal)':<16}| Daily Goal Met")
    print("-" * 50)
    for entry in activity_log:
        status = "YES" if entry['goal_met'] else "NO"
        print(f"{entry['day']:<4}| {entry['steps']:<7,}| "
              f"{entry['calories']:<16}| {status}")
    print("-" * 50)
    print(f"Total Weekly Steps   : {total_steps:,}")
    print(f"Total Weekly Calories: {total_calories:,} kcal")
    print(f"Average Daily Steps  : {avg_steps:,}")
    print(f"Goal Completion Rate : {completion_rate:.1f}%")
    print("=" * 50)


if __name__ == "__main__":
    print_dashboard()