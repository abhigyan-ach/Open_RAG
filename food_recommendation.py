import openai

# OpenAI API key for GPT
openai.api_key = ENV_FILE

def generate_food_recommendation(activity_data):
    calories_burned = activity_data['data']['calories_burned']
    sleep_quality = activity_data['data']['sleep_quality']
    
    # Example prompt based on retrieved wearable data
    prompt = f"""
    I burned {calories_burned} calories today and had a sleep quality score of {sleep_quality}.
    Based on this, can you recommend healthy food options from the following:
    banana, chicken breast, salad, apple.
    """
    
    # Call GPT to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

# Example wearable data
activity_data = {
    'data': {
        'calories_burned': 500,
        'sleep_quality': 80
    }
}

# Get food recommendation
food_recommendation = generate_food_recommendation(activity_data)
print(food_recommendation)
