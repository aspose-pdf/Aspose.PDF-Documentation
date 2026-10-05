---
title: نسخ الحقل الخارجي
linktitle: نسخ الحقل الخارجي
type: docs
weight: 80
url: /ar/java/copy-outer-field/
description: تعلم كيفية نسخ حقل نموذج من مستند PDF إلى آخر في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: نسخ حقل نموذج PDF بين المستندات في Java
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF مقصد، وربطها بواجهة FormEditor، ونسخ حقل من مستند آخر، وحفظ النتيجة باستخدام Aspose.PDF for Java.
---
## نسخ حقل من PDF آخر

1. أنشئ ملف PDF مقصد يحتوي على صفحة واحدة على الأقل.
2. اربط ملف PDF الوجهة بـ واجهة `FormEditor`.
3. استدعِ `copyOuterField(...)` مع مسار المستند المصدر، اسم الحقل، الصفحة المستهدفة، والإحداثيات.
4. احفظ المستند الوجهة المحدث.

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
