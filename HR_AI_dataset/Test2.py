import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define designer roles and their associated skills
designer_roles = [
    "UI/UX Designer", "Graphic Designer", "Motion Designer", 
    "Industrial Designer", "Game Designer", "Fashion Designer"
]

skills = {
    "UI/UX Designer": ["Wireframing", "User Research", "Prototyping", "Figma", "Adobe XD", "Usability Testing"],
    "Graphic Designer": ["Adobe Photoshop", "Illustration", "Typography", "Branding", "Color Theory", "Vector Graphics"],
    "Motion Designer": ["After Effects", "3D Animation", "Storyboarding", "Cinematic Effects", "Kinetic Typography", "Visual Effects"],
    "Industrial Designer": ["3D Modeling", "Product Prototyping", "Material Selection", "AutoCAD", "Ergonomics", "Manufacturing Process"],
    "Game Designer": ["Level Design", "Character Development", "Unity", "Unreal Engine", "Gameplay Mechanics", "World Building"],
    "Fashion Designer": ["Textile Design", "Pattern Making", "Draping", "Sustainable Fashion", "Trend Forecasting", "Garment Construction"]
}

scoring_range = list(range(11))  # Scores from 0 to 10

# Diverse instruction templates
instruction_templates = [
    "Evaluate the effectiveness of the {role} in using {skill}.",
    "Analyze how the {role} incorporated {skill} into their design process.",
    "Did the {role} successfully apply {skill} to enhance the project? Explain why.",
    "Assess the {role}'s approach to {skill} and suggest improvements.",
    "Provide feedback on how well the {role} demonstrated expertise in {skill}.",
    "Was the {role}'s execution of {skill} aligned with industry standards?",
    "Discuss how the {role}'s use of {skill} impacted the final outcome.",
    "Rate the proficiency of the {role} in applying {skill} to real-world scenarios.",
    "Explain whether the {role}'s work with {skill} met design expectations.",
    "How did the {role}'s application of {skill} contribute to project success?"
]

# Function to generate a single scenario
def generate_scenario(role):
    skill = random.choice(skills[role])
    action = random.choice([
        f"Created a design using {skill} for a client project.",
        f"Developed an innovative solution using {skill}.",
        f"Optimized an existing design by applying {skill}.",
        f"Collaborated with a team to integrate {skill} into the final product.",
        f"Overcame a design challenge by leveraging {skill}.",
    ])
    result = random.choice([
        "The final design was well-received and exceeded expectations.",
        "The project was completed with minor improvements needed.",
        "The candidate showed strong potential but lacked refinement in execution.",
        "The work did not fully meet the objectives and required further iterations.",
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
            role = random.choice(designer_roles)
            set_data.append(generate_scenario(role))
        data.append(set_data)
    return data

# Generate data
data = generate_bulk_data(sets=20, turns=10)

# Save to a JSON file
output_file = "designer_scenarios.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Generated 10 sets of 10 designer interview scenarios and saved to {output_file}")
