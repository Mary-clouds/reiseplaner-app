import streamlit as st
import requests
from rich.console import Console

console = Console()

# Display a welcome message using rich
def welcome_message():
    console.print("\n\n[bold yellow]Welcome to the AI Travel Itinerary Planner[/bold yellow]\n")

# Credit message
def credit_message():
    console.print("\n\n[bold yellow]This app was built by Nevermann with ❤️[/bold yellow]")
    console.print("[yellow]Thank you for using it! 🙏[/yellow]")

# Display current weather using API
def display_current_weather(location):
    api_weather_key = "1b3cfb66ad014a3fo55df2e890f445t9"
    api_weather_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_weather_key}&units=metric"

    response = requests.get(api_weather_url)
    response_data = response.json()

    temperature = round(response_data['temperature']['current'])
    condition = response_data['condition']['description']
    console.print(f"\nThe current temperature in [bold]{location.capitalize()}[/bold] is [bold]{temperature}°C[/bold], {condition}")

# Generate travel itinerary using AI API
def generate_itinerary(origin, destination, duration):
    prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. Keep it short, max 15 well-formatted lines, with emojis, estimated prices and daily weather in euros."
    context = "You are a travel expert and know the best tourist spots around the world"
    api_key = "1b3cfb66ad014a3fo55df2e890f445t9"
    api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

    response = requests.get(api_url, timeout=10)
    response_data = response.json()

    # Display in Streamlit
    st.markdown(response_data['answer'])

# Streamlit UI
st.title("🧳 AI Travel Itinerary Planner")
welcome_message()

origin = st.text_input("✈️ Where are you travelling from?")
destination = st.text_input("📍 What is your destination?")
duration = st.number_input("🗓️ How many days is your trip?", min_value=1, max_value=30, value=3)

if st.button("Generate Itinerary"):
    if origin and destination and duration:
        display_current_weather(origin)
        display_current_weather(destination)
        generate_itinerary(origin, destination, duration)
        credit_message()
    else:
        st.error("❗ Please enter all required information.")
