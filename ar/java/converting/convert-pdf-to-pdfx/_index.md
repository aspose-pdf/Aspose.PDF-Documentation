---
title: تحويل PDF إلى PDF/A، PDF/E، وPDF/X في Java
linktitle: تحويل PDF إلى PDF/A، PDF/E، وPDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل ملفات PDF إلى PDF/A وPDF/E وPDF/X في Java باستخدام Aspose.PDF للأرشفة والهندسة وإمكانية الوصول وسير عمل الطباعة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى صيغ PDF/x
Abstract: تشرح هذه المقالة كيفية التحقق من صحة مستندات PDF وتحويلها إلى تنسيقات PDF/A، وPDF/E، وPDF/X باستخدام Aspose.PDF لـ Java. ويغطي إنشاء السجل، والحفاظ على المرفقات لـ PDF/A-3، واستبدال الخط المفقود، ووضع العلامات التلقائي، وتكوين ملف تعريف ICC، وإعدادات هدف الإخراج.
---
يمكن لـ Aspose.PDF for Java التحقق من صحة ملفات PDF القياسية وتحويلها إلى معايير PDF أرشيفية وموجهة نحو التبادل.

## تحويل PDF إلى PDF/A

استخدم هذا المثال عندما يجب تحويل ملف PDF قياسي إلى مستند أرشيفي متوافق مع PDF/A.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بـ`document.convert(...)` مع [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` و[`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. اكتب سجل التحقق من الصحة في ملف XML الجانبي بحيث يتم تسجيل مشكلات الامتثال أثناء التحويل.
1. احفظ مخرجات PDF/A التي تم التحقق من صحتها.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## تحويل PDF إلى PDF/E

استخدم هذا المثال عندما يجب تحويل ملف PDF إلى معيار PDF/E ذي التوجه الهندسي.

1. قم بإنشاء [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) لـ [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` ومسار ملف السجل المطلوب.
1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بـ`document.convert(options)` حتى يتم تنفيذ تحويل التوافق باستخدام كائن الخيارات المجهزة.
1. احفظ ملف PDF المتوافق الناتج.

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## تحويل PDF إلى PDF/X

استخدم هذا المثال عندما يجب تحويل ملف PDF إلى معيار PDF/X المخصص للطباعة.

1. قم بإنشاء [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) لـ [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` ومسار ملف السجل المطلوب.
1. قم بتكوين [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) مثل `FOGRA39` بحيث يتم تضمين ملف تعريف الألوان المستهدف للطباعة في إعدادات التحويل.
1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واتصل بـ`document.convert(options)`.
1. احفظ مخرجات PDF/X المحولة.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
