---
title: استخراج المرفقات من ملف PDF
type: docs
weight: 10
url: ar/java/extract-attachments/
description: يشرح هذا القسم كيفية استخراج المرفقات من pdf باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

إحدى الفئات الرئيسية تحت قدرات الاستخراج في [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) هي استخراج المرفقات.
 هذه الفئة توفر مجموعة من الأساليب، التي لا تساعد فقط في استخراج المرفقات بل توفر أيضًا الأساليب التي يمكن أن تعطيك معلومات متعلقة بالمرفقات مثل طرق [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) و[GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) التي تقدم معلومات عن المرفقات واسم المرفق على التوالي. من أجل استخراج ثم الحصول على المرفقات نستخدم طرق [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) و[GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--).

يوضح لك مقتطف الشفرة التالي كيفية استخدام أساليب PdfExtractor:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // استخراج المرفقات
        pdfExtractor.extractAttachment();

        // الحصول على أسماء المرفقات
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("استخراج وتخزين...");
            // الحصول على المرفقات المستخرجة
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```