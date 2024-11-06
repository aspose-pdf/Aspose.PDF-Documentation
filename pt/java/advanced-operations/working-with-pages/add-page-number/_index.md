---
title: Adicionar Número de Página ao PDF 
linktitle: Adicionar Número de Página
type: docs
weight: 100
url: pt/java/add-page-number/
description: Aspose.PDF para Java permite que você adicione uma Carimbo de Número de Página ao seu arquivo PDF usando a classe PageNumber Stamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Todos os documentos devem ter números de página. O número da página facilita para o leitor localizar diferentes partes do documento.
**Aspose.PDF para Java** permite que você adicione números de página com PageNumberStamp.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Você pode usar a classe [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) para adicionar um carimbo de número de página em um documento PDF.
 O [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class fornece métodos para criar um carimbo baseado em número de página, como formato, margens, alinhamentos, número inicial etc. Para adicionar um carimbo de número de página, você precisa criar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) com as propriedades necessárias. Depois disso, você pode chamar o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo no arquivo PDF. Você também pode definir os atributos de fonte do carimbo de número de página.

O seguinte trecho de código mostra como adicionar números de página em um arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Criar carimbo de número de página
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Se o carimbo é de fundo
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Página # de " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Definir propriedades do texto
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Adicionar carimbo a uma página específica
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Salvar documento de saída
        pdfDocument.save(_dataDir);

    }
}
```