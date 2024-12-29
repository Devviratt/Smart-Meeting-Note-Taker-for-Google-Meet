import re

def extract_action_items(transcript):
    # Basic logic to extract tasks or action items (you can refine it further)
    action_items = re.findall(r'\b(?:task|action|follow-up|due)\b.*', transcript, flags=re.IGNORECASE)
    return action_items

# Uncomment to test this function directly
# transcript = "Full transcript with action items like task, follow-up, etc."
# actions = extract_action_items(transcript)
# print("Action items:", actions)
