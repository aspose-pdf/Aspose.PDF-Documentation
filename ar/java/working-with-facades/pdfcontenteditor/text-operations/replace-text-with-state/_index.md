---
title: استبدال النص بالحالة
linktitle: استبدال النص بالحالة
type: docs
weight: 20
url: /java/replace-text-with-state/
description: تعرف على كيفية استبدال النص بتنسيق مخصص في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استبدل نص PDF بالتنسيق المخصص في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وتكوين حالة TextState مخصصة، واستبدال كافة تكرارات النص المطابقة، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## استبدل النص بحالة نصية مخصصة

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. قم بإنشاء وتكوين `TextState` باللون وحجم الخط المطلوبين.
3. قم بتعيين نطاق استبدال النص إلى `ReplaceAll`.
4. اتصل بـ`replaceText(...)` باستخدام نص البحث والنص البديل وقم بتكوين `TextState`.
5. احفظ مستند PDF المحدث.

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
