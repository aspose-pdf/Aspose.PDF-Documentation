---
title: Definir Tamanho do PDF usando Python via C++
linktitle: Definir Tamanho do PDF
type: docs
weight: 30
url: /pt/python-cpp/get-and-set-page-properties/
description: Esta seção mostra como obter ou definir propriedades de página de PDF, como tamanho do documento, usando Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Definir Tamanho do Arquivo PDF

Aspose.PDF para Python via C++ permite que você leia e defina propriedades das páginas em um arquivo PDF em suas aplicações Python.

O próximo trecho de código abre um arquivo PDF, redimensiona a primeira página ajustando a **Caixa de Recorte** (a caixa de recorte é o tamanho da "página" em que seu documento PDF é exibido no Adobe Acrobat) e salva o documento modificado em um novo arquivo.

1. Crie um objeto de documento a partir do arquivo de entrada
1. Obtenha a coleção de páginas do documento usando [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. Obtenha a primeira página da coleção de páginas com [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Obtenha o retângulo da caixa de corte da página usando [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Calcule as novas coordenadas para a caixa de corte
1. Atualize as coordenadas da caixa de corte com os novos valores
1. Salve o documento modificado no arquivo de saída com o método 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Obtenha o diretório de trabalho atual e crie o caminho para o diretório "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # Crie os caminhos dos arquivos de entrada e saída
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Crie um objeto de documento a partir do arquivo de entrada
    doc = apCore.document_create_from_file(inputFile)

    # Obtenha a coleção de páginas do documento
    pages = apCore.document_get_pages(doc)

    # Obtenha a primeira página da coleção de páginas
    page = apCore.page_collection_get_page(pages, 1)

    # Obtenha o retângulo da caixa de corte da página
    crop_box = apCore.page_get_rectangle(page)

    # Calcule as novas coordenadas para a caixa de corte
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Atualize as coordenadas da caixa de corte com os novos valores
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Salve o documento modificado no arquivo de saída
    apCore.document_save(doc, output_file)

    # Feche o manipulador de documentos
    apCore.close_handle(doc)
```