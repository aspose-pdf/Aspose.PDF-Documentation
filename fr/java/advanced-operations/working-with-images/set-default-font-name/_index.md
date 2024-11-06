---
title: Définir le Nom de la Police par Défaut
linktitle: Définir le Nom de la Police par Défaut
type: docs
weight: 90
url: fr/java/set-default-font-name/
description: Cette section décrit comment définir le nom de la police par défaut en utilisant la bibliothèque Aspose.PDF pour Java.
lastmod: "2021-06-05"
---

L'API **Aspose.PDF pour Java** vous permet de définir un nom de police par défaut lorsqu'une police n'est pas disponible dans le document. Vous pouvez utiliser la méthode [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) de la classe [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) pour définir le nom de la police par défaut. Dans le cas où setDefaultFontName est défini sur null, la police **Times New Roman** sera utilisée.

Le code suivant montre comment définir un nom de police par défaut lors de l'enregistrement d'un PDF en image :

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
            // TODO Bloc à compléter en cas d'exception
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