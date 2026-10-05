---
title: حذف عنصر من القائمة
linktitle: حذف عنصر من القائمة
type: docs
weight: 20
url: /ar/java/del-list-item/
description: تعلم كيفية إزالة عنصر من حقل قائمة في مستند PDF باستخدام لغة Java وواجهة `FormEditor` في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: حذف عنصر من قائمة في حقل نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة عنصر معين من حقل القائمة، وحفظ المستند المحدث باستخدام واجهة `FormEditor` في Aspose.PDF for Java.
---
## حذف عنصر من حقل القائمة

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. استدعِ `delListItem(...)` للحقل الهدف والعنصر للإزالة.
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
