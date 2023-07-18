import customtkinter as ctk

# Configurações da janela:
app = ctk.CTk()
app.title("Auto Anki")
app.geometry("800x700")

# Botões:
button_send_words = ctk.CTkButton(app, text="guardar") 
button_main_function =  ctk.CTkButton(app, text="mineiração")
button_view_list =  ctk.CTkButton(app, text="lista de palavras")





app.mainloop()