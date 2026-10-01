---
title: قائمة الطوابع
linktitle: قائمة الطوابع
type: docs
weight: 20
url: /ar/java/list-stamps/
description: تعرف على كيفية سرد الطوابع المطاطية على صفحة في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: سرد طوابع PDF المطاطية في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، استرجاع الطوابع على صفحة، وفحص المجموعة الناتجة باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## سرد الطوابع على صفحة

1. ربط ملف PDF المصدر بـ `PdfContentEditor` الواجهة.
2. اتصال `getStamps(pageNumber)` لاسترجاع الطوابع على الصفحة المستهدفة.
3. افحص الناتج `StampInfo[]` مجموعة.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
