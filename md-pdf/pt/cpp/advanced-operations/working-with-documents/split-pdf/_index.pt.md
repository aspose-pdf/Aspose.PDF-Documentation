---
title: Dividir PDF programaticamente
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais com C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## Exemplo ao Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é uma aplicação web gratuita que permite investigar como a funcionalidade de divisão de apresentações funciona.

[![Aspose Dividir PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais nas suas aplicações C++. Para dividir páginas de PDF em arquivos PDF de uma única página usando C++, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Para cada iteração, crie um novo objeto Documento e copie o objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) individual para o documento vazio
1. Salve o novo PDF usando o método Save

O seguinte trecho de código C++ mostra como dividir páginas de PDF em arquivos PDF individuais.

```cpp
void SplittingDocuments() {
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String documentFileName("sample.pdf");
    
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Loop através de todas as páginas
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```