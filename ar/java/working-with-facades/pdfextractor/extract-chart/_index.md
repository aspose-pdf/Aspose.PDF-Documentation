---
title: استخراج كائنات الرسم البياني من مستند PDF (واجهات)
type: docs
weight: 20
url: ar/java/extract-chart-objects/
description: يشرح هذا القسم كيفية استخراج كائنات الرسم البياني من PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج كائنات الرسم البياني من مستند PDF (واجهات)

يسمح PDF بتجميع محتوى الصفحة في عناصر تسمى **المحتوى المُعلّم**. يعرضها Adobe Acrobat كـ "حاويات". يتم وضع كائنات الرسم البياني في مثل هذه الكائنات. لقد قدمنا طريقة جديدة هي extractMarkedContentAsImages() في فئة PdfExtractor لاستخراج هذه الكائنات. تقوم هذه الطريقة بتحويل كل **محتوى مُعلّم** إلى صورة منفصلة. يرجى ملاحظة أن جميع الرسوم البيانية لا توضع بالكامل في حاوية واحدة. لهذا السبب سيتم حفظ بعض الرسوم البيانية في صور منفصلة على أجزاء.

يرجى ملاحظة أن التجميع الصحيح للمحتوى في حاويات هو مسؤولية مصمم مستند PDF.
 إذا كنت ترغب في الحصول على الرسومات البيانية مع العنوان أو الكائنات الأخرى، يجب عليك إما تعديل/إنشاء مستند PDF حيث يتم وضع الرسم البياني بالكامل في حاوية واحدة.

```java

// افتح المستند

Document document = new Document("sample.pdf");

// أنشئ PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

// استخراج كائنات الرسم البياني كصور في مجلد

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```