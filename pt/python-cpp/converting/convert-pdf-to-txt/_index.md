---
title: Converter PDF para TXT em Python
linktitle: Converter PDF para TXT
type: docs
weight: 20
url: /pt/python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: A biblioteca Aspose.PDF para Python via C++ permite converter PDF para o formato TXT usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Converter PDF para TXT

Aspose.PDF para Python via C++ suporta a conversão de documentos PDF para um arquivo de texto seguindo os passos:

1. Criar o caminho do arquivo de entrada e saída
1. Criar uma instância da fachada do extrator de PDF com [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Vincular o arquivo PDF ao extrator com [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Extrair o texto do arquivo PDF usando [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Escrever o texto extraído no arquivo de saída
1. Salvar o PDF de saída com o método 'document.save'.

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando Python via C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Criando o caminho do diretório de dados
    dataDir = os.path.join(os.getcwd(), "samples")

    # Criando o caminho do arquivo de entrada
    input_file = os.path.join(dataDir, "sample.pdf")

    # Criando o caminho do arquivo de saída
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Criando uma instância da fachada do extrator de PDF
    extactor = apCore.facades_pdf_extractor_create()

    # Vinculando o arquivo PDF ao extrator
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Extraindo o texto do arquivo PDF
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Escrevendo o texto extraído no arquivo de saída
    with open(output_file, 'w') as f:
        f.write(text)
```