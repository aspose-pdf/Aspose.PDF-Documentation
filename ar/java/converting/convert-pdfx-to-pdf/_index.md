---
title: تحويل PDF/A وPDF/UA إلى PDF في Java
linktitle: تحويل PDF/A وPDF/UA إلى PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: تعرف على كيفية إزالة توافق PDF/A وPDF/UA من ملفات PDF المستندة إلى المعايير في Java وحفظها كمستندات PDF قياسية.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF/A وPDF/UA إلى PDF قياسي في Java
Abstract: تشرح هذه المقالة كيفية إزالة توافق PDF/A وPDF/UA من مستندات PDF المستندة إلى المعايير باستخدام Aspose.PDF لـ Java، ثم حفظ النتيجة كملف PDF قياسي.
---
يمكن لـ Aspose.PDF for Java تحويل متغيرات PDF المتوافقة مع المعايير مرة أخرى إلى مستند PDF عادي.

## تحويل PDF/A إلى PDF قياسي

استخدم هذا المثال عندما يجب إرجاع مستند PDF/A الأرشيفي إلى ملف PDF قياسي.

1. افتح ملف PDF/A المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بـ `removePdfaCompliance()` لفصل ملف تعريف التوافق الأرشيفي عن المستند الذي تم تحميله.
1. احفظ ملف PDF القياسي الناتج بدون مجموعة قيود PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## تحويل PDF/UA إلى PDF قياسي

استخدم هذا المثال عندما يتعين تحويل مستند PDF/UA يمكن الوصول إليه مرة أخرى إلى ملف PDF قياسي.

1. افتح ملف PDF/UA المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بـ `removePdfUaCompliance()` لإزالة ملف تعريف توافق إمكانية الوصول من بيانات تعريف المستند ومتطلبات البنية.
1. احفظ مستند PDF الناتج كملف PDF عادي.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
