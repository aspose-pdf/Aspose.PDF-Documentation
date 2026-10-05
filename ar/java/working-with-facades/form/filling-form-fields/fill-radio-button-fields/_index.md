---
title: ملء حقول أزرار الراديو
linktitle: ملء حقول أزرار الراديو
type: docs
weight: 30
url: /ar/java/fill-radio-button-fields/
description: تعرف على كيفية تحديد قيمة زر الراديو في نموذج PDF باستخدام Java وواجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: حدد خيار حقل زر الراديو في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، واختيار خيار زر الراديو حسب الفهرس، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.fillRadioButtonFields(...)` لاختيار خيار زر الراديو.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
