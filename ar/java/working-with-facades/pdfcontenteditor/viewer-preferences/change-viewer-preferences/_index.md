---
title: تغيير تفضيلات المشاهد
linktitle: تغيير تفضيلات المشاهد
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: تعرف على كيفية تغيير تفضيلات العارض لمستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تغيير تفضيلات عارض PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وتعديل قيمة تفضيلات العارض الحالية، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## تغيير تفضيلات المشاهد

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اقرأ قيمة تفضيلات العارض الحالية.
3. قم بدمجها مع العلامة الإضافية المطلوبة وقم بتمرير النتيجة إلى `changeViewerPreference(...)`.
4. احفظ مستند PDF المحدث.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
