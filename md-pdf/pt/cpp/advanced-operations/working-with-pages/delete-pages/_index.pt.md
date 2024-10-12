---
title: Excluir páginas de PDF programaticamente
linktitle: Excluir páginas de PDF
type: docs
weight: 30
url: /cpp/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Você pode excluir páginas de um arquivo PDF usando Aspose.PDF para C++. Para excluir uma página específica da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## Excluir página do arquivo PDF

1. Chame o método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) e especifique o índice da página
1. Chame o método Save para salvar o arquivo PDF atualizado
O trecho de código a seguir mostra como excluir uma página específica do arquivo PDF usando C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Excluir uma página específica
    document->get_Pages()->Delete(2);

    // Salvar PDF atualizado
    document->Save(_dataDir + inputFileName);
}
```