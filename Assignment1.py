import os
from google import genai
from google.genai import types

client = genai.Client(api_key="API-KEY")
MODEL_ID = "gemini-2.5-flash-lite"

def generate_text_experiment(prompt, temp, top_p, max_tokens):
    config = types.GenerateContentConfig(
        temperature=temp,
        top_p=top_p,
        max_output_tokens=max_tokens
    )
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config
    )
    return response.text


tech_prompt = "Write a blog intro about why Rust is replacing C++ in systems programming."

product_prompt = """
Write a catchy product description for:
- Product: HydroFlask 3000
- Features: Solar charging, self-cleaning, weighs 200g
"""

story_prompt = "The last light in the universe flickered, and then there was a knock at the door."

print("---Tech Prompt---")
print(generate_text_experiment(tech_prompt, 0.1, 0.95, 100))
# print(generate_text_experiment(tech_prompt, 1.8, 0.95, 1000))
print("---Product Prompt---")
print(generate_text_experiment(product_prompt, 0.7, 0.6, 300))
print("---story Prompt---")
print(generate_text_experiment(story_prompt, 1, 0.3, 500))


