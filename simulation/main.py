from tkinter import *
import random
import time
import threading
from queue import Queue
from validation import (is_float, is_int, servers_validation)
from tkinter import messagebox
from customer import Customer
import numpy as np

class BankSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Queue Simulation")
        self.master.geometry("400x400")

        self.lambda_input = Entry(master, width=50, borderwidth=5)
        self.lambda_input.pack(pady=10)

        self.mu_input = Entry(master, width=50, borderwidth=5)
        self.mu_input.pack(pady=10)

        self.servers_input = Entry(master, width=50, borderwidth=5)
        self.servers_input.pack(pady=10)

        self.submit_button = Button(master, text="Submit", command=self.start_simulation)
        self.submit_button.pack(pady=20)


        self.stop_button = Button(master, text="Stop", command=self.stop_simulation)
        self.stop_button.pack(pady=10)

        self.status_label = Label(master, text="Status: Stopped")
        self.status_label.pack(pady=10)

        self.cashiers = [None] * 6  # None means cashier is free
        self.customer_queue = Queue()
        self.running = False

    def start_simulation(self):

        lambda_value = self.lambda_input.get()
        mu_value = self.mu_input.get()
        servers_value = self.servers_input.get()

        if not is_float(lambda_value):
            messagebox.showerror("Input Error", "Lambda must be a valid float.")
            return
        if not is_float(mu_value):
            messagebox.showerror("Input Error", "Mu must be a valid float.")
            return
        if not is_int(servers_value):
            messagebox.showerror("Input Error", "Servers must be a valid int.")
            return
    
        if not servers_validation(int(servers_value)):
            messagebox.showerror("Input Error", "Servers must be less than or equal to 6.")
            return

        self.running = True
        self.status_label.config(text="Status: Running")
        self.simulate_customers()
        self.process_customers()

    def stop_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Stopped")

    def simulate_customers(self):
        def customer_generator():
            while self.running:
                customer = Customer(float(self.lambda_input.get()))
                self.customer_queue.put(customer)
                print(f"Customer {customer.id} arrived.")
                time.sleep(customer.arrival_time)  # New customer every 1 to 3 seconds

        threading.Thread(target=customer_generator, daemon=True).start()

    def process_customers(self):
        def cashier_worker(cashier_id):
            while self.running:
                if not self.customer_queue.empty():
                    customer = self.customer_queue.get()
                    service_time = np.random.exponential(float(self.mu_input.get()))  # Random service time between 2 to 5 seconds
                    print(f"Cashier {cashier_id} is serving Customer {customer.id} for {service_time:.2f} seconds.")
                    time.sleep(service_time)
                    print(f"Cashier {cashier_id} finished serving Customer {customer.id}.")
                else:
                    time.sleep(1)  # Wait for customers

        for i in range(int(self.servers_input.get())):
            threading.Thread(target=cashier_worker, args=(i + 1,), daemon=True).start()

if __name__ == "__main__":
    root = Tk()
    app = BankSimulation(root)
    root.mainloop()