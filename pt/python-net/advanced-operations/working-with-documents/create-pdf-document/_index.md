---
title: Criar arquivos PDF em Python
linktitle: Criar documento PDF
type: docs
weight: 10
url: /pt/python-net/create-pdf-document/
description: Aprenda como criar arquivos PDF e gerar PDFs pesquisáveis em Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar arquivo PDF com Python
Abstract: Aspose.PDF for Python via .NET é uma API versátil projetada para desenvolvedores manipular arquivos PDF em aplicações Python direcionadas ao framework .NET. Ela permite que os usuários criem, carreguem, modifiquem e convertam documentos PDF sem esforço. Este artigo fornece um guia passo a passo para criar um arquivo PDF simples usando Aspose.PDF. O processo envolve inicializar um objeto `Document`, adicionar uma `Page` ao documento, inserir um `TextFragment` nos parágrafos da página e salvar o arquivo como PDF. O trecho de código Python incluído demonstra essas etapas criando um documento PDF que contém o texto "Hello World!". Esta API simplifica o manuseio de PDFs com código mínimo, aumentando a produtividade dos desenvolvedores que trabalham com PDFs em ambientes .NET.
---

**Aspose.PDF for Python via .NET** é uma API de manipulação de PDF que permite que os desenvolvedores criem, carreguem, modifiquem e convertam arquivos PDF diretamente do Python para aplicações .NET com apenas algumas linhas de código.

Use estes exemplos quando precisar gerar novos arquivos PDF do zero ou converter a saída de OCR em documentos PDF pesquisáveis em Python.

## Como Criar um Arquivo PDF Simples

Para criar um PDF usando Python via .NET com Aspose.PDF, você pode seguir estas etapas:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do objeto Document
1. Adicione um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à coleção [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1.º Guarde o documento PDF resultante

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## Como criar um documento PDF pesquisável

Aspose.PDF for Python via .NET permite criar e manipular documentos PDF existentes. Ao adicionar elementos de Texto a um arquivo PDF, o PDF resultante é pesquisável. No entanto, ao converter uma imagem contendo texto para um arquivo PDF, o conteúdo do PDF resultante não é pesquisável. Como solução alternativa, podemos aplicar OCR ao arquivo resultante para que ele se torne pesquisável.

O seguinte é o código completo para atender a este requisito:

1. Carregar o PDF usando 'ap.Document'.
1. Configurar a resolução de renderização.
1. Usar 'PngDevice.process' para converter a página PDF selecionada em uma imagem.
1. Executar OCR na imagem gerada.
1. Criar um novo PDF a partir da saída de OCR.
1. Salvar o PDF pesquisável.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Tópicos relacionados ao Document

- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Formate documentos PDF em Python](/pdf/pt/python-net/formatting-pdf-document/)
- [Manipule documentos PDF em Python](/pdf/pt/python-net/manipulate-pdf-document/)
- [Otimize arquivos PDF em Python](/pdf/pt/python-net/optimize-pdf/)

