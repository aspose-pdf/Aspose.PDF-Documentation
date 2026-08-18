---
title: تغيير حجم محتويات صفحة PDF
linktitle: تغيير حجم محتويات صفحة PDF
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: قم بتغيير حجم المحتوى على صفحات PDF محددة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتغيير حجم محتويات الصفحة الموجودة في مستند PDF باستخدام Java
Abstract: تعرف على كيفية تغيير حجم محتويات الصفحة باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لاستهداف صفحات محددة، وتطبيق عرض وارتفاع محتوى جديد، وإيقاف سير العمل في حالة فشل عملية تغيير الحجم.
---
## تغيير حجم محتويات صفحة PDF

يقوم نموذج Java بتغيير حجم منطقة المحتوى في الصفحتين 1 و3 والتحقق من قيمة الإرجاع المنطقية.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اختر الصفحات التي يجب تغيير حجم محتواها.
3. اتصل `resizeContents` بالعرض والارتفاع المستهدفين.
4. تحقق من قيمة الإرجاع وقم بمعالجة الفشل قبل المتابعة.
5. احفظ المستند المحدث.

### مثال جافا

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
