import tkinter as tk
from tkinter import ttk
import webbrowser

class ParentWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Web Page Generator")

        # Label and entry for custom text
        self.label = ttk.Label(self, text="Enter custom text or click the Default HTML page button:")
        self.entry = ttk.Entry(self, width=30)
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        self.entry.grid(row=1, column=0, columnspan=2, pady=10)

        # Button to generate default HTML page
        self.default_btn = ttk.Button(self, text="Default HTML Page", command=self.generate_default_page)
        self.default_btn.grid(row=2, column=0, pady=10)

        # Button to generate HTML page with custom text
        self.custom_btn = ttk.Button(self, text="Submit Custom Text", command=self.generate_custom_page)
        self.custom_btn.grid(row=2, column=1, pady=10)

    def generate_default_page(self):
        text_content = "Stay tuned for our amazing summer sale!"
        self.generate_page(text_content)

    def generate_custom_page(self):
        text_content = self.entry.get()  # Get custom text from entry widget
        self.generate_page(text_content)

    def generate_page(self, text_content):
        if not text_content:
            # If custom text is empty, use default text
            text_content = "Stay tuned for our amazing summer sale!"

        # HTML content
        html_content = f"<!DOCTYPE html>\n<html>\n<head>\n<title>Summer Sale</title>\n</head>\n<body>\n<h1>{text_content}</h1>\n</body>\n</html>"

        # Save HTML content to a file
        with open("generated_page.html", "w") as file:
            file.write(html_content)

        # Open the generated HTML file in a new browser tab
        webbrowser.open_new_tab("generated_page.html")


if __name__ == "__main__":
    app = ParentWindow()
    app.mainloop()


    
