---
title: Ekstrak AcroForm - Ekstrak Data Form dari PDF dalam Java
linktitle: Ekstrak AcroForm
type: docs
weight: 30
url: /id/java/extract-form/
description: Ekstrak nilai dari bidang AcroForm dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak nilai bidang form dari file PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengekstrak data dari bidang AcroForm menggunakan Aspose.PDF for Java. Contoh ini mengiterasi nama-nama bidang dengan facade Form, membaca setiap nilai saat ini, dan menyimpan hasilnya dalam sebuah peta untuk pemrosesan selanjutnya.
---
Gunakan `Form` fasad ketika Anda membutuhkan alur ekstraksi nama bidang ke nilai bidang yang sederhana.

## Ekstrak nilai dari semua field AcroForm

1. Buka dokumen formulir PDF dengan [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. Iterasi melalui nama-nama field dari [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade dan baca setiap nilai field saat ini ke dalam peta.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
