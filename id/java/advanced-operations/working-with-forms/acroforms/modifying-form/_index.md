---
title: Memodifikasi AcroForm
linktitle: Memodifikasi AcroForm
type: docs
weight: 45
url: /id/java/modifying-form/
description: Modifikasi bidang AcroForm dalam dokumen PDF menggunakan Aspose.PDF for Java, termasuk menghapus teks, mengatur batas, menata tampilan bidang, dan menghapus bidang.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifikasi dan sesuaikan bidang formulir PDF dengan Java
Abstract: Artikel ini menjelaskan cara memodifikasi konten AcroForm menggunakan Aspose.PDF for Java. Artikel ini mencakup penghapusan teks dari sumber formulir Typewriter, pengaturan dan pembacaan batas panjang bidang teks, mengubah tampilan font bidang formulir, serta menghapus bidang tertentu berdasarkan namanya.
---
Pemeliharaan Form sering melibatkan pengeditan pada tingkat bidang serta pembersihan sumber daya halaman terkait formulir.

## Hapus teks dalam sumber daya formulir yang disematkan

Gunakan contoh ini ketika konten formulir Typewriter harus dikosongkan tanpa menghapus objek formulir itu sendiri.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasi melalui sumber daya formulir halaman dan temukan formulir Typewriter.
1. Bersihkan fragmen teks yang diserap dan simpan dokumen.

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Atur batas panjang field teks

Gunakan contoh ini ketika bidang teks hanya boleh menerima sejumlah karakter terbatas.

1. Buat sebuah [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fasad dan mengikat PDF sumber.
1. Atur panjang maksimum untuk bidang target.
1. Simpan dokumen yang diperbarui.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Dapatkan batas panjang bidang teks

Gunakan contoh ini ketika Anda perlu memeriksa panjang maksimum saat ini dari sebuah bidang teks.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses bidang target dari koleksi formulir.
1. Baca batas dari [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) dan keluarkan.

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## Ubah font field formulir

Gunakan contoh ini ketika field teks yang ada harus menggunakan font atau tampilan yang berbeda.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses target [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) dan atur tampilan default baru.
1. Simpan PDF yang diperbarui.

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## Hapus field formulir berdasarkan nama

Gunakan contoh ini ketika field tertentu harus dihapus dari AcroForm.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus bidang target dari form berdasarkan namanya.
1. Simpan dokumen yang diperbarui.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
