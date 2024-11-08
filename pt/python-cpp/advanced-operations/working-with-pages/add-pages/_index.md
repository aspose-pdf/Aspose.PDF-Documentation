---
title: Adicionar Páginas em PDF com Python via C++
linktitle: Adicionar Páginas
type: docs
weight: 10
url: /pt/python-cpp/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página na localização desejada em um arquivo PDF em Python usando C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Inserir Página Vazia em um Arquivo PDF na Localização Desejada

O trecho de código abre um documento PDF, adiciona uma página vazia a ele e salva o documento modificado como um novo arquivo PDF.

Para inserir uma página vazia em um arquivo PDF:

1. Abra o documento PDF
1. Adicione uma nova página em branco ao documento
1. Salve o documento modificado no arquivo de saída com o método 'document.save'

O seguinte trecho de código mostra como inserir uma página em um arquivo PDF:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Defina o caminho do diretório onde os arquivos PDF de exemplo estão localizados
    dataDir = os.path.join(os.getcwd(), "samples")

    # Defina o caminho do arquivo de entrada
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Defina o caminho do arquivo de saída
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Abra o documento PDF
    document = apw.Document(input_file)

    # Adicione uma nova página em branco ao documento
    document.pages.add()

    # Salve o documento modificado no arquivo de saída
    document.save(output_file)
```