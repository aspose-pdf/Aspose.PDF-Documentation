---
title: حفظ وثيقة PDF برمجيا
linktitle: حفظ قوات الدفاع الشعبي
type: docs
weight: 30
url: /java/save-pdf-document/
description: تعرف على كيفية حفظ مستندات PDF في Java في ملف، أو في دفق، أو كمعيار PDF باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Java
Abstract: توضح هذه المقالة كيفية حفظ مستندات PDF في Java باستخدام Aspose.PDF. وهو يغطي الحفظ في مسار ملف، والحفظ في OutputStream، وتحويل المستند قبل حفظه كملف قياسي PDF/X.
---
يوفر Aspose.PDF for Java عدة طرق لحفظ مستند اعتمادًا على الوجهة المستهدفة ومتطلبات الإخراج.

## حفظ مستند PDF في جافا

يمكنك حفظ مستند:

1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مباشرة في ملف على القرص.
1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى `OutputStream`.
1. قم بتحويل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) باستخدام [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) واحفظه بتنسيق قياسي مثل [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## حفظ المستند إلى ملف

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## احفظ المستند للبث

```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## احفظ المستند بصيغة PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
