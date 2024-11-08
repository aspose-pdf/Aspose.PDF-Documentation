---
title: تعيين اسم الخط الافتراضي
linktitle: تعيين اسم الخط الافتراضي
type: docs
weight: 90
url: /ar/java/set-default-font-name/
description: يصف هذا القسم كيفية تعيين اسم الخط الافتراضي باستخدام مكتبة Aspose.PDF لـ Java.
lastmod: "2021-06-05"
---

تتيح لك واجهة برمجة التطبيقات **Aspose.PDF for Java** تعيين اسم الخط الافتراضي عندما لا يكون الخط متاحًا في المستند. يمكنك استخدام طريقة [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) من فئة [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) لتعيين اسم الخط الافتراضي. في حالة تعيين setDefaultFontName إلى null سيتم استخدام خط **Times New Roman**.

يُظهر مقتطف الشفرة التالي كيفية تعيين اسم الخط الافتراضي عند حفظ PDF كصورة:

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