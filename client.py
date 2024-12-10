import socket, threading, tkinter as tk
from tkinter import scrolledtext

hostname, port = ("singhrasp.ddnsgeek.com", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
window = tk.Tk()
window.geometry("500x510")
window.title("Client")
window.resizable(False, False)

# scroll view
chat = scrolledtext.ScrolledText(window, width=150, height=20)
chat.config(state="disabled")

# allow multiple messages to send 
def recieve():
    msg = ""
    while True:
        try:
            msg = s.recv(1024).decode()
            if not msg:
                print("Server disconnected")
                insert_text("Server disconnected")
                break
            else:
                print(f"Server: {msg}")
                # print("Enter a message to send: ")
                insert_text(f"Server: {msg}")
        except Exception as e:
            print("Error: ", e)
            insert_text(f"Error: {e}")
            break


def send():
    input_msg = input_text_box.get("1.0", tk.END).strip() 
    try:
        insert_text(f"You: {input_msg}")
        # erase the textbox message
        input_text_box.delete("1.0", tk.END)
        # send the message
        s.send(input_msg.encode())
    except Exception as e:
        print("Error ", e)
        insert_text(f"Error: {e}")

# get the value of text box
def get_text():
    # get the message
    input_msg = input_text_box.get("1.0", tk.END).strip()
    insert_text(f"You: {input_msg}")
    # erase the textbox message
    input_text_box.delete("1.0", tk.END)
    return input_msg

def insert_text(text):
    # insert message to the scroll text box
    chat.config(state="normal")
    chat.insert(tk.END, f"{text}\n")
    chat.config(state="disabled")


label = tk.Label(window, text="Enter a message to send: ")
label.place(x=0, y=430)


# writing text box 
input_text_box = tk.Text(window, height=2, width=60)
input_text_box.focus()
input_text_box.place(x=0, y=450)
# enter key event
input_text_box.bind("<Return>", lambda event: send())

send_button = tk.Button(window, text="Send", command=send, height=2)
send_button.place(x=450, y=450)

exit_button = tk.Button(window, text="Exit", command=lambda: {
    s.send("quit".encode()),
    window.destroy(),
    s.close()
}, height=2)
exit_button.place(x=450, y=0)


chat.pack()


# "singhrasp.ddnsgeek.com"
# connect to public ip like singhrasp.ddnsgeek.com and give port number
try:
    s.connect((hostname, port))
    insert_text(f"Hosting on address and socket {s.getsockname()}")
    insert_text(f"Client host name {socket.gethostname()}")
except Exception as e:
    print("Error: ", e)
    insert_text(f"Error: {e}")


thread_reciever = threading.Thread(target=recieve, daemon=True)
thread_reciever.start()
window.mainloop()

# close the connection
s.close()
