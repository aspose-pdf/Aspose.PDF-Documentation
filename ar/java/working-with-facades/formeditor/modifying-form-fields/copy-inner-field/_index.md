---
title: نسخ الحقل الداخلي
linktitle: نسخ الحقل الداخلي
type: docs
weight: 70
url: /ar/java/copy-inner-field/
description: تعلم كيفية نسخ حقل نموذج إلى موقع جديد داخل نفس مستند PDF بلغة Java باستخدام الواجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: نسخ حقل نموذج PDF داخل نفس المستند بلغة Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتكرار حقل إلى صفحة وموقع آخرين، وحفظ المستند المحدث باستخدام الواجهة FormEditor في Aspose.PDF for Java.
---
## نسخ حقل داخل نفس ملف PDF

1. اربط PDF المصدر إلى `FormEditor` الواجهة.
2. اتصال `copyInnerField(...)` مع اسم الحقل المصدر، اسم الحقل الجديد، الصفحة، والإحداثيات.
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
