---
title: استبدال الصورة في ملف PDF موجود
linktitle: استبدال الصورة
type: docs
weight: 70
url: ar/java/replace-image-in-existing-pdf-file/
description: يصف هذا القسم كيفية استبدال الصورة في ملف PDF موجود باستخدام مكتبة Java.
lastmod: "2021-06-05"
---

تسمح لك طريقة [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) لمجموعة [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) باستبدال صورة في ملف PDF موجود.

يمكن العثور على مجموعة الصور في مجموعة الموارد لصفحة معينة. لاستبدال صورة:

1. افتح ملف PDF باستخدام كائن Document.
2. استبدل صورة معينة، ثم احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن Document.

يوضح لك مقطع الشيفرة التالي كيفية استبدال صورة في ملف PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // فتح المستند
        Document pdfDocument = new Document("input.pdf");
        // استبدال صورة معينة
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO معالجة كتلة catch
            e.printStackTrace();
        }
        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```