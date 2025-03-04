import tkinter as tk
import random

def move_button(event):
    """Move the 'No' button when the cursor gets close to it"""
    # Get window dimensions
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # Safety check - if window isn't fully initialized yet
    if window_width < 100 or window_height < 100:
        window_width = 400
        window_height = 300
    
    # Button dimensions
    button_width = no_button.winfo_width()
    button_height = no_button.winfo_height()
    
    # Ensure minimum button size
    if button_width < 30:
        button_width = 80
    if button_height < 10:
        button_height = 30
    
    # Safe margin to keep button fully visible
    margin = 20
    
    # Calculate maximum coordinates to ensure button stays visible
    max_x = max(50, window_width - button_width - margin)
    max_y = max(50, window_height - button_height - margin)
    
    # Generate new random coordinates
    new_x = random.randint(margin, max_x)
    new_y = random.randint(margin, max_y)
    
    # Place the button at the new coordinates, relative to the window
    no_button.place(x=new_x, y=new_y)

def on_yes_click():
    """Close the window when 'Yes' is clicked"""
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Question")
root.geometry("400x300")
root.resizable(False, False)

# Make sure the window has size before button placement
root.update()

# Create the question label
label = tk.Label(root, text="Are you Dumb?", font=("Arial", 20))
label.pack(pady=30)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="both", expand=True)

# Create the 'Yes' button
yes_button = tk.Button(button_frame, text="Yes", font=("Arial", 14), command=on_yes_click)
yes_button.place(x=100, y=100)

# Create the 'No' button
no_button = tk.Button(root, text="No", font=("Arial", 14))
no_button.place(x=240, y=100)

# Bind the motion event to the 'No' button
no_button.bind("<Enter>", move_button)

# Run the application
root.mainloop() 