---
title: ملء حقول زر الاختيار
linktitle: ملء حقول زر الاختيار
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: تعرف على كيفية تحديد قيمة زر الاختيار في نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: حدد خيار حقل زر الاختيار في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتحديد خيار زر الاختيار حسب الفهرس، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.fillRadioButtonFields(...)` لتحديد خيار زر الاختيار.

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
