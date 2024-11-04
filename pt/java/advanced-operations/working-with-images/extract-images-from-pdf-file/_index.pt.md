---
title: Extrair Imagens de Arquivo PDF
linktitle: Extrair Imagens
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Esta seção mostra como extrair imagens de um arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
---

Cada página contém uma coleção de [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources), e esta, por sua vez, contém a coleção de Imagens, onde todas as imagens de uma página são mantidas. O objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) obtém uma imagem específica na coleção de Imagens.

Para extrair uma imagem de uma página:

Obtenha a imagem da coleção de Imagens usando o índice da imagem.  
Use o método save(..) do objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) para salvar a imagem extraída.

O trecho de código a seguir mostra como extrair imagens do arquivo PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Extrair uma imagem específica
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Salvar imagem de saída
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Salvar arquivo PDF atualizado
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```