---
title: Dapatkan dan Atur Properti Halaman PDF di Java
linktitle: Mendapatkan dan Mengatur Properti Halaman
type: docs
weight: 90
url: /id/java/get-and-set-page-properties/
description: Pelajari cara memeriksa properti halaman PDF seperti jumlah, kotak, rotasi, dan informasi warna di Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Periksa jumlah halaman, kotak, dan tipe warna dalam file PDF dengan Java
Abstract: Artikel ini menjelaskan cara memeriksa properti halaman menggunakan Aspose.PDF for Java. Ini mencakup membaca jumlah halaman, menghasilkan paragraf dan memeriksa jumlah yang dihasilkan sebelum menyimpan, mencetak semua nilai kotak halaman utama, dan mengidentifikasi tipe warna setiap halaman.
---
Aspose.PDF for Java dapat memeriksa jumlah halaman, kotak halaman, rotasi, dan tipe warna halaman.

## Dapatkan jumlah halaman

Gunakan contoh ini ketika Anda perlu membaca total jumlah halaman dalam PDF.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Baca ukuran koleksi halaman.
1. Keluarkan jumlah total halaman.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Dapatkan jumlah halaman sebelum menyimpan

Gunakan contoh ini ketika Anda perlu mengetahui berapa banyak halaman yang akan dihasilkan konten sebelum menulis file.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan konten ke halaman.
1. Proses paragraf untuk memaksa perhitungan tata letak.
1. Baca jumlah halaman yang dihasilkan dan keluarkan.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## Dapatkan properti kotak halaman

Gunakan contoh ini ketika Anda perlu memeriksa semua dimensi kotak utama dan nilai rotasi halaman.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan akses halaman target.
1. Kumpulkan nilai kotak halaman ke dalam peta.
1. Keluarkan dimensi dan informasi rotasi halaman.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## Dapatkan tipe warna setiap halaman

Gunakan contoh ini ketika Anda perlu mengidentifikasi apakah halaman berwarna hitam putih, skala abu-abu, atau RGB.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan semua halaman dan baca setiap halaman [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Ubah nilai enum menjadi teks yang dapat dibaca dan keluarkan hasilnya.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
