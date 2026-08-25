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
    QFrame,
    QFileDialog
)

from PyQt6.QtCore import Qt
from database import Banco
from gerar_pdf import gerar_pdf as criar_pdf

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

        layout_principal.setContentsMargins(
            0, 0, 0, 0
        )

        layout_principal.setSpacing(0)

        # ==================================================
        # BARRA AZUL SUPERIOR
        # ==================================================

        barra_superior = QFrame()

        barra_superior.setFixedHeight(65)

        barra_superior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_AZUL};
            }}
        """)

        layout_barra = QHBoxLayout()

        layout_barra.setContentsMargins(
            20, 0, 20, 0
        )

        barra_superior.setLayout(
            layout_barra
        )

        titulo_barra = QLabel(
            "VISUALIZAR ESCALA"
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
            30, 25, 30, 25
        )

        layout_central.setSpacing(15)

        area_central.setLayout(
            layout_central
        )

        # ==================================================
        # SELEÇÃO DA ESCALA
        # ==================================================

        label_selecao = QLabel(
            "Selecione a Santa Ceia:"
        )

        label_selecao.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 16px;
                font-weight: bold;
            }}
        """)

        layout_central.addWidget(
            label_selecao
        )

        self.combo_escalas = QComboBox()

        self.combo_escalas.currentIndexChanged.connect(
            self.mostrar_escala
        )

        layout_central.addWidget(
            self.combo_escalas
        )

        # ==================================================
        # DATA
        # ==================================================

        self.label_data = QLabel(
            "Data: -"
        )

        self.label_data.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 20px;
                font-weight: bold;
                padding: 8px;
            }}
        """)

        self.label_data.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_central.addWidget(
            self.label_data
        )

        # ==================================================
        # TABELA
        # ==================================================

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

        layout_central.addWidget(
            self.tabela
        )

        # ==================================================
        # BOTÕES
        # ==================================================

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

        estilo_botao = f"""
            QPushButton {{
                background-color: {COR_AZUL};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 11px 18px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QPushButton:pressed {{
                background-color: {COR_VERDE};
            }}
        """

        self.botao_pdf.setStyleSheet(
            estilo_botao
        )

        self.botao_whatsapp.setStyleSheet(
            estilo_botao
        )

        layout_botoes.addWidget(
            self.botao_pdf
        )

        layout_botoes.addWidget(
            self.botao_whatsapp
        )

        layout_central.addLayout(
            layout_botoes
        )

        layout_principal.addWidget(
            area_central
        )

        # ==================================================
        # BARRA VERDE INFERIOR
        # ==================================================

        barra_inferior = QFrame()

        barra_inferior.setFixedHeight(40)

        barra_inferior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_VERDE};
            }}
        """)

        layout_rodape = QHBoxLayout()

        layout_rodape.setContentsMargins(
            20, 0, 20, 0
        )

        barra_inferior.setLayout(
            layout_rodape
        )

        rodape = QLabel(
            "Visualização das escalas cadastradas"
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
    # CARREGAR ESCALAS
    # ==================================================

    def carregar_escalas(self):

        # Bloqueia o sinal para não chamar mostrar_escala()
        # enquanto estamos preenchendo o ComboBox
        self.combo_escalas.blockSignals(True)

        self.combo_escalas.clear()

        # Primeiro item
        self.combo_escalas.addItem(
            "Selecione",
            None
        )

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

        # Deixa "Selecione" selecionado
        self.combo_escalas.setCurrentIndex(0)

        # Libera os sinais novamente
        self.combo_escalas.blockSignals(False)

        # Limpa a visualização
        self.label_data.setText(
            "Data: -"
        )

        self.tabela.setRowCount(0)

    # ==================================================
    # MOSTRAR ESCALA
    # ==================================================

    def mostrar_escala(self, index):

        if index <= 0:
            self.label_data.setText(
                "Data: -"
            )

            self.tabela.setRowCount(0)

            return

        escala_id = (
            self.combo_escalas.currentData()
        )

        if escala_id is None:
            return
        
        print("ID SELECIONADO:", escala_id)
        print("CONEXÃO BANCO:", self.banco.conexao)

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

        escala_id = (
            self.combo_escalas.currentData()
        )

        if escala_id is None:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma Santa Ceia."
            )

            return

        registros = (
            self.banco.buscar_santa_ceia(
                escala_id
            )
        )

        if not registros:

            QMessageBox.warning(
                self,
                "Atenção",
                "Não existem obreiros cadastrados "
                "para esta Santa Ceia."
            )

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

        obreiros = []

        for registro in registros:

            obreiros.append(
                registro["obreiro_nome"]
            )

        nome_arquivo = (
            f"Escala_Santa_Ceia_"
            f"{data_formatada.replace('/', '-')}.pdf"
        )

        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar PDF",
            nome_arquivo,
            "Arquivos PDF (*.pdf)"
        )

        if not caminho:
            return

        try:

            criar_pdf(
                caminho,
                data_formatada,
                obreiros
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "PDF gerado com sucesso!"
            )

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível gerar o PDF:\n\n{erro}"
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

        event.accept()