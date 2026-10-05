---
title: تغيير حجم محتويات صفحة PDF
linktitle: تغيير حجم محتويات صفحة PDF
type: docs
weight: 30
url: /ar/java/resize-pdf-page-contents/
description: تغيير حجم المحتوى على صفحات PDF المحددة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغيير حجم محتويات الصفحة الموجودة في مستند PDF باستخدام Java
Abstract: تعرّف على كيفية تغيير حجم محتويات الصفحات باستخدام Aspose.PDF for Java. يستخدم مثال Java PdfFileEditor لاستهداف صفحات محددة، وتطبيق عرض وارتفاع جديد للمحتوى، وإيقاف سير العمل إذا فشلت عملية تغيير الحجم.
---
## تغيير حجم محتويات صفحة PDF

عينة Java تغير حجم منطقة المحتوى في الصفحات 1 و 3 وتتحقق من قيمة الإرجاع المنطقية.

### الخطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. اختر الصفحات التي يجب تغيير حجم محتواها.
3. استدعِ `resizeContents` مع العرض والارتفاع المستهدفين.
4. تحقّق من قيمة الإرجاع وتعامل مع الفشل قبل المتابعة.
5. احفظ المستند المحدث.

### مثال Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
