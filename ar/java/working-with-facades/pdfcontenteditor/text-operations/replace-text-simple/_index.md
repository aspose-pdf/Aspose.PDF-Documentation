---
title: استبدال النص بسيط
linktitle: استبدال النص بسيط
type: docs
weight: 10
url: /ar/java/replace-text-simple/
description: تعلّم كيفية استبدال النص في مستند PDF بالكامل باستخدام Java من خلال واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: استبدال النص في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وتكوين نطاق استبدال النص، واستبدال جميع حالات النص المطابقة، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## استبدال النص في جميع أنحاء المستند

1. اربط ملف PDF المصدر بـ واجهة `PdfContentEditor`.
2. حدّد نطاق استبدال النص إلى `ReplaceAll`.
3. استدعِ `replaceText(...)` مع نص البحث ونص الاستبدال.
4. احفظ مستند PDF المحدث.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
