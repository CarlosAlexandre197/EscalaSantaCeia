from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox
)

from telas.cadastro_obreiros import TelaCadastroObreiros
from telas.montar_escala import TelaMontarEscala
from telas.visualizar_escala import TelaVisualizarEscala
from telas.configuracoes import TelaConfiguracoes


class TelaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.tela_obreiros = None
        self.tela_escala = None
        self.tela_visualizar = None
        self.tela_configuracoes = None
        self.setWindowTitle("Escala Santa Ceia")
        self.resize(1000, 650)

        self.criar_interface()

    def criar_interface(self):

        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        # =========================
        # TÍTULO
        # =========================

        titulo = QLabel("ESCALA SANTA CEIA")

        titulo.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                padding: 20px;
            }
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(titulo)

        # =========================
        # SUBTÍTULO
        # =========================

        subtitulo = QLabel(
            "Sistema de gerenciamento da escala mensal"
        )

        subtitulo.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding-bottom: 20px;
            }
        """)

        subtitulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(subtitulo)

        # =========================
        # BOTÕES
        # =========================

        layout_botoes = QHBoxLayout()

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

        layout_botoes.addWidget(
            self.botao_obreiros
        )

        layout_botoes.addWidget(
            self.botao_escala
        )

        layout_botoes.addWidget(
            self.botao_visualizar
        )

        layout_botoes.addWidget(
            self.botao_configuracoes
        )

        layout_principal.addLayout(
            layout_botoes
        )

        layout_principal.addStretch()

        # =========================
        # RODAPÉ
        # =========================

        rodape = QLabel(
            "Sistema de Escala Santa Ceia"
        )

        rodape.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(
            rodape
        )

    # =========================
    # CADASTRO DE OBREIROS
    # =========================

    def abrir_obreiros(self):

        if self.tela_obreiros is None:

            self.tela_obreiros = TelaCadastroObreiros()

        self.tela_obreiros.show()
        self.tela_obreiros.raise_()
        self.tela_obreiros.activateWindow()

    # =========================
    # BOTÕES AINDA NÃO IMPLEMENTADOS
    # =========================

    def em_desenvolvimento(self):

        QMessageBox.information(
            self,
            "Em desenvolvimento",
            "Esta função será implementada nas próximas etapas."
        )
        
    def abrir_escala(self):

        if self.tela_escala is None:

            self.tela_escala = TelaMontarEscala()

        self.tela_escala.show()
        self.tela_escala.raise_()
        self.tela_escala.activateWindow()
        
    def abrir_visualizar(self):

        if self.tela_visualizar is None:

            self.tela_visualizar = TelaVisualizarEscala()

        self.tela_visualizar.show()
        self.tela_visualizar.raise_()
        self.tela_visualizar.activateWindow()
        
    def abrir_configuracoes(self):

        if self.tela_configuracoes is None:

            self.tela_configuracoes = TelaConfiguracoes()

        self.tela_configuracoes.show()
        self.tela_configuracoes.raise_()
        self.tela_configuracoes.activateWindow()