---
title: تعيين رقم الكمب للحقل
linktitle: تعيين رقم الكمب للحقل
type: docs
weight: 60
url: /ar/java/set-field-comb-number/
description: تعرّف على كيفية تعيين رقم الكمب لحقل نموذج PDF في Java باستخدام الواجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تعيين رقم الكمب لحقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين رقم الكمب لحقل، وحفظ المستند المحدث باستخدام الواجهة FormEditor في Aspose.PDF for Java.
---
## تعيين رقم الكمب لحقل

1. اربط ملف PDF المصدر بـ `FormEditor` الواجهة.
2. استدعِ `setFieldCombNumber(...)` للحقل المستهدف وقيمة comb..
3. احفظ المستند المحدث.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
