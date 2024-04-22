import tkinter as tk
from tkinter import messagebox

# Fungsi untuk login
def login():
  username = entry_username.get()
  password = entry_password.get()

  # Cek apakah username dan password sudah terdaftar
  if username in users and users[username] == password:
    messagebox.showinfo("Login Berhasil", "Selamat Datang, " + username + "!")
  else:
    messagebox.showerror("Login Gagal", "username atau password invalid")

# Fungsi untuk menampilkan jendela registrasi
def show_register_window():
  register_window = tk.Toplevel(root)
  register_window.title("Registrasi")

  # Label dan Entry untuk username di jendela registrasi
  label_username = tk.Label(register_window, text="Username:")
  label_username.grid(row=0, column=0)
  entry_username = tk.Entry(register_window)
  entry_username.grid(row=0, column=1)

  # Label dan Entry untuk password di jendela registrasi
  label_password = tk.Label(register_window, text="Password:")
  label_password.grid(row=1, column=0)
  entry_password = tk.Entry(register_window, show="*")
  entry_password.grid(row=1, column=1)

  # Tombol untuk melakukan registrasi
  register_button = tk.Button(register_window, text="Register", command=lambda: register(entry_username.get(), entry_password.get()))
  register_button.grid(row=2, column=0, columnspan=2, pady=5)

# Fungsi untuk registrasi
def register(username, password):
  # Cek apakah username sudah terdaftar
  if username in users:
    messagebox.showerror("Registrasi Gagal", "Username sudah terpakai")
  else:
    # Tambahkan username dan password baru ke dictionary users
    users[username] = password
    messagebox.showinfo("Registrasi Berhasil", "Akun berhasil dibuat")
        

# Data pengguna (bisa disimpan di database)
users = {
  "ichsan": "122",
}

# Membuat jendela utama
root = tk.Tk()
root.title("Login")

# Label dan Entry untuk username
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Label dan Entry untuk password
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Tombol untuk login
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=5)

# Tombol untuk menampilkan jendela registrasi
register_button = tk.Button(root, text="Register", command=show_register_window)
register_button.grid(row=3, column=0, columnspan=2, pady=5)

# Menjalankan loop utama
root.mainloop()