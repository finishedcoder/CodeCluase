import tkinter as tk
import smtplib
from tkinter import Text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import ImageTk, Image

class MailApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Mail Application")

        # Set background image
        self.bg_image = Image.open('mail_images.png')
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        bg_label = tk.Label(self.master, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create labels and input fields
        self.to_label = tk.Label(self.master, text="To:", font=("Arial", 14), bg='red', fg='white')
        self.to_label.grid(row=0, column=0, padx=20, pady=10)
        self.to_entry = tk.Entry(self.master, width=50, font=("Arial", 14))
        self.to_entry.grid(row=0, column=1, padx=20, pady=10)

        self.subject_label = tk.Label(self.master, text="Subject:", font=("Arial", 14), bg='red', fg='white')
        self.subject_label.grid(row=1, column=0, padx=20, pady=10)
        self.subject_entry = tk.Entry(self.master, width=50, font=("Arial", 14))
        self.subject_entry.grid(row=1, column=1, padx=20, pady=10)

        self.message_label = tk.Label(self.master, text="Message:", font=("Arial", 14), bg='red', fg='white')
        self.message_label.grid(row=2, column=0, padx=20, pady=10)
        self.message_text = Text(self.master, height=10, width=50, font=("Arial", 12))
        self.message_text.grid(row=2, column=1, padx=20, pady=10)

        # Create send button
        self.send_button = tk.Button(self.master, text="Send", command=self.send_email, font=("Arial", 14), bg='red', fg='white')
        self.send_button.grid(row=3, column=1, padx=20, pady=10)

    def send_email(self):
        # Get values from input fields
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end")

        # Set up email message
        msg = MIMEMultipart()
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send email
        smtp_server = 'smtp.gmail.com' 
        smtp_username = '01sampletesting@gmail.com' # Replace with your SMTP username
        smtp_password = 'pklnydnqkntgsknu' # Replace with your SMTP password
        smtp_connection = smtplib.SMTP(smtp_server)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(smtp_username, to_address, msg.as_string())
        smtp_connection.quit()

        # Clear input fields
        self.to_entry.delete(0, "end")
        self.subject_entry.delete(0, "end")
        self.message_text.delete("1.0", "end")


mail_win = tk.Tk()
app = MailApplication(mail_win)
mail_win.geometry('800x600')
mail_win.configure(bg='white')
mail_win.iconbitmap('emails-concept.ico')
mail_win.resizable(False, False)

mail_win.mainloop()