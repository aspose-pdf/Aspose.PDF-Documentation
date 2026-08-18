---
title: تعيين البرنامج النصي الميداني
linktitle: تعيين البرنامج النصي الميداني
type: docs
weight: 20
url: /java/set-field-script/
description: تعرف على كيفية تعيين إجراء JavaScript أو تحديثه في حقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتعيين إجراء JavaScript في حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإضافة برنامج نصي أولي واستبداله ببرنامج نصي محدث وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## قم بتعيين برنامج نصي ميداني

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. أضف إجراء JavaScript أوليًا إلى الحقل.
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
