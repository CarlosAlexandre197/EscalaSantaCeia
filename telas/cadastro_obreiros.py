from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
    QFrame
)

from PyQt6.QtCore import Qt

from database import Banco

from style import (
    COR_AZUL,
    COR_AZUL_ESCURO,
    COR_VERDE
)


class TelaCadastroObreiros(QWidget):

    def __init__(self):
        super().__init__()

        self.banco = Banco()

        self.setWindowTitle(
            "Cadastro de Obreiros"
        )

        self.resize(
            800,
            600
        )

        self.criar_interface()
        self.carregar_obreiros()

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
        # BARRA AZUL
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

        titulo_barra = QLabel(
            "CADASTRO DE OBREIROS"
        )

        titulo_barra.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        layout_barra.addWidget(
            titulo_barra
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
            30,
            25,
            30,
            25
        )

        layout_central.setSpacing(
            15
        )

        area_central.setLayout(
            layout_central
        )

        # ==================================================
        # CAMPOS
        # ==================================================

        layout_nome = QHBoxLayout()

        label_nome = QLabel(
            "Nome:"
        )

        label_nome.setMinimumWidth(
            80
        )

        self.input_nome = QLineEdit()

        self.input_nome.setPlaceholderText(
            "Digite o nome do obreiro"
        )

        layout_nome.addWidget(
            label_nome
        )

        layout_nome.addWidget(
            self.input_nome
        )

        layout_central.addLayout(
            layout_nome
        )

        # --------------------------------------------------
        # TELEFONE
        # --------------------------------------------------

        layout_telefone = QHBoxLayout()

        label_telefone = QLabel(
            "Telefone:"
        )

        label_telefone.setMinimumWidth(
            80
        )

        self.input_telefone = QLineEdit()

        self.input_telefone.setPlaceholderText(
            "Digite o telefone"
        )

        layout_telefone.addWidget(
            label_telefone
        )

        layout_telefone.addWidget(
            self.input_telefone
        )

        layout_central.addLayout(
            layout_telefone
        )

        # ==================================================
        # BOTÕES
        # ==================================================

        layout_botoes = QHBoxLayout()

        layout_botoes.setSpacing(
            10
        )

        self.botao_adicionar = QPushButton(
            "Adicionar"
        )

        self.botao_editar = QPushButton(
            "Editar"
        )

        self.botao_desativar = QPushButton(
            "Desativar"
        )

        self.botao_limpar = QPushButton(
            "Limpar"
        )

        self.botao_adicionar.clicked.connect(
            self.adicionar_obreiro
        )

        self.botao_editar.clicked.connect(
            self.editar_obreiro
        )

        self.botao_desativar.clicked.connect(
            self.desativar_obreiro
        )

        self.botao_limpar.clicked.connect(
            self.limpar_campos
        )

        # --------------------------------------------------
        # ESTILO DOS BOTÕES
        # --------------------------------------------------

        estilo_botao = f"""
            QPushButton {{
                background-color: {COR_AZUL};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 18px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QPushButton:pressed {{
                background-color: {COR_VERDE};
            }}
        """

        self.botao_adicionar.setStyleSheet(
            estilo_botao
        )

        self.botao_editar.setStyleSheet(
            estilo_botao
        )

        self.botao_desativar.setStyleSheet(
            estilo_botao
        )

        self.botao_limpar.setStyleSheet(
            estilo_botao
        )

        layout_botoes.addWidget(
            self.botao_adicionar
        )

        layout_botoes.addWidget(
            self.botao_editar
        )

        layout_botoes.addWidget(
            self.botao_desativar
        )

        layout_botoes.addWidget(
            self.botao_limpar
        )

        layout_central.addLayout(
            layout_botoes
        )

        # ==================================================
        # TABELA
        # ==================================================

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(
            3
        )

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "Telefone"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabela.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.tabela.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.tabela.cellClicked.connect(
            self.selecionar_obreiro
        )

        layout_central.addWidget(
            self.tabela
        )

        layout_principal.addWidget(
            area_central
        )

        # ==================================================
        # BARRA VERDE
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
            "Cadastro e gerenciamento de obreiros"
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

        sistema = QLabel(
            "Escala Santa Ceia"
        )

        sistema.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)

        layout_rodape.addWidget(
            sistema
        )

        layout_principal.addWidget(
            barra_inferior
        )

        self.setLayout(
            layout_principal
        )

    # ==================================================
    # CARREGAR OBREIROS
    # ==================================================

    def carregar_obreiros(self):

        obreiros = self.banco.listar_obreiros()

        self.tabela.setRowCount(
            0
        )

        for obreiro in obreiros:

            linha = self.tabela.rowCount()

            self.tabela.insertRow(
                linha
            )

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    str(obreiro["id"])
                )
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    obreiro["nome"]
                )
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(
                    obreiro["telefone"] or ""
                )
            )

    # ==================================================
    # ADICIONAR
    # ==================================================

    def adicionar_obreiro(self):

        nome = (
            self.input_nome
            .text()
            .strip()
        )

        telefone = (
            self.input_telefone
            .text()
            .strip()
        )

        if not nome:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do obreiro."
            )

            return

        self.banco.adicionar_obreiro(
            nome,
            telefone
        )

        QMessageBox.information(
            self,
            "Sucesso",
            "Obreiro cadastrado com sucesso!"
        )

        self.limpar_campos()

        self.carregar_obreiros()

    # ==================================================
    # SELECIONAR
    # ==================================================

    def selecionar_obreiro(
        self,
        linha,
        coluna
    ):

        id_obreiro = int(
            self.tabela
            .item(linha, 0)
            .text()
        )

        obreiro = (
            self.banco.buscar_obreiro(
                id_obreiro
            )
        )

        if obreiro:

            self.input_nome.setText(
                obreiro["nome"]
            )

            self.input_telefone.setText(
                obreiro["telefone"] or ""
            )

    # ==================================================
    # EDITAR
    # ==================================================

    def editar_obreiro(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        id_obreiro = int(
            self.tabela
            .item(linha, 0)
            .text()
        )

        nome = (
            self.input_nome
            .text()
            .strip()
        )

        telefone = (
            self.input_telefone
            .text()
            .strip()
        )

        if not nome:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do obreiro."
            )

            return

        self.banco.atualizar_obreiro(
            id_obreiro,
            nome,
            telefone
        )

        QMessageBox.information(
            self,
            "Sucesso",
            "Obreiro atualizado com sucesso!"
        )

        self.limpar_campos()

        self.carregar_obreiros()

    # ==================================================
    # DESATIVAR
    # ==================================================

    def desativar_obreiro(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        id_obreiro = int(
            self.tabela
            .item(linha, 0)
            .text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar",
            "Deseja desativar este obreiro?"
        )

        if resposta == (
            QMessageBox.StandardButton.Yes
        ):

            self.banco.desativar_obreiro(
                id_obreiro
            )

            self.limpar_campos()

            self.carregar_obreiros()

    # ==================================================
    # LIMPAR
    # ==================================================

    def limpar_campos(self):

        self.input_nome.clear()

        self.input_telefone.clear()

        self.tabela.clearSelection()

    # ==================================================
    # FECHAR
    # ==================================================

    def closeEvent(
        self,
        event
    ):

        self.banco.fechar()

        event.accept()