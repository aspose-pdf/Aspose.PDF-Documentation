---
title: Como Mesclar PDF usando Python via C++
linktitle: Mesclar arquivos PDF
type: docs
weight: 10
url: /pt/python-cpp/merge-pdf-documents/
keywords: "mesclar vários pdf em um único pdf python, combinar vários pdf em um python, mesclar vários pdf em um python"
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mesclar ou combinar múltiplos PDFs em um único PDF em Python via C++

Ao utilizar Python e uma biblioteca C++ da Aspose, você pode mesclar vários arquivos PDF em um único PDF de forma eficiente.

Para concatenar dois arquivos PDF:

1. Abra o primeiro documento
1. Em seguida, adicione as páginas do segundo documento ao primeiro
1. Salve o arquivo de saída concatenado com o método 'document.save'.

O trecho de código a seguir mostra como concatenar arquivos PDF.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # Abra o primeiro documento
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # Adicione as páginas do segundo documento ao primeiro
    document1.pages.add(document2.pages)

    # Salve o arquivo de saída concatenado
    document1.save(output_file)
```