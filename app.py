import streamlit as st
import requests
from rich import print
from rich.markdown import Markdown

st.title("ReisePlanner App")
st.write("Hallo! Das ist eine einfache Web-App.")

#Display the destination weather
def display_current_weather(location):
  """Get te current temperature und condition in the a location"""
  api_weather_key ="1b3cfb66ad014a3fo55df2e890f445t9"
  api_weather_url =f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_weather_key}&units=metric"

  response = requests.get(api_weather_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']
  print(f"\n\nThe current temperature in [bold]{location.capitalize()}[/bold] is [bold]{temperature}°C[/bold], {condition}\n")

#Display the itinerary
def generate_itinerary(origin, destination, duration):
  """Generate a travel itineray between 2 places using AI"""
  print(f"\nCalculating itineraries from {origin} to {destination}..\n")
  #prompt
  prompt = f"Generate a travel itinary from {origin} to {destination} in {duration} days. Tis is a road, keep it short, less than 15 well formated lines. add some emojis. Add an estimated price and weather condition of each day in euros."
  #context
  context = "You are a travel expert and know te best tourist spots around the world"
  #api key
  api_key = "1b3cfb66ad014a3fo55df2e890f445t9"
  #api url
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"
  #call the api
  response = requests.get(api_url)
  response_data = response.json()
  itinerary = Markdown(response_data['answer'])
  #print the result/ display the itinerary
  print(itinerary)

#Display a welcome message
def welcome_message():
  """welcome message"""
  print("\n\n[bold yellow]Welcome to the AI Travel itinerary planner[/bold yellow]\n\n")

def credit_message():
  """credit message"""
  message_one= "\n\n\nThis Ai Travel itinerary planner was coded by [bold yellow]Nevermann[/bold yellow] with ❤️"
  message_two = "                   [yellow]Thank you for using it!🙏[/yellow]"
  print( message_one )
  print(message_two)

welcome_message()

#Get some user input
origin = input("Where are you travelling from? ")
destination = input("What is your trip destination? ")
duration = input("How many days will your trip last? (enter a number only i.e 3)")

if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit_message()
else:
  print("Invalid input. please try again! ")


