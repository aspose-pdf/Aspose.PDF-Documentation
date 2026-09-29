---
title: Bekerja dengan Formulir XFA
linktitle: Formulir XFA
type: docs
weight: 20
url: /id/java/xfa-forms/
description: Pelajari cara mengonversi formulir XFA ke AcroForms standar dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Konversi formulir PDF berbasis XFA ke AcroForms standar dengan Java
Abstract: Artikel ini menjelaskan cara bekerja dengan formulir berbasis XFA menggunakan Aspose.PDF for Java. Artikel ini mencakup mengonversi formulir XFA dinamis ke AcroForm standar dan menangani dokumen XFA yang memerlukan opsi ignore-needs-rendering sebelum konversi.
---
Formulir XFA dapat dikonversi ke AcroForms standar sehingga dapat diproses dengan API formulir PDF reguler.

## Konversi formulir XFA dinamis ke AcroForm

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses dokumen [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) dan atur yang diperlukan [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) properti.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Konversi formulir XFA dengan `ignoreNeedsRendering`

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses dokumen [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) dan atur yang diperlukan `ignoreNeedsRendering` dan [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) properti.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
