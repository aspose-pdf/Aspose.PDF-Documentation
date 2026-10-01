---
title: عمليات الصور
linktitle: عمليات الصور
type: docs
weight: 50
url: /ar/java/pdfcontenteditor-image-operations/
description: تعرف على تغطية عمليات الصور الحالية في جافا المتوفرة عبر واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: سير عمل تحرير الصور في جافا باستخدام PdfContentEditor
Abstract: يغطي هذا القسم سير العمل المتعلق بالصور الذي يدعمه حاليًا مجموعة أمثلة PdfContentEditor لجافا. يحتوي المستودع على مثال مباشر لاستبدال صورة، بينما يتم الاحتفاظ بمواضيع حذف الصور غير المدعومة كملاحظات نطاق صريحة.
---
Java الحالية `PdfContentEditorExamples` الفئة تدعم مباشرة `replaceImage(...)`.

## استبدال صورة

1. ربط ملف PDF المصدر بـ `PdfContentEditor` واجهة.
2. اتصال `replaceImage(...)` مع رقم الصفحة، فهرس الصورة، ومسار صورة الاستبدال.
3. احفظ مستند PDF المحدث.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
