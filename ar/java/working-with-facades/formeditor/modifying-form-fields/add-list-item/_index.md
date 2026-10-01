---
title: إضافة عنصر إلى القائمة
linktitle: إضافة عنصر إلى القائمة
type: docs
weight: 10
url: /ar/java/add-list-item/
description: تعرف على كيفية إضافة عناصر إلى حقل قائمة في مستند PDF باستخدام Java عبر واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إضافة عنصر إلى حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة عنصر جديد إلى حقل قائمة، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## إضافة عنصر إلى حقل القائمة

1. اربط ملف PDF المصدر بـ `FormEditor` واجهة.
2. اتصال `addListItem(...)` للحقل المستهدف وزوج العرض/القيمة الجديد.
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
