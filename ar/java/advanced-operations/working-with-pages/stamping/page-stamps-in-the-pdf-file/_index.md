---
title: إضافة ختم صفحة PDF إلى ملف PDF
linktitle: الأختام في ملف PDF
type: docs
weight: 30
url: ar/java/page-stamps-in-the-pdf-file/
description: إضافة ختم صفحة إلى ملف PDF باستخدام فئة PdfPageStamp مع جافا.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة ختم صفحة باستخدام جافا

يمكن استخدام [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) عندما تحتاج إلى تطبيق ختم مركب يحتوي على رسومات ونصوص وجداول. يوضح المثال التالي كيفية استخدام ختم لإنشاء أدوات مكتبية كما هو الحال في استخدام Adobe InDesign، Illustrator، Microsoft Word. افترض أن لدينا بعض الوثائق المدخلة ونريد تطبيق نوعين من الحدود باللون الأزرق ولون البرقوق.

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    // إنشاء ختم صفحة باللون الأزرق
    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    // إنشاء ختم صفحة بلون البرقوق
    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        // إضافة ختم الصفحة بناءً على موضع الصفحة
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    // حفظ المستند
    document.save(_dataDir + outputFileName);
}
```