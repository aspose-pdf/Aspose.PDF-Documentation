---
title: إزالة الإجراء الميداني
linktitle: إزالة الإجراء الميداني
type: docs
weight: 50
url: /java/remove-field-action/
description: تعرف على كيفية إزالة إجراء ميداني من حقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إزالة إجراء حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة الإجراء المرتبط بحقل معين، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## إزالة إجراء ميداني

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل بـ `removeFieldAction(...)` للحصول على الحقل الهدف.
3. احفظ المستند المحدث.

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
