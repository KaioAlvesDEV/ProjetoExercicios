from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Define um tamanho de janela inicial
Window.size = (380, 500)

# A String KV define a aparência (o "CSS" do Kivy)
kv_style = """
<InterfaceCalculadora>:
    orientation: 'vertical'
    padding: 25
    spacing: 15
    canvas.before:
        Color:
            rgba: (0.1, 0.1, 0.12, 1)  # Fundo Escuro Moderno
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Aluguel de Carros"
        font_size: '28sp'
        bold: True
        color: (0, 0.7, 1, 1) # Azul Brilhante
        size_hint_y: None
        height: 80

    # Campo de Dias
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: 80
        Label:
            text: "Dias com o carro:"
            halign: 'left'
            text_size: self.size
        TextInput:
            id: dias_input
            hint_text: "Ex: 5"
            multiline: False
            input_filter: 'int'

    # Campo de KM
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: 80
        Label:
            text: "KM percorridos:"
            halign: 'left'
            text_size: self.size
        TextInput:
            id: km_input
            hint_text: "Ex: 150.5"
            multiline: False
            input_filter: 'float'

    # Botão de Calcular
    Button:
        text: "CALCULAR TOTAL"
        size_hint_y: None
        height: 60
        background_normal: ''
        background_color: (0, 0.7, 1, 1)
        color: (1, 1, 1, 1)
        bold: True
        on_release: root.calcular_aluguel()

    # Resultado
    Label:
        id: resultado_label
        text: "R$ 0,00"
        font_size: '40sp'
        bold: True
        color: (0.2, 0.8, 0.2, 1) # Verde
"""


class InterfaceCalculadora(BoxLayout):
    def calcular_aluguel(self):
        try:
            # Pegando os valores dos IDs definidos no KV
            dias = int(self.ids.dias_input.text)
            km = float(self.ids.km_input.text)

            # Sua lógica original
            total = (dias * 60) + (km * 0.15)

            # Atualizando o Label na tela
            self.ids.resultado_label.text = f"R$ {total:.2f}"
        except ValueError:
            self.ids.resultado_label.text = "Dados Inválidos"
            self.ids.resultado_label.color = (1, 0, 0, 1)


class CarroApp(App):
    def build(self):
        # Carrega a string KV
        Builder.load_string(kv_style)
        return InterfaceCalculadora()


if __name__ == '__main__':
    CarroApp().run()