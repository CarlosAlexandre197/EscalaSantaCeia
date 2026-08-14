from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QDateEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)

from PyQt6.QtCore import QDate

from database import Banco


class TelaMontarEscala(QWidget):

    def __init__(self):
        super().__init__()

        self.banco = Banco()

        self.setWindowTitle("Montar Escala - Santa Ceia")
        self.resize(800, 600)

        self.criar_interface()
        self.carregar_obreiros()
        self.carregar_escalas()

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        # =========================
        # TÍTULO
        # =========================

        titulo = QLabel("Montar Escala da Santa Ceia")

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        layout_principal.addWidget(titulo)

        # =========================
        # DATA
        # =========================

        layout_data = QHBoxLayout()

        label_data = QLabel("Data da Santa Ceia:")

        self.data_santa_ceia = QDateEdit()

        self.data_santa_ceia.setCalendarPopup(True)

        self.data_santa_ceia.setDate(
            QDate.currentDate()
        )

        layout_data.addWidget(label_data)
        layout_data.addWidget(self.data_santa_ceia)

        layout_principal.addLayout(layout_data)

        # =========================
        # OBREIRO
        # =========================

        layout_obreiro = QHBoxLayout()

        label_obreiro = QLabel("Obreiro:")

        self.combo_obreiro = QComboBox()

        layout_obreiro.addWidget(label_obreiro)
        layout_obreiro.addWidget(self.combo_obreiro)

        layout_principal.addLayout(layout_obreiro)

        # =========================
        # BOTÃO ADICIONAR
        # =========================

        self.botao_adicionar = QPushButton(
            "Adicionar à Escala"
        )

        self.botao_adicionar.clicked.connect(
            self.adicionar_escala
        )

        layout_principal.addWidget(
            self.botao_adicionar
        )

        # =========================
        # TABELA
        # =========================

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(3)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Data",
            "Obreiro"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout_principal.addWidget(
            self.tabela
        )

        # =========================
        # EXCLUIR
        # =========================

        self.botao_excluir = QPushButton(
            "Excluir Selecionada"
        )

        self.botao_excluir.clicked.connect(
            self.excluir_escala
        )

        layout_principal.addWidget(
            self.botao_excluir
        )

        self.setLayout(
            layout_principal
        )

    # =========================
    # CARREGAR OBRIEIROS
    # =========================

    def carregar_obreiros(self):

        self.combo_obreiro.clear()

        obreiros = self.banco.listar_obreiros()

        for obreiro in obreiros:

            self.combo_obreiro.addItem(
                obreiro["nome"],
                obreiro["id"]
            )

    # =========================
    # ADICIONAR ESCALA
    # =========================

    def adicionar_escala(self):

        if self.combo_obreiro.currentIndex() < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Cadastre pelo menos um obreiro."
            )

            return

        data = self.data_santa_ceia.date().toString(
            "yyyy-MM-dd"
        )

        obreiro_id = self.combo_obreiro.currentData()

        self.banco.adicionar_escala(
            data,
            obreiro_id
        )

        self.carregar_escalas()

    # =========================
    # CARREGAR ESCALAS
    # =========================

    def carregar_escalas(self):

        escalas = self.banco.listar_escalas()

        self.tabela.setRowCount(0)

        for escala in escalas:

            linha = self.tabela.rowCount()

            self.tabela.insertRow(linha)

            data = QDate.fromString(
                escala["data"],
                "yyyy-MM-dd"
            )

            data_formatada = data.toString(
                "dd/MM/yyyy"
            )

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    str(escala["id"])
                )
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    data_formatada
                )
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(
                    escala["nome_obreiro"]
                )
            )

    # =========================
    # EXCLUIR ESCALA
    # =========================

    def excluir_escala(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma escala."
            )

            return

        id_escala = int(
            self.tabela.item(
                linha,
                0
            ).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar",
            "Deseja excluir esta escala?"
        )

        if resposta == QMessageBox.StandardButton.Yes:

            self.banco.excluir_escala(
                id_escala
            )

            self.carregar_escalas()

    # =========================
    # FECHAR
    # =========================

    def closeEvent(self, event):

        self.banco.fechar()

        event.accept()