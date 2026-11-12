# HR Candidate Skill-Matching Analyzer

# TASK 1: Job requirements as a set
job_requirements = {'Python', 'SQL', 'Git', 'Docker'}

# Sets are unordered, so this list fixes the order skills appear in the report
SKILL_ORDER = ['Python', 'SQL', 'Git', 'Docker']

# TASK 2: Candidate profiles {name: set of skills}
candidates = {
    'Sarah': {'Python', 'SQL', 'Git', 'Docker', 'AWS'},   # has all, plus an extra
    'John':  {'Python', 'SQL', 'Excel'},
    'Mike':  {'SQL', 'Java'},
}


# Helpers for report formatting
def format_skills(skills, limit=14):
    """Join skills in display order; shorten with '...' if too long."""
    ordered = [s for s in SKILL_ORDER if s in skills]
    text = ", ".join(ordered)
    if len(text) > limit:
        text = text[:limit - 3] + "..."
    return text


# TASKS 3 & 4: Matching and scoring
def evaluate_candidate(skills):
    matched = job_requirements.intersection(skills)       # skills they have
    missing = job_requirements.difference(skills)         # skills they lack
    if len(job_requirements) == 0:
        score = 0.0
    else:
        score = (len(matched) / len(job_requirements)) * 100.0   # float math
    return matched, missing, score


def analyze_all():
    results = []
    for name, skills in candidates.items():
        matched, missing, score = evaluate_candidate(skills)
        results.append((name, score, matched, missing))
    # Rank: highest score first, ties broken alphabetically by name
    results.sort(key=lambda r: (-r[1], r[0]))
    return results


# TASK 5: Report
def print_report():
    results = analyze_all()

    print("=" * 50)
    print("HR RECRUITMENT MATCH REPORT")
    print("=" * 50)
    print(f"{'Candidate':<10}| {'Match Score':<12}| {'Matched Skills':<15}| Missing")
    print("-" * 50)
    for name, score, matched, missing in results:
        score_text = f"{score:.0f}%"
        matched_text = "All Required" if not missing else format_skills(matched)
        missing_text = "None" if not missing else format_skills(missing)
        print(f"{name:<10}| {score_text:<12}| {matched_text:<15}| {missing_text}")
    print("-" * 50)
    best_name, best_score = results[0][0], results[0][1]
    print(f"Best Candidate Match : {best_name} ({best_score:.0f}%)")
    print("=" * 50)


if __name__ == "__main__":
    print_report()