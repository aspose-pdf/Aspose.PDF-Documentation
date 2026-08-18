---
title: تعيين البيانات التعريفية لملف PDF
linktitle: تعيين البيانات التعريفية لملف PDF
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: تعرف على كيفية تحديث بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث بيانات تعريف PDF باستخدام Aspose.PDF لـ Java
Abstract: تعرف على كيفية تحديث بيانات تعريف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileInfo لتعيين حقول البيانات التعريفية القياسية مثل الموضوع والعنوان والكلمات الأساسية والمنشئ، وإضافة إدخال بيانات تعريف مخصص، وحفظ النتيجة في ملف PDF جديد.
---
## تعيين البيانات التعريفية لملف PDF

استخدم سير العمل هذا عندما تحتاج إلى تسوية معلومات المستند أو إثرائها قبل حفظ ملف PDF.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لملف PDF المصدر.
2. قم بتعيين حقول البيانات التعريفية القياسية التي تريد تحديثها.
3. أضف أي بيانات تعريف مخصصة باستخدام `setMetaInfo`.
4. احفظ المستند المحدث باستخدام `save()`.
5. أغلق المثيل `PdfFileInfo`.

### مثال جافا

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
