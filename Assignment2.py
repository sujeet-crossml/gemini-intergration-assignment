from google import genai
from google.genai import types
import PIL.Image


client = genai.Client(api_key="AIzaSyDkmUBKbEuBoENeEvmlTb4SrK-mJZ8YzKQ")
model_id = "gemini-3-flash-preview" 

img_room = PIL.Image.open('room.png')
img_diagram = PIL.Image.open('flowchart.png')
img_food = PIL.Image.open('food.png')
prompt = "Style: Cyberpunk-Boho. Suggest 3 furniture changes."
prompt2="Explain step 3 of this process in one sentence."
prompt3 ="I am Vegan. Create a fusion dinner recipe from these."

def text_generation(image, prompt, temp, top_p, top_k):
    config= types.GenerateContentConfig(
    temperature=temp,  
    top_p=top_p,       
    top_k=top_k          
    )
    response = client.models.generate_content(
    model=model_id,
    contents=[image, prompt],
    config=config
    )
    print(f"Design Suggestions:\n{response.text}\n\n")

# High Temp for "Creative Sparks"
text_generation(img_room,prompt, 0.9, 0.95, 50)
# Low Temp for "Factual Precision"
text_generation(img_diagram,prompt2, 0.1, 0.4, 20)
# Balanced for "Practical Innovation" 
text_generation(img_food,prompt3, 0.6, 0.8, 40)




# config_design = types.GenerateContentConfig(
#     temperature=0.9,  
#     top_p=0.95,       
#     top_k=50          
# )

# config_tech = types.GenerateContentConfig(
#     temperature=0.1,  
#     top_p=0.4,        
#     top_k=20   )      

# config_recipe = types.GenerateContentConfig(
#     temperature=0.6,  
#     top_p=0.8,        
#     top_k=40         )
 
# response = client.models.generate_content(
#     model=model_id,
#     contents=[img_diagram, "Explain step 3 of this process in one sentence."],
#     config=config_tech
# )
# print(f"Technical Analysis:\n{response.text}")

# response = client.models.generate_content(
#     model=model_id,
#     contents=[img_food, "I am Vegan. Create a fusion dinner recipe from these."],
#     config=config_recipe
# )
# print(f"Fusion Recipe:\n{response.text}")