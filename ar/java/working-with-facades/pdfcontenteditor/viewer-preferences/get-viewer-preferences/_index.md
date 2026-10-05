---
title: احصل على تفضيلات العارض
linktitle: احصل على تفضيلات العارض
type: docs
weight: 10
url: /ar/java/get-viewer-preferences/
description: تعرف على كيفية قراءة تفضيلات عارض مستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: قراءة تفضيلات عارض PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF وطباعة قيمة تفضيل العارض الحالي باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## احصل على تفضيل العارض الحالي

1. اربط ملف PDF المصدر بـ واجهة `PdfContentEditor`.
2. استدعِ `getViewerPreference()` لقراءة القيمة الحالية.
3. تحقّق أو اطبع علم التفضيل المرتجع.

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
