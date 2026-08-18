---
title: إعادة تسمية الحقل
linktitle: إعادة تسمية الحقل
type: docs
weight: 50
url: /java/rename-field/
description: تعرف على كيفية إعادة تسمية حقل نموذج موجود في مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إعادة تسمية حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإعادة تسمية حقل محدد وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## إعادة تسمية حقل

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `renameField(...)` باستخدام اسم الحقل الحالي واسم الحقل الجديد.
3. احفظ المستند المحدث.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
