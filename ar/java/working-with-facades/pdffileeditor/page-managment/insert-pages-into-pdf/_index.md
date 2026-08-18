---
title: إدراج الصفحات في PDF
linktitle: إدراج الصفحات في PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: قم بإدراج الصفحات المحددة من ملف PDF إلى آخر في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإدراج صفحات من ملف PDF آخر في الموضع المختار باستخدام Java
Abstract: تعرف على كيفية إدراج صفحات في ملف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لإدراج صفحات محددة من مستند ثانٍ بعد رقم صفحة معين في ملف PDF المستهدف.
---
## إدراج صفحات في ملف PDF

يقوم نموذج Java بإدراج الصفحتين 1 و2 من المستند الثانوي بعد الصفحة 2 من ملف PDF المستهدف.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اختر نقطة الإدراج في المستند الهدف.
3. حدد أرقام الصفحات المراد نسخها من المستند المصدر.
4. اتصل `insert` باستخدام الملف الهدف ونقطة الإدراج والملف المصدر ومصفوفة الصفحات وملف الإخراج.
5. احفظ ملف PDF المحدث.

### مثال جافا

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
