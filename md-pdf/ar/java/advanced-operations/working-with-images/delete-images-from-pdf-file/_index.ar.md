---
title: حذف الصور من ملف PDF
linktitle: حذف الصور
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
---

لحذف صورة من ملف PDF، استخدم ببساطة طريقة الحذف (delete(..)) في مجموعة الصور.

1. قم بإنشاء كائن Document وافتح ملف PDF المدخل.
2. احصل على الصفحة التي تحتوي على الصورة من مجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
3. تُحفظ الصور في مجموعة الصور الموجودة في مجموعة [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) الخاصة بالصفحة.
4. احذف صورة باستخدام طريقة Delete في مجموعة الصور.
5. احفظ الناتج باستخدام طريقة Save الخاصة بكائن Document.

يوضح مقطع الشيفرة البرمجية التالي كيفية حذف صورة من ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // إنشاء ختم رقم الصفحة
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // ما إذا كان الختم في الخلفية
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // تعيين خصائص النص
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // إضافة ختم إلى صفحة معينة
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // حفظ المستند الناتج
        pdfDocument.save(_dataDir);

    }
}
```