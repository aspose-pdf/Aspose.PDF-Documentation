---
title: تعبئة حقول الباركود
linktitle: تعبئة حقول الباركود
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: تعرف على كيفية ملء حقل نموذج باركود في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بملء حقل الرمز الشريطي في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين قيمة حقل الرمز الشريطي، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.fillBarcodeFields(...)` لملء حقل الرمز الشريطي في نموذج PDF.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
