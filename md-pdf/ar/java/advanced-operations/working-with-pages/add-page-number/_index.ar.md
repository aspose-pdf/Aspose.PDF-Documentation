---
title: إضافة رقم الصفحة إلى ملف PDF
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: /java/add-page-number/
description: Aspose.PDF for Java يسمح لك بإضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumberStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يجب أن تحتوي جميع الوثائق على أرقام صفحات. يسهل رقم الصفحة على القارئ تحديد أجزاء مختلفة من الوثيقة.
**Aspose.PDF for Java** يسمح لك بإضافة أرقام الصفحات باستخدام PageNumberStamp.

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت من خلال هذا الرابط [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

يمكنك استخدام [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) لإضافة ختم رقم الصفحة في مستند PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) توفر فئة طرق لإنشاء ختم بناءً على رقم الصفحة مثل التنسيق، الهوامش، المحاذاة، الرقم المبدئي وغيرها. لإضافة ختم رقم الصفحة، تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وكائن [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) بالخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) لفئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) لإضافة الختم في ملف PDF. يمكنك أيضًا تعيين خصائص الخط لختم رقم الصفحة.

يُظهر لك مقطع الشيفرة التالي كيفية إضافة أرقام الصفحات في ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // افتح المستند
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

        // أضف الختم إلى الصفحة المحددة
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // حفظ المستند الناتج
        pdfDocument.save(_dataDir);

    }
}
```