from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PyQt6.QtCore import Qt


class TelaConfiguracoes(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configurações")
        self.resize(600, 400)

        self.criar_interface()

    def criar_interface(self):

        layout = QVBoxLayout()

        titulo = QLabel("Configurações")

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(titulo)

        mensagem = QLabel(
            "As configurações do sistema serão "
            "implementadas nesta tela."
        )

        mensagem.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(mensagem)

        self.setLayout(layout)