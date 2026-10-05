---
title: إنشاء مستند PDF بنمط N-Up
linktitle: إنشاء مستند PDF بنمط N-Up
type: docs
weight: 10
url: /ar/java/create-n-up-pdf-document/
description: إنشاء تخطيط PDF بنمط N-Up 2x2 في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء تخطيط PDF بنمط N-Up من وثيقة موجودة في Java
Abstract: تعرف على كيفية إنشاء مستند PDF بنمط N-Up باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileEditor لوضع أربع صفحات مصدر على كل ورقة إخراج ويظهر أيضًا نسخة تُعيد قيمة منطقية للتحقق من الفشل.
---
## إنشاء مستند PDF بنمط N-Up

عينة Java تستخدم `PdfFileEditor.makeNUp` لبناء تخطيط 2x2 من ملف PDF موجود.

### خطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. استدعِ `makeNUp` مع ملف الإدخال، ملف الإخراج، وعدد الأعمدة والصفوف.
3. احفظ المستند المُولَّد.
4. إذا كنت تريد التحقق الصريح من النجاح، استدع النسخة التي تُعيد قيمة منطقية وتتعامل مع `false` نتيجة.

### مثال Java

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
