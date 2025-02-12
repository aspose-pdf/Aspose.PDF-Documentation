---
title: Set Default Font Name
linktitle: Set Default Font Name
type: docs
weight: 90
url: /java/set-default-font-name/
description: This section describes how to set default font name using Aspose.PDF for Java library.
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: How to set default font name using Aspose.PDF for Java
Abstract: The article provides an overview of using the Aspose.PDF for Java API to set a default font name for PDF documents when converting them into images. It highlights the `setDefaultFontName` method from the `RenderingOptions` class, which allows users to specify a default font to be used when the original font is unavailable. If no default font is specified (i.e., set to null), the system defaults to using "Times New Roman." The article includes a Java code snippet demonstrating how to apply this feature - it outlines the process of loading a PDF document, setting the default font to "Arial," and converting a page of the PDF into a PNG image using a `PngDevice` with specified rendering options. The code ensures that even if a font is missing in the original PDF, the output image maintains consistent font rendering.
SoftwareApplication: java
---

**Aspose.PDF for Java** API allows you to set a default font name when a font is not available in the document. You can use [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) method of [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) class to set the default font name. In case setDefaultFontName is set to null the **Times New Roman** font will be used. 

The following code snippet shows how to set a default font name when saving PDF into an image:

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
