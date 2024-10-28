---
title: Excluir Imagens do Arquivo PDF
linktitle: Excluir Imagens
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Esta seção explica como excluir Imagens de um Arquivo PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

Para excluir uma imagem de um arquivo PDF, basta usar o método delete(..) da coleção Images.

1. Crie um objeto Document e abra o arquivo PDF de entrada.
1. Obtenha a Página que contém a imagem da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. As imagens estão na coleção Images, encontrada na coleção [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) da página.
1. Exclua uma imagem com o método Delete da coleção Images.
1. Salve a saída usando o método Save do objeto Document.

O snippet de código a seguir mostra como excluir uma imagem de um arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Criar carimbo de número de página
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Se o carimbo é de fundo
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Página # de " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Definir propriedades do texto
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0F);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getAqua());

        // Adicionar carimbo a uma página específica
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Salvar documento de saída
        pdfDocument.save(_dataDir);

    }
}
```