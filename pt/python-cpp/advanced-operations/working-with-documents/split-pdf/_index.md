---
title: Dividir PDF programaticamente em Python
linktitle: Dividir arquivos PDF
type: docs
weight: 20
url: /pt/python-cpp/split-pdf-document/
keywords: dividir pdf em vários arquivos, dividir pdf em pdfs separados, dividir pdf python
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dividir páginas de PDF pode ser um recurso útil para aqueles que desejam dividir um arquivo grande em páginas separadas ou grupos de páginas.

## Exemplo ao Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é uma aplicação web gratuita online que permite investigar como a funcionalidade de divisão de apresentação funciona.

[![Aspose Dividir PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python C++. Para dividir páginas de PDF em arquivos PDF de uma única página usando Python, os seguintes passos podem ser seguidos:

O trecho de código configura os diretórios e caminhos de arquivo necessários, abre um documento PDF e, em seguida, percorre cada página do documento.
 Para cada página, cria um novo documento, copia a página atual para o novo documento e salva o novo documento como um arquivo PDF separado com uma convenção de nomenclatura específica.

1. Abra o documento de entrada
1. Inicialize a contagem de páginas
1. Percorra todas as páginas do documento

## Dividir PDF em vários arquivos ou PDFs separados em Python

O seguinte trecho de código Python mostra como dividir páginas de PDF em arquivos PDF individuais.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Abrir documento
    document = apw.Document(inputFile)

    pageCount = 1

    # Percorrer todas as páginas

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```