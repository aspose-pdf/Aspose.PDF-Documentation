---
title: إضافة ختم مطاطي
linktitle: إضافة ختم مطاطي
type: docs
weight: 10
url: /ar/java/add-rubber-stamp/
description: تعرف على كيفية إضافة تعليق ختم مطاطي إلى مستند PDF بلغة Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إضافة ختم مطاطي إلى PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وإنشاء تعليق ختم مطاطي بنص التسمية واللون، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## إضافة ختم مطاطي

1. ربط ملف PDF المصدر بـ `PdfContentEditor` واجهة.
2. اتصال `createRubberStamp(...)` مع رقم الصفحة، المستطيل، العنوان، المحتويات، واللون.
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
