---
title: Mover Páginas de PDF
linktitle: Mover Páginas
type: docs
weight: 20
url: pt/java/move-pages/
description: Tente mover páginas para a localização desejada ou para o final de um arquivo PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Movendo uma Página de um Documento PDF para Outro

Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando Java.
Para mover uma página, devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem.
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de destino.
1. Obter a Página da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Adicionar a página ao documento de destino.
1. Salvar o PDF de saída usando o método Save.
1. Excluir a página no documento de origem.
1. Salvar o PDF de origem usando o método Save.

O seguinte trecho de código mostra como mover uma página.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Salvar arquivo de saída
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Movendo um monte de Páginas de um Documento PDF para Outro

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem.
1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de destino.
1. Defina um array com números de páginas a serem movidos.

1. Execute o loop através do array:
   1. Obtenha a Página da [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) da coleção.
   1. Adicione a página ao documento de destino.
1. Salve o PDF de saída usando o método Save.
1. Exclua a página no documento de origem usando o array.
1. Salve o PDF de origem usando o método Save.

O trecho de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Salve os arquivos de saída
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Movendo uma Página para um novo local no Documento PDF atual

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem.
1. Obtenha a página da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Adicione a página à nova localização (por exemplo, ao final).
1. Exclua a página na localização anterior.
1. Salve o PDF de saída usando o método Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Salvar arquivo de saída
    srcDocument.save(dstFileName);
  }
}
```