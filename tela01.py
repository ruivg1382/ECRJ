import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela=customtkinter.CTk()
janela.geometry("500x300")



def click():
    print("Login realizado com sucesso")


label=customtkinter.CTkLabel(janela,text="Utilizador:")
label.pack(padx=10,pady=5)

entrada=customtkinter.CTkEntry(janela, placeholder_text="Username")
entrada.pack(padx=10,pady=10)

label2=customtkinter.CTkLabel(janela,text="Password:")
label2.pack(padx=10,pady=5)

password=customtkinter.CTkEntry(janela,placeholder_text="Password",show="*")
password.pack(padx=10, pady=10)

checkbox=customtkinter.CTkCheckBox(janela,text="Lembrar password")
checkbox.pack(padx=10,pady=10)

button=customtkinter.CTkButton(janela, text="Login", command=click)
button.pack(padx=10, pady=10)






janela.mainloop()