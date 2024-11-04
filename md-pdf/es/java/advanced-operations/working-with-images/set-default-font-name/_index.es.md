---
title: Configurar Nombre de Fuente Predeterminada
linktitle: Configurar Nombre de Fuente Predeterminada
type: docs
weight: 90
url: /java/set-default-font-name/
description: Esta sección describe cómo configurar el nombre de fuente predeterminado utilizando la biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
---

**Aspose.PDF para Java** API te permite configurar un nombre de fuente predeterminado cuando una fuente no está disponible en el documento. Puedes usar el método [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) de la clase [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) para establecer el nombre de fuente predeterminado. En caso de que setDefaultFontName se establezca en null, se usará la fuente **Times New Roman**.

El siguiente fragmento de código muestra cómo establecer un nombre de fuente predeterminado al guardar un PDF en una imagen:

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
            // TODO Auto-generated catch block
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