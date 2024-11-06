---
title: Adicionar Páginas em PDF com C++
linktitle: Adicionar Páginas
type: docs
weight: 10
url: pt/cpp/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página na localização desejada em um arquivo PDF. Aprenda como mover, remover (excluir) páginas de um arquivo PDF usando C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta seção mostra como adicionar páginas a um PDF usando a biblioteca **Aspose.PDF para C++**.

Aspose.PDF para C++ API fornece total flexibilidade para trabalhar com páginas em um documento PDF usando C++.

Ela mantém todas as páginas de um documento PDF em [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) que pode ser usada para trabalhar com páginas PDF.
Aspose.PDF para C++ permite que você insira uma página em um documento PDF em qualquer localização no arquivo, bem como adicione páginas ao final de um arquivo PDF.

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para C++ permite que você insira uma página em um documento PDF em qualquer localização no arquivo, bem como adicione páginas ao final de um arquivo PDF.

### Inserir Página Vazia em um Arquivo PDF na Localização Desejada

O seguinte exemplo de código explica como adicionar uma página em um documento PDF.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o arquivo PDF de entrada.
1. Chame o método [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) com o índice especificado.
1. Salve o PDF de saída

O seguinte trecho de código mostra como inserir uma página em um arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void InsertEmptyPageAtDesiredLocation() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Inserir uma página em branco em um PDF
    document->get_Pages()->Insert(2);

    // Salvar arquivo de saída
    document->Save(_dataDir + outputFileName);
}
```

No exemplo de código a seguir, você pode inserir uma página vazia na localização desejada copiando os parâmetros da página especificada:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Inserir uma página vazia em um PDF
    auto pageNew = document->get_Pages()->Insert(2);

    // copiar parâmetros da página da página 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Salvar arquivo de saída
    document->Save(_dataDir + outputFileName);
}
```

### Adicionar uma Página Vazia no Final de um Arquivo PDF

Às vezes, você quer garantir que um documento termine em uma página vazia. Este tópico explica como inserir uma página em branco no final do documento PDF.

Para inserir uma página em branco no final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o arquivo PDF de entrada.
1. Chame o método [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), sem quaisquer parâmetros.
1. Salve o PDF de saída usando o método Save.

O snippet de código a seguir mostra como inserir uma página em branco no final de um arquivo PDF.

```cpp
void AddEmptyPageEnd() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Inserir uma página em branco no final de um arquivo PDF
    document->get_Pages()->Add();

    // Salvar arquivo de saída
    document->Save(_dataDir + outputFileName);
}
```