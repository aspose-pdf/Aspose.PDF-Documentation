---
title: "Mengonversi HTML ke PDF di Java"
linktitle: "Mengonversi file HTML ke PDF"
type: docs
weight: 40
url: /id/java/convert-html-to-pdf/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi HTML, MHTML, dan halaman web ke PDF dalam Java dengan Aspose.PDF, termasuk pengaturan media, aturan halaman CSS, penyematan font, konten SVG, dan output satu halaman.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Mengonversi HTML ke PDF dalam Java dengan Aspose.PDF"
Abstract: Artikel ini menjelaskan cara mengonversi file HTML dan MHTML ke PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup alur kerja dasar HTML ke PDF dan menunjukkan cara mengontrol rendering dengan tipe media, prioritas aturan halaman CSS, font yang disematkan, konten SVG, output satu halaman, serta konversi langsung dari halaman web yang hidup.
---
Aspose.PDF for Java dapat mengonversi file HTML lokal, konten MHTML yang diarsipkan, dan halaman web langsung menjadi dokumen PDF. Anda dapat mengendalikan alur konversi dengan `HtmlLoadOptions` dan `MhtLoadOptions` untuk memengaruhi skala tata letak, penanganan media CSS, prioritas aturan halaman, penyematan font, resolusi sumber daya, dan perilaku rendering satu halaman.

## Mengonversi HTML ke PDF

Gunakan contoh ini ketika file HTML lokal harus dikonversi langsung menjadi dokumen PDF.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) untuk mengonfigurasi bagaimana sumber HTML diinterpretasikan selama impor.
1. Atur [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) ke `ScaleToPageWidth` konten HTML yang terlalu lebar diskalakan ke lebar halaman PDF target alih-alih dipotong.
1. Buka file HTML sumber dengan melewatkan jalurnya dan opsi pemuatan yang dikonfigurasi ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan yang dihasilkan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) sebagai file PDF pada jalur output target.

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi HTML ke PDF dengan opsi tipe media

Gunakan contoh ini ketika penanganan tipe media CSS harus dikontrol selama konversi HTML.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) untuk pengaturan konversi.
1. Atur [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) ke `Screen` ketika HTML harus dirender dengan aturan CSS yang dimaksudkan untuk tampilan di layar alih-alih media cetak.
1. Buka file HTML dengan opsi pemuatan yang telah dikonfigurasi sehingga gaya yang bergantung pada media query diterapkan selama konversi.
1. Simpan hasilnya [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) sebagai file PDF.

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi HTML ke PDF dengan prioritas aturan halaman CSS

Gunakan contoh ini ketika CSS `@page` aturan harus memengaruhi tata letak halaman PDF akhir.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) sebelum membuka file HTML.
1. Konfigurasikan `setPriorityCssPageRule(false)` ketika pengaturan tata letak lainnya harus memiliki prioritas atas CSS `@page` deklarasi dalam markup sumber.
1. Muat konten HTML ke dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan opsi yang dikonfigurasi sehingga tata letak halaman diselesaikan selama impor.
1. Simpan file PDF yang dihasilkan.

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi HTML ke PDF dengan font yang disematkan

Gunakan contoh ini ketika PDF output harus mempertahankan font HTML dengan menyematkannya.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) untuk konfigurasi impor HTML.
1. Aktifkan `setEmbedFonts(true)` Jadi font yang ditentukan selama render HTML disimpan dalam PDF output.
1. Buka sumber HTML dengan opsi pemuatan ini untuk menjaga tipografi asli tetap tersedia dalam dokumen akhir.
1. Simpan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) sebagai PDF dengan sumber daya font yang disematkan disertakan.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Merender konten HTML pada satu halaman PDF

Gunakan contoh ini ketika konten HTML yang panjang harus tetap berada di satu halaman PDF alih-alih mengalir ke beberapa halaman.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) untuk pengaturan konversi.
1. Aktifkan `setRenderToSinglePage(true)` sehingga HTML yang diimpor ditata pada satu halaman PDF alih-alih dibagi menjadi beberapa halaman.
1. Buka HTML sumber dengan opsi pemuatan yang dikonfigurasi dan biarkan Aspose.PDF membangun tata letak halaman dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan file PDF output.

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi HTML yang berisi SVG inline

Gunakan contoh ini ketika sumber HTML menyertakan data SVG inline yang harus dirender dalam PDF.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) dengan direktori induk file HTML sebagai jalur dasar sehingga sumber daya terkait dapat diselesaikan secara konsisten selama konversi.
1. Buka file HTML yang berisi markup SVG inline dengan melewatkan jalur sumber dan opsi pemuatan ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF merender DOM HTML bersama dengan elemen SVG yang disematkan ke dalam konten halaman PDF.
1. Simpan dokumen PDF yang dihasilkan.

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi halaman web ke PDF

Gunakan contoh ini ketika URL web langsung harus dirender dan disimpan sebagai dokumen PDF.

1. Buat sebuah instans [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) dengan URL target sehingga sumber daya relatif seperti stylesheet dan gambar dapat diselesaikan terhadap alamat tersebut.
1. Ubah string URL menjadi a objek `URL` dan buka aliran masuknya untuk mengambil konten HTML secara langsung.
1. Buat [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dari aliran respons dan opsi pemuatan yang dikonfigurasi sehingga halaman yang diunduh diproses dengan URL dasar yang benar.
1. Simpan halaman web yang dirender sebagai file PDF dan tutup sumber daya stream secara otomatis dengan try-with-resources.

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## Mengonversi MHTML ke PDF

Gunakan contoh ini ketika file MHTML yang diarsipkan harus dikonversi menjadi dokumen PDF.

1. Buat sebuah instans [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) untuk memberi tahu Aspose.PDF agar memuat sumber sebagai konten MIME HTML.
1. Buka `.mht` atau `.mhtml` file dengan melewatkan jalurnya dan opsi pemuatan MHTML ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Izinkan Aspose.PDF menguraikan konten HTML yang diarsipkan dan sumber daya tersematnya ke dalam model dokumen PDF.
1. Simpan file PDF yang dihasilkan.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
