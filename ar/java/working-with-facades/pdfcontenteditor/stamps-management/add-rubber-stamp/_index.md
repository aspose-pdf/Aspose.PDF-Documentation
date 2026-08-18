---
title: إضافة ختم مطاطي
linktitle: إضافة ختم مطاطي
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: تعرف على كيفية إضافة تعليق توضيحي بختم مطاطي إلى مستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: أضف ختمًا مطاطيًا إلى ملف PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وإنشاء تعليق توضيحي بختم مطاطي مع نص التسمية واللون، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## أضف ختمًا مطاطيًا

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل `createRubberStamp(...)` برقم الصفحة والمستطيل والعنوان والمحتويات واللون.
3. احفظ مستند PDF المحدث.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
