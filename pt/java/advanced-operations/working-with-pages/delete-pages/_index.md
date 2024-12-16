---
title: Excluir Páginas PDF programaticamente
linktitle: Excluir Páginas PDF
type: docs
weight: 40
url: /pt/java/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Você pode excluir páginas de um arquivo PDF usando o Aspose.PDF para Java. Para excluir uma página específica da [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) simplesmente chame o método delete() e especifique o índice da página específica que você deseja excluir. Em seguida, chame o método save para salvar o arquivo PDF atualizado.

## Excluir Página do Arquivo PDF

1. Chame o método Delete e especifique o índice da página
1. Chame o método Save para salvar o arquivo PDF atualizado
O seguinte trecho de código mostra como excluir uma página específica do arquivo PDF usando Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Excluir uma página específica
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Salvar PDF atualizado
    pdfDocument.save(_dataDir);    

  }
```