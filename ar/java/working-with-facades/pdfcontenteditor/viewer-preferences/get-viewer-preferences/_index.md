---
title: الحصول على تفضيلات المشاهد
linktitle: الحصول على تفضيلات المشاهد
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: تعرف على كيفية قراءة تفضيلات العارض لمستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قراءة تفضيلات عارض PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF وطباعة قيمة تفضيلات العارض الحالية باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## احصل على تفضيلات العارض الحالية

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل `getViewerPreference()` لقراءة القيمة الحالية.
3. قم بفحص أو طباعة علامة التفضيل التي تم إرجاعها.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
