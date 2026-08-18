---
title: عمليات الصورة
linktitle: عمليات الصورة
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: تعرف على التغطية الحالية لعملية صورة Java المتوفرة في واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: سير عمل تحرير الصور في Java باستخدام PdfContentEditor
Abstract: يغطي هذا القسم عمليات سير العمل المتعلقة بالصور التي تدعمها حاليًا مجموعة أمثلة Java PdfContentEditor. يتضمن المستودع مثالًا مباشرًا لاستبدال صورة، بينما يتم الاحتفاظ بموضوعات حذف الصور غير المدعومة كملاحظات واضحة للنطاق.
---
فئة Java `PdfContentEditorExamples` الحالية تدعم مباشرة `replaceImage(...)`.

## استبدال صورة

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل `replaceImage(...)` برقم الصفحة وفهرس الصورة ومسار الصورة البديلة.
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
