---
title: استبدال النص بالحالة
linktitle: استبدال النص بالحالة
type: docs
weight: 20
url: /ar/java/replace-text-with-state/
description: تعرف على كيفية استبدال النص بتنسيق مخصص في Java باستخدام الواجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: استبدال نص PDF بتنسيق مخصص في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وتكوين TextState مخصص، واستبدال جميع مرات ظهور النص المطابق، وحفظ المستند المحدث باستخدام الواجهة PdfContentEditor في Aspose.PDF for Java.
---
## استبدال النص بحالة نص مخصصة

1. ربط ملف PDF المصدر بـ `PdfContentEditor` واجهة.
2. إنشاء وتكوين `TextState` مع اللون وحجم الخط المطلوبين.
3. حدد نطاق استبدال النص إلى `ReplaceAll`.
4. اتصال `replaceText(...)` مع نص البحث، نص الاستبدال، والمكوّن `TextState`.
5. حفظ مستند PDF المحدث.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
