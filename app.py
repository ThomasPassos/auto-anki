import customtkinter as ctk

from connector import DictionaryConnector

# Inicialização do app
app = ctk.CTk()
connector = DictionaryConnector()

# Botões
button_save_words = ctk.CTkButton(app, text="GUARDAR")
button_begin_cards = ctk.CTkButton(app, text="CRIAR CARDS")
button_word_list = ctk.CTkButton(app, text="PALAVRAS GUARDADAS")

# Posicionamento dos botões
button_save_words.pack()
button_begin_cards.pack()
button_word_list.pack()

app.mainloop()