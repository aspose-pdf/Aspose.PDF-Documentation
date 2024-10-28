---
title: Mover Páginas de PDF programaticamente C++
linktitle: Mover Páginas de PDF
type: docs
weight: 20
url: /cpp/move-pages/
description: Tente mover páginas para a localização desejada ou para o final de um arquivo PDF usando Aspose.PDF para C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Movendo uma Página de um Documento PDF para Outro

Mover páginas de PDF em um documento é uma tarefa muito interessante e popular.
Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando C++.
Para mover uma página devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o arquivo PDF de origem.
1. Obter a Página da coleção do [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Adicionar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) a página ao documento de destino.
1. Salvar o PDF de saída usando o método Save.
1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) página no documento de origem.
1. Salve o PDF de origem usando o método Save.

O trecho de código a seguir mostra como mover uma página.

```cpp
void MovePage()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // Salvar arquivo de saída
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## Movendo um conjunto de Páginas de um Documento PDF para Outro

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o arquivo PDF de origem.
1. Defina um array com números de páginas a serem movidas.
1. Execute o loop através do array:
1. Obtenha a Página da coleção do [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Adicione](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) a página ao documento de destino.
1. Salve o PDF de saída usando o método Save.
1. [Exclua](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) a página no documento de origem.
1. Salve o PDF de origem usando o método Save.

O trecho de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```cpp
void MoveBunchPages()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // Salvar arquivos de saída
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## Movendo uma Página para um novo local no documento PDF atual

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o arquivo PDF de origem.
1. Obtenha a Página da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Adicione](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) a página para o novo local (por exemplo, para o final).
1. [Exclua](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) a página na localização anterior.
1. Salve o PDF de saída usando o método Save.

```cpp
void MovePagesInOnePDF()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Salvar arquivo de saída
    srcDocument->Save(dstFileName);
}
```