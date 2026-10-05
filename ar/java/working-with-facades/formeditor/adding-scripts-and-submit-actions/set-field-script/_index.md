---
title: ضبط سكريبت الحقل
linktitle: ضبط سكريبت الحقل
type: docs
weight: 20
url: /ar/java/set-field-script/
description: تعرف على كيفية تعيين أو تحديث إجراء JavaScript على حقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تعيين إجراء JavaScript على حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط PDF موجود، إضافة سكريبت أولي، استبداله بسكريبت محدث، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## ضبط سكريبت حقل

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. أضف إجراء JavaScript أولي إلى الحقل.
3. استبدله بنص البرنامج النصي المحدث.
4. احفظ المستند المحدث.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
