---
title: تحويل PDF إلى PDF/A و PDF/E و PDF/X في Java
linktitle: تحويل PDF إلى PDF/A و PDF/E و PDF/X
type: docs
weight: 120
url: /ar/java/convert-pdf-to-pdf_x/
lastmod: "2026-10-01"
description: تعرف على كيفية تحويل ملفات PDF إلى PDF/A و PDF/E و PDF/X في Java باستخدام Aspose.PDF للأرشفة والهندسة وإمكانية الوصول وتدفقات الطباعة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى صيغ PDF/x
Abstract: تشرح هذه المقالة طريقة التحقق من صحة وتحويل مستندات PDF إلى تنسيقات PDF/A و PDF/E و PDF/X باستخدام Aspose.PDF for Java. وتغطي إنشاء السجلات، الحفاظ على المرفقات لـ PDF/A-3، استبدال الخطوط المفقودة، الوسم التلقائي، تكوين ملف تعريف ICC، وإعدادات نية الإخراج.
---
يمكن لـ Aspose.PDF for Java التحقق من صحة وتحويل ملفات PDF القياسية إلى معايير PDF الأرشيفية والموجهة للتبادل.

## تحويل PDF إلى PDF/A

استخدم هذا المثال عندما يجب تحويل ملف PDF قياسي إلى مستند أرشيفي متوافق مع PDF/A.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثيل.
1. اتصال `document.convert(...)` مع [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` و [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. اكتب سجل التحقق إلى ملف XML جانبي حتى تُسجَّل مشكلات الامتثال أثناء التحويل.
1. احفظ مخرجات PDF/A التي تم التحقق منها.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## تحويل PDF إلى PDF/E

استخدم هذا المثال عندما يجب تحويل ملف PDF إلى معيار PDF/E الهندسي.

1. إنشاء [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) لـ [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` و مسار ملف السجل المطلوب.
1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثيل.
1. اتصال `document.convert(options)` لذا يتم تنفيذ تحويل الامتثال باستخدام كائن الخيارات المُجهَّز.
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

استخدم هذا المثال عندما يجب تحويل ملف PDF إلى معيار PDF/X الموجه للطباعة.

1. إنشاء [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) لـ [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` و مسار ملف السجل المطلوب.
1. قم بتكوين [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) مثل `FOGRA39` لذلك يتم تضمين ملف تعريف اللون المستهدف للطباعة في إعدادات التحويل.
1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إنشاء مثيل واستدعاء `document.convert(options)`.
1. احفظ الإخراج المحول بصيغة PDF/X.

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
