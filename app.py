from prompts import story_prompt, illustration_prompt
from openai import OpenAI

client = OpenAI()

def generate_story(theme):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": story_prompt(theme)}]
    )
    return response.choices[0].message.content

def generate_illustrations(story):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": illustration_prompt(story)}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    theme = input("Enter a theme (e.g., friendship, jungle, space): ")
    story = generate_story(theme)
    
    print("\n--- STORY ---\n")
    print(story)

    illustrations = generate_illustrations(story)
    
    print("\n--- ILLUSTRATION PROMPTS ---\n")
    print(illustrations)
