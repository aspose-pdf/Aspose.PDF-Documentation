---
title: إنشاء صور مصغرة من مستندات PDF
linktitle: إنشاء صور مصغرة
type: docs
weight: 100
url: /ar/java/generate-thumbnail-images-from-pdf-documents/
description: يصف هذا القسم كيفية إنشاء صور مصغرة من مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
---

## نهج Aspose.PDF لـ Java

يوفر Aspose.PDF لـ Java دعمًا واسعًا للتعامل مع مستندات PDF. كما يدعم القدرة على تحويل صفحات مستندات PDF إلى مجموعة متنوعة من تنسيقات الصور. يمكن تحقيق الوظيفة الموصوفة أعلاه بسهولة باستخدام Aspose.PDF لـ Java.

لـ Aspose.PDF فوائد مميزة:

- لا تحتاج إلى تثبيت Adobe Acrobat على نظامك للعمل مع ملفات PDF.
- استخدام Aspose.PDF لـ Java بسيط وسهل الفهم مقارنة بـ Acrobat Automation.

إذا كنا بحاجة لتحويل صفحات PDF إلى JPEGs، فإن مساحة الأسماء [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) توفر فئة تسمى [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) لعرض صفحات PDF كصور JPEG.
 يرجى إلقاء نظرة على مقطع الشيفرة التالي.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // استرجاع أسماء جميع ملفات PDF في دليل معين
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // خطأ أثناء قراءة الدليل
        }

        // التكرار عبر جميع إدخالات الملفات في المصفوفة
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // فتح المستند
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // إنشاء كائن Resolution
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // تحويل صفحة معينة وحفظ الصورة إلى التدفق
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // إغلاق التدفق
                imageStream.close();
            }
        }

    }
}
```