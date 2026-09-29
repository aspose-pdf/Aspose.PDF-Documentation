---
title: Tambahkan Cap Gambar ke PDF dalam Java
linktitle: Cap gambar dalam File PDF
type: docs
weight: 10
url: /id/java/image-stamps-in-pdf-page/
description: Pelajari cara menambahkan cap gambar ke halaman PDF dalam Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan cap gambar dan latar belakang gambar ke halaman PDF dengan Java
Abstract: Artikel ini menjelaskan cara menambahkan stempel gambar ke file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup stempel gambar dengan penempatan, rotasi, opasitas, dan kontrol kualitas, serta menggunakan gambar sebagai latar belakang kotak mengambang.
---
Aspose.PDF for Java mendukung stempel gambar sebagai overlay dan elemen tata letak berbasis gambar.

## Tambahkan stempel gambar

Gunakan contoh ini ketika sebuah halaman harus menampilkan stempel gambar dengan penempatan dan opasitas kustom.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) dan konfigurasikan tampilannya.
1. Tambahkan stempel ke halaman dan simpan dokumen.

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan cap gambar dengan kontrol kualitas

Gunakan contoh ini ketika Anda perlu menyesuaikan kualitas rendering stempel gambar.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) dan atur nilai kualitas.
1. Tambahkan stempel ke halaman dan simpan hasilnya.

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Gunakan gambar sebagai latar belakang kotak mengambang

Gunakan contoh ini ketika gambar harus menjadi latar belakang kontainer tata letak yang bergaya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan akses halaman target.
1. Buat sebuah [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) dengan pengaturan teks dan batas.
1. Atur gambar latar, tambahkan kotak ke halaman, dan simpan dokumen.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
