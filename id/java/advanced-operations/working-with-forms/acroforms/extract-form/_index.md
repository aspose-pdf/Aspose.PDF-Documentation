---
title: "Mengekstrak AcroForm - ekstrak data Form dari PDF dalam Java"
linktitle: "Mengekstrak AcroForm"
type: docs
weight: 30
url: /id/java/extract-form/
description: Ekstrak nilai dari bidang AcroForm dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak nilai bidang form dari file PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengekstrak data dari bidang AcroForm menggunakan Aspose.PDF for Java. Contoh ini mengiterasi nama-nama bidang dengan fasad Form, membaca setiap nilai saat ini, dan menyimpan hasilnya dalam sebuah peta untuk pemrosesan selanjutnya."
---
Gunakan fasad `Form` ketika Anda membutuhkan alur ekstraksi nama bidang ke nilai bidang yang sederhana.

## Mengekstrak nilai dari semua bidang AcroForm

1. Buka dokumen formulir PDF dengan fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Iterasikan melalui nama-nama bidang dari fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dan baca setiap nilai bidang saat ini ke dalam peta.

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
