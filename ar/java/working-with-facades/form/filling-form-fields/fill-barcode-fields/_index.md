---
title: ملء حقول الباركود
linktitle: ملء حقول الباركود
type: docs
weight: 50
url: /ar/java/fill-barcode-fields/
description: تعلم كيفية ملء حقل نموذج الباركود في Java باستخدام الواجهة Form في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: ملء حقل الباركود في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين قيمة حقل الباركود، وحفظ المستند المحدث باستخدام الواجهة Form في Aspose.PDF for Java.
---
استخدم `FormExamples.fillBarcodeFields(...)` لملء حقل الباركود في نموذج PDF.

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
