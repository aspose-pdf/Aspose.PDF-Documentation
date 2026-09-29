---
title: Impor dan Ekspor Data Form
linktitle: Impor dan Ekspor Data Form
type: docs
weight: 80
url: /id/java/import-export-form-data/
description: Impor dan ekspor data bidang AcroForm dalam format XML, FDF, XFDF, dan JSON menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Impor dan ekspor data formulir PDF dengan Java
Abstract: Artikel ini menjelaskan cara menukar data AcroForm dengan format eksternal menggunakan Aspose.PDF for Java. Artikel ini mencakup mengimpor dan mengekspor data XML, FDF, dan XFDF melalui antarmuka Form dan mengekstrak nilai bidang formulir ke JSON.
---
Aspose.PDF for Java mendukung beberapa format pertukaran data umum untuk formulir interaktif.

## Impor data Form dari XML

Gunakan contoh ini ketika nilai formulir disimpan dalam file XML dan harus diterapkan ke formulir PDF.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran masukan XML dan impor data ke dalam formulir.
1. Simpan dokumen PDF yang diperbarui.

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Ekspor data formulir ke XML

Gunakan contoh ini ketika Anda perlu menyimpan nilai AcroForm saat ini dalam format XML.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran keluaran untuk file XML.
1. Ekspor data formulir ke XML.

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Impor data formulir dari FDF

Gunakan contoh ini ketika nilai formulir tiba dalam format pertukaran FDF.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran input FDF dan impor data.
1. Simpan dokumen PDF yang telah diisi.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Ekspor data formulir ke FDF

Gunakan contoh ini ketika nilai formulir PDF harus dibagikan sebagai file FDF.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran output untuk file FDF.
1. Ekspor data formulir dalam format FDF.

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Impor data formulir dari XFDF

Gunakan contoh ini ketika data formulir disediakan dalam format XFDF dan harus digabungkan ke dalam PDF.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran masukan XFDF dan impor nilai-nilai tersebut.
1. Simpan dokumen PDF yang diperbarui.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Ekspor data formulir ke XFDF

Gunakan contoh ini ketika Anda membutuhkan file pertukaran berbasis XML untuk nilai AcroForm.

1. Buat sebuah [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad dan mengikat PDF sumber.
1. Buka aliran keluaran untuk file XFDF.
1. Ekspor nilai formulir saat ini ke XFDF.

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## Ekstrak bidang formulir ke JSON

Gunakan contoh ini ketika nilai formulir harus diekspor ke representasi JSON ringan.

1. Buka PDF dengan [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fasad.
1. Iterasi melalui nama-nama field dan serialisasikan nilai-nilainya ke dalam teks JSON.
1. Tuliskan konten JSON ke file target.

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## Gunakan kembali pembantu ekstraksi JSON

Gunakan contoh ini ketika Anda ingin metode pembungkus khusus yang mendelegasikan ke rutinitas ekspor JSON utama.

1. Panggil helper ekstraksi JSON yang ada dengan PDF sumber dan jalur output.
1. Gunakan kembali logika ekstraksi yang sama tanpa menduplikasi kode serialisasi.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
