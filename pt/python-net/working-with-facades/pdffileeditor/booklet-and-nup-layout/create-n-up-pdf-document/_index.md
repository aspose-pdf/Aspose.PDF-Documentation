---
title: Criar Documento PDF N-Up
type: docs
weight: 10
url: /pt/python-net/create-n-up-pdf-document/
description: Aprenda como criar um documento PDF N-Up enquanto lida com possíveis erros de forma segura usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Layout PDF N-Up em Python
Abstract: Aprenda como gerar um layout PDF N-Up usando Aspose.PDF for Python. Este exemplo demonstra como combinar várias páginas de um documento PDF em uma única página usando o método ‘make_n_up’ ou ‘try_make_n_up’ da classe PdfFileEditor.
---

Um layout N-Up coloca várias páginas de um documento PDF em uma única página em formato de grade. Esse layout é frequentemente usado para imprimir apresentações, folhetos ou relatórios onde várias páginas podem ser visualizadas de uma só vez.

Usando Aspose.PDF for Python, os desenvolvedores podem criar rapidamente um documento N-Up especificando o número de linhas e colunas que determinam quantas páginas originais aparecem em cada página de saída.

Neste trecho de código, o método 'make_n_up' da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe organiza as páginas do PDF de entrada em uma grade 2 × 2, significando que quatro páginas originais aparecem em uma página no documento de saída.

No exemplo mostrado, o layout usa 2 linhas e 2 colunas, produzindo quatro páginas por folha:

1. Abra o arquivo PDF de origem.
1. Crie uma instância de PdfFileEditor.
1. Especifique o número de linhas e colunas para o layout N-Up.
1. Gere um novo PDF com páginas combinadas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET permite gerar layouts N-Up com a classe PdfFileEditor. O método 'try_make_n_up' funciona de forma semelhante ao make_n_up, mas em vez de gerar uma exceção quando uma operação falha, ele retorna um valor booleano indicando se o processo foi bem-sucedido.

O layout N-Up organiza várias páginas PDF em uma única página usando uma grade definida por linhas e colunas.

O método 'try_make_n_up' oferece uma maneira mais segura de executar esta operação porque:

- Retorna True se o layout for criado com sucesso
- Retorna False se a operação falhar
- Não interrompe a execução do programa com exceções

No exemplo abaixo, o documento é organizado usando uma grade 2 × 2, que coloca quatro páginas originais em cada página de saída.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
