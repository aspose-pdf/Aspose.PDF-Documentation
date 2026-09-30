---
title: "Menambahkan gambar ke PDF menggunakan Java"
linktitle: "Menambahkan gambar"
type: docs
weight: 10
url: /id/java/add-image-to-existing-pdf-file/
description: Pelajari cara menambahkan gambar ke file PDF yang ada dalam Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Menambahkan gambar ke file PDF yang ada dengan Java
Abstract: Artikel ini menunjukkan cara menambahkan gambar ke dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup penempatan gambar pada koordinat tetap, menambahkan gambar melalui operator halaman tingkat rendah, menetapkan teks alternatif untuk aksesibilitas, dan menyematkan data gambar dengan kompresi Flate compression.
---
Aspose.PDF for Java mendukung baik penempatan gambar tingkat tinggi maupun gambar berbasis operator tingkat rendah.

## Menambahkan gambar dengan koordinat halaman

Gunakan contoh ini ketika Anda perlu menempatkan gambar pada posisi tetap di halaman PDF.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Panggil `page.addImage()` dengan jalur gambar sumber dan persegi panjang target.
1. Simpan file PDF yang dihasilkan.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar dengan operator halaman

Gunakan contoh ini ketika Anda membutuhkan kontrol tingkat rendah atas penempatan dan skala gambar melalui operator halaman.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka aliran gambar sumber.
1. Tambahkan gambar ke sumber daya halaman dan hitung persegi panjang target.
1. Tuliskan operator grafis yang diperlukan dan simpan dokumen.

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar dan mengatur teks alternatif

Gunakan contoh ini ketika gambar harus menyertakan metadata aksesibilitas untuk pembaca layar.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan gambar ke halaman.
1. Ambil yang disisipkan [`XImage`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) dari sumber halaman.
1. Atur teks alternatif dan simpan PDF.

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar dengan kompresi Flate

Gunakan contoh ini ketika Anda ingin menyematkan data gambar dengan menggunakan kompresi Flate.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka aliran gambar.
1. Tambahkan gambar ke sumber daya halaman dengan `ImageFilterType.Flate`.
1. Gambar gambar melalui operator halaman dan menyimpan hasilnya.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
