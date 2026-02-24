---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /pt/python-net/open-pdf-document/
description: Aprenda como abrir um arquivo PDF em Python usando a biblioteca Aspose.PDF para Python via .NET. Você pode abrir PDFs existentes, documentos a partir de um stream e documentos PDF criptografados.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrindo documentos PDF usando a biblioteca Aspose.PDF em Python
Abstract: Este artigo oferece um guia sobre como abrir documentos PDF existentes usando a biblioteca Aspose.PDF em Python. Ele descreve três métodos para isso – abrir um PDF especificando o nome do arquivo, abrir um PDF a partir de um stream e abrir um PDF criptografado fornecendo uma senha. Cada método inclui um trecho de código que demonstra como usar a biblioteca Aspose.PDF para acessar o PDF e imprimir o número de páginas que ele contém. Esses exemplos ilustram a flexibilidade e a funcionalidade do Aspose.PDF para lidar com diferentes cenários de acesso a arquivos PDF.
---

## Abrir documento PDF existente

Existem várias maneiras de abrir um documento. A mais fácil é especificar o nome do arquivo.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF existente a partir de um stream

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF criptografado

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

