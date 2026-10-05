---
title: إنشاء كتيب PDF
linktitle: إنشاء كتيب PDF
type: docs
weight: 20
url: /ar/java/create-pdf-booklet/
description: إنشاء ملف PDF جاهز للكتيب من مستند موجود بلغة Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء مخرجات كتيب من مستند PDF في Java
Abstract: تعلم كيفية إنشاء كتيب PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileEditor لإعادة ترتيب الصفحات لطباعة الكتيب ويتضمن أيضًا متغيرًا يُعيد قيمة منطقية للتحقق البسيط من النجاح.
---
## إنشاء كتيب PDF

استخدام `PdfFileEditor.makeBooklet` لإعادة ترتيب صفحات PDF موجود إلى ترتيب كتيب.

### خطوات

1. أنشئ مثيلًا `PdfFileEditor`.
2. استدعِ `makeBooklet` مع ملف PDF المصدر وملف الإخراج.
3. احفظ مستند الكتيب.
4. إذا كنت تريد التحقق من حالة الإرجاع، استخدم النسخة التي تُعيد قيمة منطقية وتعامل مع النتيجة الفاشلة.

### مثال Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
