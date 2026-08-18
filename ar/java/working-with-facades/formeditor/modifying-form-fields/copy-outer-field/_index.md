---
title: نسخ الحقل الخارجي
linktitle: نسخ الحقل الخارجي
type: docs
weight: 80
url: /java/copy-outer-field/
description: تعرف على كيفية نسخ حقل نموذج من مستند PDF إلى آخر في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: انسخ حقل نموذج PDF بين المستندات في Java
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF وجهة، وربطه بواجهة FormEditor، ونسخ حقل من مستند آخر، وحفظ النتيجة باستخدام Aspose.PDF لـ Java.
---
## انسخ حقلاً من ملف PDF آخر

1. قم بإنشاء ملف PDF وجهة يحتوي على صفحة واحدة على الأقل.
2. قم بربط ملف PDF الوجهة بالواجهة `FormEditor`.
3. اتصل بـ `copyOuterField(...)` مع تحديد مسار المستند المصدر واسم الحقل والصفحة المستهدفة والإحداثيات.
4. احفظ مستند الوجهة المحدث.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
