---
title: إضافة عنصر القائمة
linktitle: إضافة عنصر القائمة
type: docs
weight: 10
url: /java/add-list-item/
description: تعرف على كيفية إضافة عناصر إلى حقل قائمة في مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إضافة عنصر قائمة إلى حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإضافة عنصر جديد إلى حقل قائمة وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## إضافة عنصر إلى حقل القائمة

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `addListItem(...)` للحصول على الحقل الهدف وزوج العرض/القيمة الجديد.
3. احفظ المستند المحدث.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
