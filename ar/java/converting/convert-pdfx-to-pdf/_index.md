---
title: تحويل PDF/A و PDF/UA إلى PDF في Java
linktitle: تحويل PDF/A و PDF/UA إلى PDF
type: docs
weight: 120
url: /ar/java/convert-pdf_x-to-pdf/
lastmod: "2026-10-01"
description: تعلم كيفية إزالة التوافق مع PDF/A و PDF/UA من ملفات PDF المبنية على المعايير في Java وحفظها كمستندات PDF عادية.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF/A و PDF/UA إلى PDF عادي في Java
Abstract: تشرح هذه المقالة كيفية إزالة التوافق مع PDF/A و PDF/UA من مستندات PDF المبنية على المعايير باستخدام Aspose.PDF for Java، ثم حفظ النتيجة كملف PDF عادي.
---
يمكن لـ Aspose.PDF for Java تحويل أنواع PDF المتوافقة مع المعايير مرة أخرى إلى مستند PDF عادي.

## تحويل PDF/A إلى PDF قياسي

استخدم هذا المثال عندما يجب تخفيض وثيقة PDF/A الأرشيفية إلى PDF قياسي.

1. افتح ملف PDF/A المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثيل.
1. اتصال `removePdfaCompliance()` لفصل ملف تعريف الالتزام بالأرشفة عن المستند المحمل.
1. احفظ ملف PDF القياسي الناتج دون تعيين قيود PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## تحويل PDF/UA إلى PDF قياسي

استخدم هذا المثال عندما ينبغي تحويل مستند PDF/UA القابل للوصول مرةً أخرى إلى PDF قياسي.

1. افتح ملف PDF/UA الأصلي في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثيل.
1. اتصال `removePdfUaCompliance()` لإزالة ملف تعريف الامتثال لإمكانية الوصول من بيانات تعريف المستند والمتطلبات الهيكلية.
1. احفظ مستند PDF الناتج كملف PDF عادي.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
