def story_prompt(theme):
    return f"""
Create a short children's story based on the theme '{theme}'.
Keep it engaging, simple, and suitable for ages 5–10.
Include 3–4 scenes.
"""

def illustration_prompt(story):
    return f"""
Based on the following story, generate 4 detailed illustration prompts 
for a children's book artist. Each prompt should describe the scene visually.

Story:
{story}
"""
