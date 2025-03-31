import random
from faker import Faker
import json

# Initialize Faker instance
fake = Faker()

# Define roles and their associated skills
roles = ["Operations Manager", "Strategy Manager", "Manufacturing Manager"]

skills = {
    "Operations Manager": ["Supply Chain", "Process Optimization", "Lean Manufacturing", "Inventory Management", "Logistics"],
    "Strategy Manager": ["Market Analysis", "Business Growth", "Competitive Analysis", "Financial Planning", "Corporate Strategy"],
    "Manufacturing Manager": ["Production Planning", "Quality Control", "Lean Manufacturing", "Automation", "Supply Chain Management"]
}

scoring_range = list(range(11))  # Scores from 0 to 10

# Different types of instructions for more variation
instruction_templates = [
    "Assess how effectively the {role} handled {skill}.",
    "Review the decision-making process used by the {role} in implementing {skill}.",
    "Analyze the impact of {skill} on the {role}'s overall performance.",
    "Did the {role} successfully apply {skill} in this scenario? Justify your reasoning.",
    "Evaluate the efficiency of the {role}'s approach in using {skill}.",
    "Provide feedback on how well the {role} utilized {skill} to solve the challenge.",
    "Was the {role}'s execution of {skill} effective in achieving the desired outcome?",
    "How would you rate the {role}'s ability to apply {skill} in a real-world situation?",
    "Discuss the strengths and weaknesses in how the {role} implemented {skill}.",
    "Explain whether the {role}'s approach to {skill} aligns with industry best practices."
]

# Function to generate a single scenario
def generate_scenario(role):
    skill = random.choice(skills[role])
    action = random.choice([
        f"Implemented {skill} strategies to improve efficiency.",
        f"Led a team in using {skill} for a major project.",
        f"Optimized processes using {skill}.",
        f"Developed an innovative solution using {skill}.",
        f"Improved operations by integrating {skill} tools.",
    ])
    result = random.choice([
        "The project was a success and significantly improved system performance.",
        "The task faced some challenges but was eventually completed with minor issues.",
        "The candidate demonstrated an excellent understanding but did not complete the project.",
        "The project did not meet the required objectives, and additional improvements are necessary.",
    ])
    score = random.choice(scoring_range)
    
    instruction = random.choice(instruction_templates).format(role=role, skill=skill)

    return {
        "type": "cot_reasoning",
        "instruction": instruction,
        "input": f"Candidate's response: '{action}'",
        "output": result,
        "scoring": str(score)
    }

# Function to generate 10 sets of data, each with 10 turns
def generate_bulk_data(sets=10, turns=10):
    data = []
    for _ in range(sets):
        set_data = []
        for _ in range(turns):
            role = random.choice(roles)
            set_data.append(generate_scenario(role))
        data.append(set_data)
    return data

# Generate 10 sets of 10 turns
data = generate_bulk_data(sets=50, turns=10)

# Save the generated data to a JSON file
with open("generated_data2.json", "w") as f:
    json.dump(data, f, indent=4)

print("Generated data saved to 'generated_data2.json'")
