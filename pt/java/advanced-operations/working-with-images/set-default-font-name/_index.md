---
title: Definir Nome de Fonte Padrão
linktitle: Definir Nome de Fonte Padrão
type: docs
weight: 90
url: pt/java/set-default-font-name/
description: Esta seção descreve como definir o nome de fonte padrão usando a biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
---

A API **Aspose.PDF para Java** permite definir um nome de fonte padrão quando uma fonte não está disponível no documento. Você pode usar o método [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) da classe [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) para definir o nome da fonte padrão. Caso setDefaultFontName seja definido como nulo, a fonte **Times New Roman** será usada.

O trecho de código a seguir mostra como definir um nome de fonte padrão ao salvar um PDF em uma imagem:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

public class ExampleSetDefaultFontName {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SetDefaultFontName() {
        
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        FileOutputStream imageStream = null;;
        try {
            imageStream = new FileOutputStream(_dataDir + "SetDefaultFontName.png");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated bloco de captura
            e.printStackTrace();
        }

        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.setDefaultFontName ("Arial");
        pngDevice.setRenderingOptions(ro);
        pngDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
    }    
}
```