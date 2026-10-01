---
title: إنشاء مستند PDF برمجيًا
linktitle: إنشاء PDF
type: docs
weight: 10
url: /ar/java/create-document/
description: تعلم كيفية إنشاء مستند PDF من الصفر في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملفات PDF باستخدام Aspose.PDF for Java
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF في Java باستخدام Aspose.PDF. يقوم المثال بإنشاء كائن Document جديد، يضيف صفحة، يدرج TextFragment بنص تجريبي، ويحفظ النتيجة كملف PDF.
---
إنشاء ملفات PDF في الكود هو مطلب شائع للتقارير والفواتير والوثائق التجارية المولدة. يوفر Aspose.PDF for Java طريقة مباشرة لبناء مستند من الصفر.

## كيفية إنشاء ملف PDF في Java

لإنشاء مستند PDF برمجيًا:

1. إنشاء [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كائن.
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إضافة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) إلى فقرات الصفحة.
1. احفظ الـ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى ملف إخراج.

## إنشاء مستند PDF بسيط

المثال التالي بلغة Java يعتمد على `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
