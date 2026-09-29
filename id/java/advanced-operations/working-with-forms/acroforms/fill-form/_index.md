---
title: Isi AcroForm - Isi Formulir PDF menggunakan Java
linktitle: Isi AcroForm
type: docs
weight: 20
url: /id/java/fill-form/
description: Isi bidang AcroForm dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Isi bidang AcroForm dalam file PDF dengan Java
Abstract: Artikel ini menjelaskan cara mengisi bidang AcroForm menggunakan Aspose.PDF for Java. Contoh tersebut memuat PDF melalui facade Form, mencocokkan nama bidang dengan peta nilai, memperbarui bidang yang cocok, dan menyimpan dokumen yang selesai.
---
itu `Form` facade dapat digunakan untuk mengotomatisasi pengisian bidang pada AcroForm yang ada.

## Isi bidang AcroForm dengan nilai baru

1. Buka dokumen PDF Form dengan [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad.
1. Iterasikan melalui bidang Form dan perbarui entri yang cocok dengan nilai yang diberikan.
1. Simpan dokumen PDF yang diperbarui.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
