import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


def gerar_pdf(
    caminho,
    data,
    obreiros
):

    # ==================================================
    # CAMINHO DAS IMAGENS
    # ==================================================

    pasta_projeto = os.path.dirname(
        os.path.abspath(__file__)
    )

    caminho_logo = os.path.join(
        pasta_projeto,
        "imagens",
        "logo_igreja.jpg"
    )

    caminho_assinatura = os.path.join(
        pasta_projeto,
        "imagens",
        "assinatura.png"
    )

    # ==================================================
    # DOCUMENTO
    # ==================================================

    documento = SimpleDocTemplate(
        caminho,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm
    )

    estilos = getSampleStyleSheet()

    estilo_titulo = ParagraphStyle(
        "Titulo",
        parent=estilos["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0D47A1"),
        spaceAfter=5
    )

    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#1976D2"),
        spaceAfter=15
    )

    estilo_data = ParagraphStyle(
        "Data",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=14,
        leading=18,
        spaceAfter=15
    )

    estilo_rodape = ParagraphStyle(
        "Rodape",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=10,
        textColor=colors.grey
    )

    elementos = []

    # ==================================================
    # LOGO
    # ==================================================

    if os.path.exists(caminho_logo):

        logo = Image(
            caminho_logo
        )

        logo.drawHeight = 2.5 * cm
        logo.drawWidth = 2.5 * cm

        tabela_logo = Table(
            [[logo]],
            colWidths=[17 * cm]
        )

        tabela_logo.setStyle(
            TableStyle([
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )
            ])
        )

        elementos.append(
            tabela_logo
        )

        elementos.append(
            Spacer(1, 8)
        )

    # ==================================================
    # CABEÇALHO
    # ==================================================

    elementos.append(
        Paragraph(
            "ADSAM 317 Ministério Madureira",
            estilo_titulo
        )
    )

    elementos.append(
        Paragraph(
            "ESCALA DA SANTA CEIA",
            estilo_subtitulo
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Data: {data}</b>",
            estilo_data
        )
    )

    elementos.append(
        Spacer(1, 5)
    )

    # ==================================================
    # TABELA
    # ==================================================

    dados = [
        [
            "Nº",
            "Obreiro"
        ]
    ]

    for numero, obreiro in enumerate(
        obreiros,
        start=1
    ):

        dados.append(
            [
                str(numero),
                obreiro
            ]
        )

    tabela = Table(
        dados,
        colWidths=[
            2 * cm,
            14 * cm
        ],
        repeatRows=1
    )

    tabela.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1976D2")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "CENTER"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#BDBDBD")
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                "Helvetica"
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                11
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                9
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                9
            )
        ])
    )

    elementos.append(
        tabela
    )

    # ==================================================
    # ASSINATURA
    # ==================================================

    elementos.append(
        Spacer(1, 35)
    )

    if os.path.exists(caminho_assinatura):

        assinatura = Image(
            caminho_assinatura
        )

        assinatura.drawHeight = 2 * cm
        assinatura.drawWidth = 5 * cm

        tabela_assinatura = Table(
            [[assinatura]],
            colWidths=[17 * cm]
        )

        tabela_assinatura.setStyle(
            TableStyle([
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )
            ])
        )

        elementos.append(
            tabela_assinatura
        )

    else:

        elementos.append(
            Spacer(1, 20)
        )

    elementos.append(
        Paragraph(
            "Carlos Alexandre",
            estilo_rodape
        )
    )

    elementos.append(
        Spacer(1, 15)
    )

    elementos.append(
        Paragraph(
            "Escala Santa Ceia",
            estilo_rodape
        )
    )

    # ==================================================
    # GERAR PDF
    # ==================================================

    documento.build(
        elementos
    )