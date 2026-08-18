---
title: حذف عنصر القائمة
linktitle: حذف عنصر القائمة
type: docs
weight: 20
url: /java/del-list-item/
description: تعرف على كيفية إزالة عنصر من حقل قائمة في مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: حذف عنصر قائمة من حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة عنصر معين من حقل قائمة، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## حذف عنصر من حقل القائمة

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `delListItem(...)` للحصول على الحقل الهدف والعنصر المطلوب إزالته.
3. احفظ المستند المحدث.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
