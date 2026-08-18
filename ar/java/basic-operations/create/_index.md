---
title: إنشاء مستند PDF برمجياً
linktitle: إنشاء قوات الدفاع الشعبي
type: docs
weight: 10
url: /java/create-document/
description: تعرف على كيفية إنشاء مستند PDF من البداية في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملفات PDF باستخدام Aspose.PDF لجافا
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF في Java باستخدام Aspose.PDF. يقوم المثال بإنشاء كائن مستند جديد، وإضافة صفحة، وإدراج TextFragment مع نموذج نص، وحفظ النتيجة كملف PDF.
---
يعد إنشاء ملفات PDF في التعليمات البرمجية مطلبًا شائعًا للتقارير والفواتير ومستندات الأعمال التي تم إنشاؤها. يوفر Aspose.PDF for Java طريقة مباشرة لإنشاء مستند من البداية.

## كيفية إنشاء ملف PDF في جافا

لإنشاء مستند PDF برمجياً:

1. قم بإنشاء كائن [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أضف [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) إلى فقرات الصفحة.
1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) في ملف إخراج.

## إنشاء مستند PDF بسيط

يستند مثال Java التالي إلى `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
