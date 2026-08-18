---
title: قم بتعيين رقم مشط الحقل
linktitle: قم بتعيين رقم مشط الحقل
type: docs
weight: 60
url: /java/set-field-comb-number/
description: تعرف على كيفية تعيين رقم مشط لحقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتعيين رقم مشط لحقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين رقم مشط للحقل، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## قم بتعيين رقم مشط الحقل

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `setFieldCombNumber(...)` للحصول على الحقل الهدف وقيمة المشط.
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
