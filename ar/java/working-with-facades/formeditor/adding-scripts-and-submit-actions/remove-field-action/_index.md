---
title: إزالة إجراء الحقل
linktitle: إزالة إجراء الحقل
type: docs
weight: 50
url: /ar/java/remove-field-action/
description: تعلم كيفية إزالة إجراء حقل من حقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إزالة إجراء حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة الإجراء المرتبط بحقل محدد، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## إزالة إجراء حقل

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. استدعِ `removeFieldAction(...)` للحقل المستهدف.
3. احفظ المستند المحدّث.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
