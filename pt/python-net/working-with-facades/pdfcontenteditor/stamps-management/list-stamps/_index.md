---
title: Listar Carimbos
type: docs
weight: 70
url: /pt/python-net/list-stamps/
description: Este exemplo carrega um PDF, recupera todos os carimbos da página 1, os imprime e exibe uma mensagem caso nenhum carimbo seja encontrado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Listar Anotações de Carimbo de Borracha em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como recuperar e listar anotações de carimbo de borracha de um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como acessar os carimbos em uma página específica e exibir seus detalhes.
---

Ao trabalhar com PDFs anotados, pode ser necessário inspecionar os carimbos de borracha existentes antes de modificá-los ou removê-los. O método 'get_stamps()' permite recuperar todos os carimbos colocados em uma página específica. Você pode então percorrer os resultados e processá-los programaticamente.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Recuperar todos os carimbos da página 1.
1. Itere pela coleção de carimbos.
1. Imprima cada carimbo.
1. Exiba uma mensagem se não houver carimbos.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
