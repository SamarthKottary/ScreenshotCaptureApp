import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab

def take_screenshot():
    root.withdraw()  # Hide the main window
    screenshot = ImageGrab.grab()  # Capture screenshot
    root.deiconify()  # Show the main window again

    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All Files", "*.*")])
    if file_path:
        screenshot.save(file_path)
        print(f"Screenshot saved at: {file_path}")

# Create the GUI window
root = tk.Tk()
root.title("Screenshot Capture App")
root.geometry("300x200")

# Add a button
btn_screenshot = tk.Button(root, text="Take Screenshot", command=take_screenshot)
btn_screenshot.pack(expand=True)

# Run the app
root.mainloop()
