# __borko__
"""Check port is open or not in ip location"""

# Import modules
import socket
import tkinter as tk
from tkinter import ttk
from threading import Thread


def check_open_or_not(host, port):
    """Create socket with timeout 0.2s
    Try to connect with host by port if
    ok (0) result is write in L_BOX field"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    try:
        result = s.connect_ex((host, port))
    except socket.error as er:
        print(f"Gain Error, {er}")
    else:
        if result == 0:
            L_BOX.insert(
                tk.END, f'[+{port}] on host {host} looked to be open'
            )


def run_test():
    check_port = E_PORT.get().split(",")
    host = E_IP.get()
    for port in check_port:
        check_open_or_not(host, int(port))


# Graphical
root = tk.Tk()
root.title("Check open port on target mashine")
root.geometry("400x500+200+100")
root.resizable(False, False)

# Configura panel
pane = ttk.PanedWindow(root, orient=tk.VERTICAL)

pane_top = ttk.Frame(pane, relief=tk.RAISED)
pane_bottom = ttk.Frame(pane, relief=tk.RAISED)

pane_top.pack()
pane_bottom.pack()

pane.add(pane_top)
pane.add(pane_bottom)

pane.pack(fill=tk.BOTH, expand=1)

# Enter mashine ip and port
L_IP = ttk.Label(pane_top, text="Enter host")
E_IP = tk.Entry(pane_top, width=30)
E_IP.columnconfigure(0, weight=1)
L_IP.grid(row=0, column=0, sticky='nw')
E_IP.grid(row=0, column=1, sticky='we', padx=5)
E_IP.focus()

L_PORT = ttk.Label(pane_top, text="Enter ports")
E_PORT = tk.Entry(pane_top, width=30)
E_PORT.columnconfigure(0, weight=1)
L_PORT.grid(row=1, column=0, sticky='nw')
E_PORT.grid(row=1, column=1, sticky='we', padx=3)

B = tk.Button(pane_top, text="Check", command=run_test)
B.grid(row=0, column=2, rowspan=2, sticky="we")

# Configure result pane
S = tk.Scrollbar(pane_bottom)
S.pack(side=tk.RIGHT, fill=tk.Y)
L_BOX = tk.Listbox(pane_bottom, yscrollcommand=S.set)
L_BOX.pack(fill=tk.BOTH, expand=1)
S.config(command=L_BOX.yview)


if __name__ == '__main__':
    root.mainloop()