---
title: Dividir PDF programaticamente
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/java/split-document/
description: Este tópico mostra como dividir páginas PDF em arquivos PDF individuais em suas aplicações Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Você pode dividir arquivos PDF usando Aspose.PDF e obter os resultados online neste link: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Este tópico mostra como dividir páginas PDF com Aspose.PDF para Java em arquivos PDF individuais em suas aplicações Java. Para dividir páginas PDF em arquivos PDF de página única usando Java, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Para cada iteração, crie um novo objeto Document e adicione o objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individual no documento vazio.
1. Salve o novo PDF usando o método Save.

O seguinte trecho de código Java mostra como dividir páginas de um PDF em arquivos PDF individuais.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Percorrer todas as páginas
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```