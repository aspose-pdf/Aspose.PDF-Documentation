---
title: استخراج الخطوط من PDF 
linktitle: استخراج الخطوط
type: docs
weight: 30
url: ar/java/extract-fonts-from-pdf/
description: كيفية استخراج الخطوط من ملف PDF باستخدام Aspose.PDF لـ Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حال كنت ترغب في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام الطريقة `Document.IDocumentFontUtilities.getAllFonts()` المقدمة في فئة Document. يرجى التحقق من مقطع الشيفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // المسار إلى دليل المستندات.
    String filePath = "<... أدخل اسم الملف ...>";
    
    // تحميل مستند PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```