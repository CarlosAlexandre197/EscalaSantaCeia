from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFrame
)

from PyQt6.QtCore import Qt

from style import (
    COR_AZUL,
    COR_AZUL_ESCURO,
    COR_VERDE
)


class TelaConfiguracoes(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Configurações"
        )

        self.resize(
            700,
            500
        )

        self.criar_interface()

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(0)

        # ==================================================
        # BARRA AZUL SUPERIOR
        # ==================================================

        barra_superior = QFrame()

        barra_superior.setFixedHeight(
            65
        )

        barra_superior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_AZUL};
            }}
        """)

        layout_barra = QHBoxLayout()

        layout_barra.setContentsMargins(
            20,
            0,
            20,
            0
        )

        barra_superior.setLayout(
            layout_barra
        )

        titulo = QLabel(
            "CONFIGURAÇÕES"
        )

        titulo.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        layout_barra.addWidget(
            titulo
        )

        layout_barra.addStretch()

        sistema = QLabel(
            "Escala Santa Ceia"
        )

        sistema.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
            }
        """)

        layout_barra.addWidget(
            sistema
        )

        layout_principal.addWidget(
            barra_superior
        )

        # ==================================================
        # ÁREA CENTRAL
        # ==================================================

        area_central = QWidget()

        layout_central = QVBoxLayout()

        layout_central.setContentsMargins(
            40,
            30,
            40,
            30
        )

        layout_central.setSpacing(
            18
        )

        area_central.setLayout(
            layout_central
        )

        # ==================================================
        # TÍTULO
        # ==================================================

        titulo_config = QLabel(
            "Configurações do sistema"
        )

        titulo_config.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 20px;
                font-weight: bold;
            }}
        """)

        titulo_config.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_central.addWidget(
            titulo_config
        )

        # ==================================================
        # NOME DA IGREJA
        # ==================================================

        layout_igreja = QHBoxLayout()

        label_igreja = QLabel(
            "Nome da igreja:"
        )

        label_igreja.setMinimumWidth(
            150
        )

        self.input_igreja = QLineEdit()

        self.input_igreja.setPlaceholderText(
            "Digite o nome da igreja"
        )

        layout_igreja.addWidget(
            label_igreja
        )

        layout_igreja.addWidget(
            self.input_igreja
        )

        layout_central.addLayout(
            layout_igreja
        )

        # ==================================================
        # RESPONSÁVEL
        # ==================================================

        layout_responsavel = QHBoxLayout()

        label_responsavel = QLabel(
            "Responsável:"
        )

        label_responsavel.setMinimumWidth(
            150
        )

        self.input_responsavel = QLineEdit()

        self.input_responsavel.setPlaceholderText(
            "Digite o nome do responsável"
        )

        layout_responsavel.addWidget(
            label_responsavel
        )

        layout_responsavel.addWidget(
            self.input_responsavel
        )

        layout_central.addLayout(
            layout_responsavel
        )

        # ==================================================
        # BOTÃO SALVAR
        # ==================================================

        self.botao_salvar = QPushButton(
            "Salvar Configurações"
        )

        self.botao_salvar.setStyleSheet(f"""
            QPushButton {{
                background-color: {COR_AZUL};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px 20px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QPushButton:pressed {{
                background-color: {COR_VERDE};
            }}
        """)

        layout_central.addWidget(
            self.botao_salvar
        )

        layout_central.addStretch()

        layout_principal.addWidget(
            area_central
        )

        # ==================================================
        # BARRA VERDE INFERIOR
        # ==================================================

        barra_inferior = QFrame()

        barra_inferior.setFixedHeight(
            40
        )

        barra_inferior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_VERDE};
            }}
        """)

        layout_rodape = QHBoxLayout()

        layout_rodape.setContentsMargins(
            20,
            0,
            20,
            0
        )

        barra_inferior.setLayout(
            layout_rodape
        )

        rodape = QLabel(
            "Configurações do sistema"
        )

        rodape.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)

        layout_rodape.addWidget(
            rodape
        )

        layout_rodape.addStretch()

        versao = QLabel(
            "Versão 1.0"
        )

        versao.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)

        layout_rodape.addWidget(
            versao
        )

        layout_principal.addWidget(
            barra_inferior
        )

        self.setLayout(
            layout_principal
        )