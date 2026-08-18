---
title: إنشاء مستند N-Up PDF
linktitle: إنشاء مستند N-Up PDF
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: قم بإنشاء تخطيط 2x2 N-Up PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء تخطيط N-Up PDF من مستند موجود في Java
Abstract: تعرف على كيفية إنشاء مستند N-Up PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لوضع أربع صفحات مصدر على كل ورقة إخراج ويعرض أيضًا متغير إرجاع منطقي للتحقق من الفشل.
---
## قم بإنشاء مستند N-Up PDF

يستخدم نموذج Java `PdfFileEditor.makeNUp` لإنشاء تخطيط 2x2 من ملف PDF موجود.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اتصل `makeNUp` بملف الإدخال وملف الإخراج وعدد الأعمدة والصفوف.
3. احفظ المستند الذي تم إنشاؤه.
4. إذا كنت تريد التحقق الصريح من النجاح، فاتصل بمتغير الإرجاع المنطقي وتعامل مع النتيجة `false`.

### مثال جافا

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
