---
title: نسخ الحقل الداخلي
linktitle: نسخ الحقل الداخلي
type: docs
weight: 70
url: /java/copy-inner-field/
description: تعرف على كيفية نسخ حقل نموذج إلى موضع جديد داخل نفس مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: انسخ حقل نموذج PDF داخل نفس المستند في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتكرار حقل إلى صفحة وموضع آخر، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## انسخ حقلاً داخل نفس ملف PDF

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `copyInnerField(...)` باسم الحقل المصدر واسم الحقل الجديد والصفحة والإحداثيات.
3. احفظ المستند المحدث.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
