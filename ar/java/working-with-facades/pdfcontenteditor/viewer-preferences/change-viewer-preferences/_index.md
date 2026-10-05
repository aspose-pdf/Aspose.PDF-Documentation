---
title: تغيير تفضيلات العارض
linktitle: تغيير تفضيلات العارض
type: docs
weight: 20
url: /ar/java/change-viewer-preferences/
description: تعلم كيفية تغيير تفضيلات عارض مستند PDF بلغة Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تغيير تفضيلات عارض PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، تعديل قيمة تفضيل العارض الحالية، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## تغيير تفضيل العارض

1. اربط ملف PDF المصدر إلى واجهة `PdfContentEditor`.
2. اقرأ قيمة تفضيل المشاهد الحالية.
3. ادمجه مع العلامة الإضافية المطلوبة ومرّر النتيجة إلى `changeViewerPreference(...)`.
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
