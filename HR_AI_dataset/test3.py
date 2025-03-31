import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define behavioral traits HR evaluates
behavioral_traits = {
    "Leadership": [
        "Guiding a team through a challenging project",
        "Taking initiative in an uncertain situation",
        "Handling conflict within a team",
        "Motivating colleagues towards a common goal"
    ],
    "Teamwork": [
        "Collaborating with diverse team members",
        "Encouraging input from all team members",
        "Supporting a struggling colleague",
        "Compromising for team success"
    ],
    "Adaptability": [
        "Adjusting to a new work environment",
        "Quickly learning new skills under pressure",
        "Handling an unexpected role change",
        "Working on multiple projects with changing priorities"
    ],
    "Problem-Solving": [
        "Finding a solution to a critical system failure",
        "Overcoming a budget constraint in a project",
        "Resolving customer complaints efficiently",
        "Analyzing data to improve company performance"
    ],
    "Communication": [
        "Delivering a persuasive presentation",
        "Handling a difficult conversation professionally",
        "Clarifying misunderstandings in a project",
        "Negotiating successfully with a client"
    ],
    "Time Management": [
        "Prioritizing tasks under tight deadlines",
        "Managing workload during peak times",
        "Balancing multiple responsibilities",
        "Optimizing work processes for efficiency"
    ],
    "Creativity": [
        "Developing an innovative marketing strategy",
        "Designing a unique product feature",
        "Thinking outside the box to solve a challenge",
        "Introducing a fresh approach to customer engagement"
    ],
    "Work Ethic": [
        "Demonstrating commitment to long-term goals",
        "Going above and beyond to complete a task",
        "Maintaining integrity in difficult situations",
        "Consistently meeting or exceeding expectations"
    ],
    "Conflict Resolution": [
        "Mediating a dispute between coworkers",
        "Turning a disagreement into a constructive discussion",
        "Defusing a tense situation between employees",
        "Finding a win-win solution to a workplace issue"
    ],
    "Decision-Making": [
        "Making a quick but informed decision under pressure",
        "Weighing pros and cons before finalizing a choice",
        "Choosing between multiple viable solutions",
        "Handling ethical dilemmas in decision-making"
    ],
    "Stress Management": [
        "Handling high-pressure situations with composure",
        "Finding ways to maintain productivity under stress",
        "Avoiding burnout while managing a heavy workload",
        "Helping others stay calm in stressful environments"
    ]
}

# Scoring criteria (0-10 scale)
scoring_range = list(range(11))

# Expanded candidate response templates
candidate_responses = [
    "During a project, I faced {scenario}. I handled it by {action}, which led to {result}.",
    "A challenge I encountered was {scenario}. I responded by {action}, and the outcome was {result}.",
    "I believe {trait} is critical in any role. In one case, {scenario} happened, so I {action}, resulting in {result}.",
    "One instance where I used {trait} was when {scenario}. I adapted by {action}, which improved {result}.",
    "While working on {scenario}, I relied on {trait} to {action}. This helped achieve {result}.",
    "When I faced {scenario}, I chose to {action}, and this decision led to {result}."
]

# Expanded HR evaluation feedback
evaluation_feedback = [
    "The candidate effectively demonstrated {trait} in their response with a strong example.",
    "Their answer showcased a solid understanding of {trait}, but lacked a detailed explanation.",
    "The response showed potential, but they could improve on structuring their approach to {trait}.",
    "While the candidate provided an example, it did not fully illustrate their {trait} skills in depth.",
    "The response was well-articulated and displayed a high level of competence in {trait}.",
    "The example was relevant, but it could have included more specifics on the impact of {trait}.",
    "The candidate showed a good grasp of {trait}, but their execution in the scenario seemed unclear.",
    "This was a strong answer, highlighting a deep understanding of {trait} and its applications.",
    "The example was fair, but the response lacked depth in problem analysis and resolution.",
    "A great demonstration of {trait}, showcasing initiative and clear decision-making skills."
]

# Instruction templates (NO QUESTIONS, only direct instructions)
instruction_templates = [
    "Analyze the candidate's ability to handle {trait}.",
    "Evaluate how well the candidate manages {trait} in workplace scenarios.",
    "Assess the effectiveness of the candidate's response regarding {trait}.",
    "Determine the level of {trait} demonstrated in the given scenario.",
    "Review the candidate's approach to {trait} and its impact on the situation.",
    "Rate the candidate's ability to apply {trait} in this context.",
    "Provide an assessment of how well the candidate used {trait} to address the situation.",
    "Measure the candidate's response in relation to {trait} and its effectiveness.",
    "Judge the candidate's capability in demonstrating {trait} within this workplace challenge.",
    "Critique the depth of {trait} application in the candidate's response."
]

# Function to generate a single behavioral interview scenario
def generate_scenario():
    trait = random.choice(list(behavioral_traits.keys()))
    scenario = random.choice(behavioral_traits[trait])
    instruction = random.choice(instruction_templates).format(trait=trait)
    action = random.choice([
        "analyzing the issue carefully",
        "collaborating with my team to find solutions",
        "thinking creatively to overcome obstacles",
        "staying calm under pressure",
        "making data-driven decisions",
        "seeking guidance from mentors",
        "quickly adapting to the situation",
        "maintaining a positive and solution-focused mindset"
    ])
    result = random.choice([
        "a successful resolution of the challenge",
        "improved team collaboration and efficiency",
        "positive feedback from leadership",
        "increased project success and productivity",
        "a significant improvement in performance metrics"
    ])
    
    response = random.choice(candidate_responses).format(scenario=scenario, action=action, result=result, trait=trait)
    feedback = random.choice(evaluation_feedback).format(trait=trait)
    score = random.choice(scoring_range)

    return {
        "type": "cot_reasoning",
        "instruction": instruction,
        "input": f"Candidate's response: '{response}'",
        "output": feedback,
        "scoring": str(score)
    }

# Function to generate 30 sets of behavioral interview data, each with 10 turns
def generate_bulk_data(sets=30, turns=10):
    data = []
    for _ in range(sets):
        set_data = []
        for _ in range(turns):
            set_data.append(generate_scenario())
        data.append(set_data)
    return data

# Generate the dataset
data = generate_bulk_data(sets=30, turns=10)

# Save the generated dataset to a JSON file
output_file = "behavioral_assessment_scenarios.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Generated 20 sets of 10 behavioral interview scenarios and saved to {output_file}")
