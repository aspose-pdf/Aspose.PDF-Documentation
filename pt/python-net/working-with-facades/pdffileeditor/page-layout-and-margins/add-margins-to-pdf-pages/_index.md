---
title: Adicionar Margens às Páginas PDF
type: docs
weight: 10
url: /pt/python-net/add-margins-to-pdf-pages/
description: Adicionar margens personalizadas às páginas selecionadas de um PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Margens Personalizadas a Páginas PDF Específicas em Python
Abstract: Aprenda como adicionar margens personalizadas às páginas selecionadas de um PDF usando Aspose.PDF for Python. Este exemplo demonstra como expandir os limites da página especificando margens superior, inferior, esquerda e direita para páginas individuais, tornando os PDFs mais imprimíveis ou visualmente consistentes.
---

Adicionar margens às páginas PDF pode melhorar a legibilidade, preparar documentos para impressão ou alocar espaço para anotações. Usando Aspose.PDF for Python, desenvolvedores podem adicionar programaticamente margens a páginas específicas de um PDF sem modificar o layout do conteúdo.

Neste trecho de código, o [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) A classe é usada para adicionar margens de 0,5 polegada nas páginas 1 e 3 do documento de entrada. As margens são definidas em pontos (1 polegada = 72 pontos) e aplicadas individualmente à esquerda, à direita, ao topo e à base de cada página.

1. Abra o documento PDF de origem.
1. Crie uma instância de 'PdfFileEditor'.
1. Defina as margens e as páginas a serem modificadas.
1. Aplique as margens usando o método 'add_margins'.
1. Salve o PDF atualizado no arquivo de saída.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
