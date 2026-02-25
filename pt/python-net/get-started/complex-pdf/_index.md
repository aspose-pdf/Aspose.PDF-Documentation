---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
weight: 30
url: /pt/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET permite criar documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um PDF complexo usando Python
Abstract: Este artigo expande o processo básico de criação de PDF demonstrado no exemplo "Hello, World" ilustrando como criar um documento PDF mais complexo usando Python e Aspose.PDF. O documento de exemplo é desenvolvido para uma empresa fictícia de serviços de balsas de passageiros e inclui uma imagem, dois fragmentos de texto (um cabeçalho e um parágrafo) e uma tabela. O processo envolve várias etapas – instanciar um objeto `Document` para criar um PDF vazio, adicionar uma `Page` e, em seguida, inserir uma `Image` na página. Um `TextFragment` é criado para o cabeçalho usando a fonte Arial com tamanho de 24pt e alinhamento centralizado, que é então adicionado aos parágrafos da página. Um segundo `TextFragment` é adicionado para a descrição, usando a fonte Times New Roman com tamanho de 14pt e alinhamento à esquerda. Em seguida, uma tabela é criada e formatada com larguras de coluna específicas, bordas e preenchimento. A tabela inclui uma linha de cabeçalho com células destacadas e várias linhas de dados geradas por iteração
---

O exemplo [Hello, World](/pdf/python-net/hello-world-example/) mostrou passos simples para criar um documento PDF usando Python e Aspose.PDF. Neste artigo, examinaremos a criação de um documento mais complexo com Aspose.PDF para Python. Como exemplo, usaremos um documento de uma empresa fictícia que opera serviços de balsas de passageiros. Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela.

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Nesta etapa criaremos um documento PDF vazio com alguns metadados, mas sem páginas.
1. Adicionar uma [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao objeto do documento. Assim, agora nosso documento terá uma página.
1. Adicionar uma [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) à Page.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o cabeçalho. Para o cabeçalho usaremos a fonte Arial com tamanho 24pt e alinhamento central.
1. Adicionar o cabeçalho aos [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para a descrição. Para a descrição usaremos a fonte Arial com tamanho 24pt e alinhamento central.
1. Adicionar (descrição) aos parágrafos da página.
1. Criar e estilizar a Tabela. Definir largura das colunas, bordas, preenchimento e fonte.
1. Adicionar (tabela) aos [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página.
1. Salvar o documento "Complex.pdf".

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```

