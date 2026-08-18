---
title: استبدال النص بسيط
linktitle: استبدال النص بسيط
type: docs
weight: 10
url: /java/replace-text-simple/
description: تعرف على كيفية استبدال النص في مستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استبدال النص في ملف PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وتكوين نطاق استبدال النص، واستبدال كافة تكرارات النص المطابقة، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## استبدل النص في جميع أنحاء المستند

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. قم بتعيين نطاق استبدال النص إلى `ReplaceAll`.
3. اتصل `replaceText(...)` بنص البحث والنص البديل.
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
