---
title: حذف عنصر من القائمة
linktitle: حذف عنصر من القائمة
type: docs
weight: 20
url: /ar/java/del-list-item/
description: تعلم كيفية إزالة عنصر من حقل قائمة في مستند PDF باستخدام لغة جافا وواجهة `FormEditor` في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: حذف عنصر من قائمة في حقل نموذج PDF باستخدام جافا
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة عنصر معين من حقل القائمة، وحفظ المستند المحدث باستخدام واجهة `FormEditor` في Aspose.PDF for Java.
---
## حذف عنصر من حقل القائمة

1. ربط ملف PDF المصدر إلى `FormEditor` واجهة.
2. اتصال `delListItem(...)` للحقل الهدف والعنصر للإزالة.
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
