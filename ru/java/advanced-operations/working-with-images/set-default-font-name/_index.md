---
title: Установить Имя Шрифта По Умолчанию
linktitle: Установить Имя Шрифта По Умолчанию
type: docs
weight: 90
url: /ru/java/set-default-font-name/
description: Этот раздел описывает, как установить имя шрифта по умолчанию, используя библиотеку Aspose.PDF для Java.
lastmod: "2021-06-05"
---

API **Aspose.PDF for Java** позволяет установить имя шрифта по умолчанию, если шрифт недоступен в документе. Вы можете использовать метод [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) класса [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions), чтобы установить имя шрифта по умолчанию. Если setDefaultFontName установлен в null, будет использоваться шрифт **Times New Roman**.

Следующий фрагмент кода показывает, как установить имя шрифта по умолчанию при сохранении PDF в изображение:

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
            // TODO Автоматически созданный блок catch
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