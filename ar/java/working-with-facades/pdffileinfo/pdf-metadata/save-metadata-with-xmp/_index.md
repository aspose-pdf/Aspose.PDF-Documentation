---
title: حفظ البيانات التعريفية باستخدام XMP
linktitle: حفظ البيانات التعريفية باستخدام XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: تعرف على كيفية حفظ بيانات تعريف PDF باستخدام XMP في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ بيانات تعريف PDF باستخدام XMP باستخدام Aspose.PDF لـ Java
Abstract: تعرف على كيفية حفظ بيانات تعريف PDF باستخدام XMP باستخدام Aspose.PDF لـ Java. يقوم مثال Java بتحديث حقول البيانات التعريفية الأساسية باستخدام PdfFileInfo ويعيد كتابتها باستخدام `saveNewInfoWithXmp()` بحيث يقوم مستند الإخراج بتخزين المعلومات في نموذج XMP.
---
## حفظ البيانات التعريفية باستخدام XMP

استخدم سير العمل هذا عندما تحتاج إلى تخزين معلومات المستند المحدثة بتنسيق XMP.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لملف PDF المصدر.
2. قم بتعيين حقول البيانات التعريفية التي تريد تحديثها، مثل الموضوع والعنوان والكلمات الرئيسية والمنشئ.
3. اتصل `saveNewInfoWithXmp()` بمسار ملف الإخراج.
4. أغلق المثيل `PdfFileInfo`.

### مثال جافا

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
