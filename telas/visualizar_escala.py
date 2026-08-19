from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
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

class TelaVisualizarEscala(QWidget):

    def __init__(self):
        super().__init__()

        self.banco = Banco()

        self.setWindowTitle("Visualizar Escala - Santa Ceia")
        self.resize(800, 600)

        self.criar_interface()
        self.carregar_escalas()

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        titulo = QLabel(
            "Visualizar Escala da Santa Ceia"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(titulo)

        # ----------------------------------------------
        # SELECIONAR ESCALA
        # ----------------------------------------------

        layout_selecao = QHBoxLayout()

        label = QLabel(
            "Selecione a Santa Ceia:"
        )

        self.combo_escalas = QComboBox()

        self.combo_escalas.currentIndexChanged.connect(
            self.mostrar_escala
        )

        layout_selecao.addWidget(label)
        layout_selecao.addWidget(
            self.combo_escalas
        )

        layout_principal.addLayout(
            layout_selecao
        )

        # ----------------------------------------------
        # DATA
        # ----------------------------------------------

        self.label_data = QLabel(
            "Data: -"
        )

        self.label_data.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        layout_principal.addWidget(
            self.label_data
        )

        # ----------------------------------------------
        # TABELA
        # ----------------------------------------------

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(2)

        self.tabela.setHorizontalHeaderLabels([
            "Nº",
            "Obreiro"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabela.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        layout_principal.addWidget(
            self.tabela
        )

        # ----------------------------------------------
        # BOTÕES
        # ----------------------------------------------

        layout_botoes = QHBoxLayout()

        self.botao_pdf = QPushButton(
            "Gerar PDF"
        )

        self.botao_whatsapp = QPushButton(
            "Enviar WhatsApp"
        )

        self.botao_pdf.clicked.connect(
            self.gerar_pdf
        )

        self.botao_whatsapp.clicked.connect(
            self.enviar_whatsapp
        )

        layout_botoes.addWidget(
            self.botao_pdf
        )

        layout_botoes.addWidget(
            self.botao_whatsapp
        )

        layout_principal.addLayout(
            layout_botoes
        )

        self.setLayout(
            layout_principal
        )

    # ==================================================
    # CARREGAR ESCALAS
    # ==================================================

    def carregar_escalas(self):

        self.combo_escalas.clear()

        escalas = (
            self.banco.listar_santa_ceias()
        )

        for escala in escalas:

            data = escala["data"]

            partes = data.split("-")

            if len(partes) == 3:

                data_formatada = (
                    f"{partes[2]}/"
                    f"{partes[1]}/"
                    f"{partes[0]}"
                )

            else:

                data_formatada = data

            self.combo_escalas.addItem(
                data_formatada,
                escala["id"]
            )

        if self.combo_escalas.count() > 0:

            self.mostrar_escala(0)

        else:

            self.label_data.setText(
                "Data: -"
            )

            self.tabela.setRowCount(0)

    # ==================================================
    # MOSTRAR ESCALA
    # ==================================================

    def mostrar_escala(self, index):

        if index < 0:
            return

        escala_id = (
            self.combo_escalas.currentData()
        )

        if escala_id is None:
            return

        registros = (
            self.banco.buscar_santa_ceia(
                escala_id
            )
        )

        self.tabela.setRowCount(0)

        if not registros:
            return

        data = registros[0]["data"]

        partes = data.split("-")

        if len(partes) == 3:

            data_formatada = (
                f"{partes[2]}/"
                f"{partes[1]}/"
                f"{partes[0]}"
            )

        else:

            data_formatada = data

        self.label_data.setText(
            f"Data: {data_formatada}"
        )

        for numero, registro in enumerate(
            registros,
            start=1
        ):

            linha = self.tabela.rowCount()

            self.tabela.insertRow(
                linha
            )

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    str(numero)
                )
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    registro["obreiro_nome"]
                )
            )

    # ==================================================
    # GERAR PDF
    # ==================================================

    def gerar_pdf(self):

        if self.combo_escalas.currentData() is None:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma escala."
            )

            return

        QMessageBox.information(
            self,
            "Em desenvolvimento",
            "A geração do PDF será implementada "
            "na próxima etapa."
        )

    # ==================================================
    # WHATSAPP
    # ==================================================

    def enviar_whatsapp(self):

        if self.combo_escalas.currentData() is None:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma escala."
            )

            return

        QMessageBox.information(
            self,
            "Em desenvolvimento",
            "O envio pelo WhatsApp será implementado "
            "posteriormente."
        )

    # ==================================================
    # FECHAR
    # ==================================================

    def closeEvent(self, event):

        self.banco.fechar()

        event.accept()