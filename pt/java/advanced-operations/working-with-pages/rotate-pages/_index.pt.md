---
title: Rotacionar Páginas PDF programaticamente
linktitle: Rotacionar Páginas PDF
type: docs
weight: 60
url: /java/rotate-pages/
description: Alterar a orientação da página e ajustar o conteúdo da página para a nova orientação usando Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Alterar Orientação da Página

Este artigo descreve como atualizar ou alterar a orientação das páginas em um arquivo PDF existente.

Aspose.PDF para Java tem a funcionalidade de mudar a orientação da página de paisagem para retrato e vice-versa. Para alterar a orientação da página, defina o [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) da página usando o seguinte trecho de código.

Você também pode alterar a orientação da página definindo o ângulo de rotação usando o método Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // Precisamos mover a página para cima para compensar a mudança de tamanho da página
            // // (a borda inferior da página é 0,0 e a informação geralmente é colocada a partir do
            // // topo da página. É por isso que movemos a borda inferior para cima na diferença entre
            // // a altura antiga e a nova.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // Às vezes também precisamos definir o CropBox (se ele foi definido no arquivo original)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Definindo o ângulo de rotação da página
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Salvar arquivo de saída
        pdfDocument.save(_dataDir);
    }    
}
```