import tkinter as tk

class Lamp:
    def __init__(self):
        # Cria a janela principal
        self.window = tk.Tk()
        self.window.title("Lâmpada")
        
        # Cria os botões de ligar e desligar
        self.button_on = tk.Button(self.window, text="Ligar", command=self.turn_on)
        self.button_off = tk.Button(self.window, text="Desligar", command=self.turn_off)
        
        # Posiciona os botões na tela
        self.button_on.pack(side=tk.LEFT)
        self.button_off.pack(side=tk.RIGHT)
        
        # Cria a imagem da lâmpada
        self.image = tk.Label(self.window)
        self.image.pack()
        
        # Carrega as imagens da lâmpada ligada e desligada
        self.image_on = tk.PhotoImage(file="lamp_on.png")
        self.image_off = tk.PhotoImage(file="lamp_off.png")
        
        # Inicialmente, a lâmpada está desligada
        self.is_on = False
        self.update_image()
        
        # Inicia o loop de eventos
        self.window.mainloop()
    
    def turn_on(self):
        self.is_on = True
        self.update_image()
    
    def turn_off(self):
        self.is_on = False
        self.update_image()
    
    def update_image(self):
        if self.is_on:
            self.image.config(image=self.image_on)
        else:
            self.image.config(image=self.image_off)

# Cria a lâmpada
lamp = Lamp()
