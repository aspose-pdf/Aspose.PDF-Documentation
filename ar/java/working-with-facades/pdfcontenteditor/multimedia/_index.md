---
title: الوسائط المتعددة
linktitle: الوسائط المتعددة
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: تعرف على تغطية الوسائط المتعددة الحالية المتوفرة في واجهة Java PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: سير عمل التعليقات التوضيحية للوسائط المتعددة في Java باستخدام PdfContentEditor
Abstract: يغطي هذا القسم مهام سير العمل المتعلقة بالوسائط المتعددة والتي تدعمها حاليًا مجموعة أمثلة Java PdfContentEditor. يتضمن المستودع مثالًا مباشرًا لتعليق توضيحي للفيلم، بينما يتم الاحتفاظ بالموضوعات الصوتية غير المدعومة كملاحظات واضحة للنطاق.
---
فئة Java `PdfContentEditorExamples` الحالية تدعم مباشرة `addMovieAnnotation(...)`.

## إضافة تعليق توضيحي للفيلم

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل بـ`createMovie(...)` باستخدام مستطيل التعليقات التوضيحية ومسار ملف الفيلم ورقم الصفحة.
3. احفظ مستند PDF المحدث.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
