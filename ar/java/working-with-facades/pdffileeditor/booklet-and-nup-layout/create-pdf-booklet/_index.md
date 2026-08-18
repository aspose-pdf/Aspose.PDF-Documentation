---
title: إنشاء كتيب PDF
linktitle: إنشاء كتيب PDF
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: قم بإنشاء ملف PDF جاهز للكتيبات من مستند موجود في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء إخراج كتيب من مستند PDF في Java
Abstract: تعرف على كيفية إنشاء كتيب PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لإعادة ترتيب الصفحات لطباعة الكتيبات ويتضمن أيضًا متغير إرجاع منطقي للتحقق من النجاح البسيط.
---
## إنشاء كتيب PDF

استخدم `PdfFileEditor.makeBooklet` لإعادة ترتيب صفحات ملف PDF موجود في ترتيب كتيب.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اتصل بـ `makeBooklet` باستخدام ملف PDF المصدر وملف الإخراج.
3. احفظ مستند الكتيب.
4. إذا كنت تريد التحقق من حالة الإرجاع، فاستخدم متغير الإرجاع المنطقي وتعامل مع النتيجة الفاشلة.

### مثال جافا

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
