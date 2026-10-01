---
title: الوسائط المتعددة
linktitle: الوسائط المتعددة
type: docs
weight: 70
url: /ar/java/pdfcontenteditor-multimedia/
description: تعرف على التغطية الحالية للوسائط المتعددة المتاحة في واجهة Java PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تدفقات عمل تعليقات الوسائط المتعددة في Java مع PdfContentEditor
Abstract: يغطي هذا القسم تدفقات العمل المتعلقة بالوسائط المتعددة التي يدعمها حاليًا مجموعة أمثلة Java PdfContentEditor. يحتوي المستودع على مثال تعيين فيلم مباشر، بينما تُحتفظ بموضوعات الصوت غير المدعومة كملاحظات نطاق صريحة.
---
جافا الحالية `PdfContentEditorExamples` الفئة تدعم مباشرة `addMovieAnnotation(...)`.

## إضافة تعيين فيلم

1. ربط ملف PDF المصدر إلى `PdfContentEditor` واجهة.
2. اتصال `createMovie(...)` مع مستطيل التعليق التوضيحي ومسار ملف الفيديو ورقم الصفحة.
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
