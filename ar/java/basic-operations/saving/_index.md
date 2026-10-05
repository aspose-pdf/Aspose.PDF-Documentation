---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/java/save-pdf-document/
description: تعلم كيفية حفظ مستندات PDF في Java إلى ملف، إلى تدفق، أو كمعيار PDF باستخدام Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Java
Abstract: تصف هذه المقالة كيفية حفظ مستندات PDF في Java باستخدام Aspose.PDF. وتغطي الحفظ إلى مسار ملف، والحفظ إلى OutputStream، وتحويل المستند قبل حفظه كملف معيار PDF/X.
---
يوفر Aspose.PDF for Java عدة طرق لحفظ المستند اعتمادًا على الوجهة المستهدفة ومتطلبات الإخراج.

## حفظ مستند PDF في Java

يمكنك حفظ مستند:

1. احفظ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مباشرةً إلى ملف على القرص.
1. احفظ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى `OutputStream`.
1. حوّل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مع [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) واحفظه بتنسيق قياسي مثل [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## حفظ المستند إلى ملف

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## حفظ المستند إلى التدفق

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

## حفظ المستند كـ PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
