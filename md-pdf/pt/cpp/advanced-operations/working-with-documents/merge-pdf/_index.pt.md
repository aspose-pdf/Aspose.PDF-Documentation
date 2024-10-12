---
title: Mesclar PDF usando C++
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Mesclar arquivos PDF não é uma tarefa fácil, mas é muito popular. Você pode usar a biblioteca Aspose.PDF para C++ para combinar arquivos PDF em um documento rapidamente e facilmente.

## Mesclar Arquivos PDF usando C++

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), cada um contendo um dos arquivos PDF de entrada.
1. Em seguida, chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) para o objeto Document ao qual você deseja adicionar o outro arquivo PDF.
1. Adicione a [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) do segundo documento ao primeiro arquivo.
1. Finalmente, salve o arquivo PDF de saída usando o método Save.

O trecho de código a seguir mostra como concatenar arquivos PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Abrir documento
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Adicionar páginas do segundo documento ao primeiro
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Salvar arquivo de saída concatenado
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Exemplo ao Vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é um aplicativo web gratuito online que permite investigar como a funcionalidade de mesclagem de apresentações funciona.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)