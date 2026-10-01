---
title: تعيين بيانات تعريف PDF
linktitle: تعيين بيانات تعريف PDF
type: docs
weight: 50
url: /ar/java/set-pdf-metadata/
description: تعلم كيفية تحديث بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث بيانات تعريف PDF باستخدام Aspose.PDF for Java
Abstract: تعلم كيفية تحديث بيانات تعريف PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileInfo لتعيين حقول البيانات التعريفية القياسية مثل الموضوع، العنوان، الكلمات المفتاحية، والإنشاء، ويضيف إدخال بيانات تعريف مخصص، ويحفظ النتيجة في ملف PDF جديد.
---
## تعيين بيانات تعريف PDF

استخدم هذا سير العمل عندما تحتاج إلى تطبيع أو إثراء معلومات المستند قبل حفظ ملف PDF.

### خطوات

1. إنشاء `PdfFileInfo` كائن لملف PDF المصدر.
2. تعيين حقول البيانات الوصفية القياسية التي تريد تحديثها.
3. أضف أي بيانات تعريف مخصصة باستخدام `setMetaInfo`.
4. احفظ المستند المحدث باستخدام `save()`.
5. أغلق الـ `PdfFileInfo` مثيل.

### مثال Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
