---
title: حذف الصفحات من PDF
linktitle: حذف الصفحات من PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: احذف الصفحات المحددة من ملف PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة صفحات معينة من مستند PDF باستخدام Java
Abstract: تعرف على كيفية حذف الصفحات من ملف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لإزالة مجموعة محددة من أرقام الصفحات وحفظ الصفحات المتبقية كمستند جديد.
---
## حذف صفحات من ملف PDF

يقوم نموذج Java بإزالة الصفحتين 2 و4 من المستند المصدر.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. أنشئ مصفوفة تحتوي على أرقام الصفحات المطلوب إزالتها.
3. اتصل `delete` باستخدام ملف الإدخال ومصفوفة الصفحات وملف الإخراج.
4. احفظ ملف PDF الناتج.

### مثال جافا

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
