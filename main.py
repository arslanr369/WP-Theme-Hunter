import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_theme_name():
    # Get the URL from the text field
    url = url_entry.get()

    # Get the WordPress theme name
    theme_name = find_wordpress_theme(url)

    # If the theme name exists, display it in the result label
    if theme_name:
        result_label.config(text=f'The theme name is {theme_name}.')
    else:
        result_label.config(text='The WordPress theme name could not be detected.')

def find_wordpress_theme(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the WordPress theme name in the HTML
    theme_name = soup.find('link', attrs={'rel': 'stylesheet'}, href=lambda href: href and 'wp-content/themes' in href)

    # If the theme name exists, extract it and return
    if theme_name:
        theme_name = theme_name['href'].split('wp-content/themes/')[1].split('/')[0]
        return theme_name

    # If the theme name does not exist, return None
    return None

# Create the GUI
root = tk.Tk()
root.geometry('400x200')
root.title('WP Theme Detector by @ARSLANR369')

# Create the URL entry field
url_label = tk.Label(root, text='Enter URL:',font=('Arial', 10))
url_label.pack(side=tk.TOP, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(side=tk.TOP)

# Create the detect button
detect_button = tk.Button(root, text='Detect Theme', command=get_theme_name ,font=('Arial', 10))
detect_button.pack(side=tk.TOP, pady=10)

# Create the result label
result_label = tk.Label(root, text='',font=('Arial', 20))
result_label.pack(side=tk.TOP)

# Run the GUI
root.mainloop()
