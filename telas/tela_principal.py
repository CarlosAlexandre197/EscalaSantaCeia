from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame
)

from PyQt6.QtCore import Qt

from telas.cadastro_obreiros import TelaCadastroObreiros
from telas.montar_escala import TelaMontarEscala
from telas.visualizar_escala import TelaVisualizarEscala
from telas.configuracoes import TelaConfiguracoes

from style import (
    COR_AZUL,
    COR_AZUL_ESCURO,
    COR_VERDE,
    COR_VERDE_CLARO
)


class TelaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.tela_obreiros = None
        self.tela_escala = None
        self.tela_visualizar = None
        self.tela_configuracoes = None

        self.setWindowTitle(
            "Escala Santa Ceia"
        )

        self.resize(
            1000,
            650
        )

        self.criar_interface()

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        widget_central = QWidget()

        self.setCentralWidget(
            widget_central
        )

        layout_principal = QVBoxLayout()

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(0)

        widget_central.setLayout(
            layout_principal
        )

        # ==================================================
        # BARRA AZUL SUPERIOR
        # ==================================================

        barra_superior = QFrame()

        barra_superior.setFixedHeight(
            70
        )

        barra_superior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_AZUL};
            }}
        """)

        layout_barra_superior = QHBoxLayout()

        layout_barra_superior.setContentsMargins(
            25,
            0,
            25,
            0
        )

        barra_superior.setLayout(
            layout_barra_superior
        )

        titulo_barra = QLabel(
            "ESCALA SANTA CEIA"
        )

        titulo_barra.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)

        layout_barra_superior.addWidget(
            titulo_barra
        )

        layout_barra_superior.addStretch()

        subtitulo_barra = QLabel(
            "Sistema de Gerenciamento"
        )

        subtitulo_barra.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
            }
        """)

        layout_barra_superior.addWidget(
            subtitulo_barra
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
            35,
            40,
            35
        )

        layout_central.setSpacing(
            20
        )

        area_central.setLayout(
            layout_central
        )

        # --------------------------------------------------
        # TÍTULO
        # --------------------------------------------------

        titulo = QLabel(
            "Bem-vindo ao sistema"
        )

        titulo.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 26px;
                font-weight: bold;
            }}
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_central.addWidget(
            titulo
        )

        # --------------------------------------------------
        # SUBTÍTULO
        # --------------------------------------------------

        subtitulo = QLabel(
            "Selecione uma opção para continuar"
        )

        subtitulo.setStyleSheet("""
            QLabel {
                color: #555555;
                font-size: 16px;
            }
        """)

        subtitulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_central.addWidget(
            subtitulo
        )

        layout_central.addSpacing(
            20
        )

        # ==================================================
        # BOTÕES
        # ==================================================

        layout_linha_1 = QHBoxLayout()

        layout_linha_1.setSpacing(
            20
        )

        self.botao_obreiros = QPushButton(
            "Cadastro de Obreiros"
        )

        self.botao_escala = QPushButton(
            "Montar Escala"
        )

        self.botao_visualizar = QPushButton(
            "Visualizar Escala"
        )

        self.botao_configuracoes = QPushButton(
            "Configurações"
        )

        # --------------------------------------------------
        # CONEXÕES
        # --------------------------------------------------

        self.botao_obreiros.clicked.connect(
            self.abrir_obreiros
        )

        self.botao_escala.clicked.connect(
            self.abrir_escala
        )

        self.botao_visualizar.clicked.connect(
            self.abrir_visualizar
        )

        self.botao_configuracoes.clicked.connect(
            self.abrir_configuracoes
        )

        # --------------------------------------------------
        # ESTILO DOS BOTÕES
        # --------------------------------------------------

        estilo_botao = f"""
            QPushButton {{
                background-color: {COR_AZUL};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 18px;
                font-size: 15px;
                font-weight: bold;
                min-height: 55px;
            }}

            QPushButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QPushButton:pressed {{
                background-color: {COR_VERDE};
            }}
        """

        self.botao_obreiros.setStyleSheet(
            estilo_botao
        )

        self.botao_escala.setStyleSheet(
            estilo_botao
        )

        self.botao_visualizar.setStyleSheet(
            estilo_botao
        )

        self.botao_configuracoes.setStyleSheet(
            estilo_botao
        )

        layout_linha_1.addWidget(
            self.botao_obreiros
        )

        layout_linha_1.addWidget(
            self.botao_escala
        )

        layout_central.addLayout(
            layout_linha_1
        )

        layout_linha_2 = QHBoxLayout()

        layout_linha_2.setSpacing(
            20
        )

        layout_linha_2.addWidget(
            self.botao_visualizar
        )

        layout_linha_2.addWidget(
            self.botao_configuracoes
        )

        layout_central.addLayout(
            layout_linha_2
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
            45
        )

        barra_inferior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_VERDE};
            }}
        """)

        layout_barra_inferior = QHBoxLayout()

        layout_barra_inferior.setContentsMargins(
            20,
            0,
            20,
            0
        )

        barra_inferior.setLayout(
            layout_barra_inferior
        )

        rodape = QLabel(
            "Sistema de Escala Santa Ceia"
        )

        rodape.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
            }
        """)

        layout_barra_inferior.addWidget(
            rodape
        )

        layout_barra_inferior.addStretch()

        versao = QLabel(
            "Versão 1.0"
        )

        versao.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
            }
        """)

        layout_barra_inferior.addWidget(
            versao
        )

        layout_principal.addWidget(
            barra_inferior
        )

    # ==================================================
    # CADASTRO DE OBREIROS
    # ==================================================

    def abrir_obreiros(self):

        if self.tela_obreiros is None:

            self.tela_obreiros = TelaCadastroObreiros()

        self.tela_obreiros.show()
        self.tela_obreiros.raise_()
        self.tela_obreiros.activateWindow()

    # ==================================================
    # MONTAR ESCALA
    # ==================================================

    def abrir_escala(self):

        if self.tela_escala is None:

            self.tela_escala = TelaMontarEscala()

        self.tela_escala.show()
        self.tela_escala.raise_()
        self.tela_escala.activateWindow()

    # ==================================================
    # VISUALIZAR ESCALA
    # ==================================================

    def abrir_visualizar(self):

        if self.tela_visualizar is None:

            self.tela_visualizar = TelaVisualizarEscala()

        self.tela_visualizar.show()
        self.tela_visualizar.raise_()
        self.tela_visualizar.activateWindow()

    # ==================================================
    # CONFIGURAÇÕES
    # ==================================================

    def abrir_configuracoes(self):

        if self.tela_configuracoes is None:

            self.tela_configuracoes = TelaConfiguracoes()

        self.tela_configuracoes.show()
        self.tela_configuracoes.raise_()
        self.tela_configuracoes.activateWindow()