---
title: قائمة الطوابع
linktitle: قائمة الطوابع
type: docs
weight: 20
url: /java/list-stamps/
description: تعرف على كيفية إدراج الطوابع المطاطية على صفحة في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قائمة الطوابع المطاطية PDF في جافا
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، واسترداد الطوابع على الصفحة، وفحص المجموعة الناتجة باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## قائمة الطوابع على الصفحة

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل بـ `getStamps(pageNumber)` لاسترداد الطوابع الموجودة على الصفحة المستهدفة.
3. افحص المجموعة `StampInfo[]` الناتجة.

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
