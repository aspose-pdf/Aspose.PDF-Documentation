---
title: حفظ البيانات الوصفية باستخدام XMP
linktitle: حفظ البيانات الوصفية باستخدام XMP
type: docs
weight: 30
url: /ar/java/save-metadata-with-xmp/
description: تعرف على كيفية حفظ البيانات الوصفية لملف PDF باستخدام XMP في Java عبر واجهة PdfFileInfo.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ البيانات الوصفية لملف PDF باستخدام XMP مع Aspose.PDF for Java
Abstract: تعرف على كيفية حفظ البيانات الوصفية لملف PDF باستخدام XMP عبر Aspose.PDF for Java. يقوم مثال Java بتحديث حقول البيانات الوصفية الأساسية باستخدام PdfFileInfo ويعيد كتابتها باستخدام `saveNewInfoWithXmp()` بحيث يخزن المستند الناتج المعلومات بصيغة XMP.
---
## حفظ البيانات الوصفية باستخدام XMP

استخدم هذا التدفق عندما تحتاج إلى تخزين معلومات المستند المحدثة بصيغة XMP.

### خطوات

1. أنشئ كائن `PdfFileInfo` للملف PDF المصدر.
2. حدّد حقول البيانات التعريفية التي تريد تحديثها، مثل الموضوع والعنوان والكلمات المفتاحية والمنشئ.
3. استدعِ `saveNewInfoWithXmp()` مع مسار ملف الإخراج.
4. أغلق `PdfFileInfo` مثال.

### مثال Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
