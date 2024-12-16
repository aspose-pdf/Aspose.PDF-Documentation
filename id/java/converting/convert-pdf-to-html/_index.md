---
title: Mengonversi File PDF ke Format HTML 
linktitle: Mengonversi File PDF ke Format HTML
type: docs
weight: 50
url: /id/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke format HTML dengan pustaka Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF untuk Java menyediakan banyak fitur untuk mengonversi berbagai format file ke dokumen PDF dan mengonversi file PDF ke berbagai format keluaran. Artikel ini membahas cara mengonversi file PDF ke format HTML dan menyimpan gambar dari file PDF ke dalam folder tertentu.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke HTML secara online**

Aspose.PDF untuk Java menghadirkan aplikasi online gratis ["PDF ke HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Ketika mengonversi file PDF besar dengan beberapa halaman ke format HTML, output muncul sebagai satu halaman HTML. Ini bisa menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk membagi output menjadi beberapa halaman selama konversi PDF ke HTML.

## Mengonversi Halaman PDF ke HTML

Aspose.PDF untuk Java menyediakan banyak fitur untuk mengonversi berbagai format file ke dokumen PDF dan mengonversi file PDF ke berbagai format output. Artikel ini membahas cara mengonversi file PDF ke format HTML dan menyimpan gambar dari file PDF ke dalam folder tertentu.

Cuplikan kode berikut menunjukkan semua opsi yang mungkin dapat digunakan saat mengonversi PDF ke HTML.

```java
// Buka dokumen PDF sumber
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// Simpan file ke dalam format dokumen MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## Mengonversi PDF ke HTML - Memisahkan Output ke HTML Multi-halaman

Aspose.PDF untuk Java mendukung fitur untuk mengonversi dokumen PDF ke berbagai format output termasuk HTML.
 Namun ketika mengonversi file PDF besar (terdiri dari beberapa halaman), Anda mungkin memiliki kebutuhan untuk menyimpan setiap halaman PDF ke file HTML terpisah.

Saat mengonversi file PDF besar dengan beberapa halaman ke format HTML, outputnya muncul sebagai satu halaman HTML. Ini bisa menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk membagi output menjadi beberapa halaman selama konversi PDF ke HTML. Silakan coba gunakan potongan kode berikut.

```java
// Buka dokumen PDF sumber
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// Memulai objek HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Tentukan untuk membagi output menjadi beberapa halaman
htmlOptions.setSplitIntoPages(true);

// Simpan dokumen
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## Konversi PDF ke HTML - Hindari Menyimpan Gambar dalam Format SVG

Format output default untuk menyimpan gambar saat mengonversi dari PDF ke HTML adalah SVG. Selama konversi, beberapa gambar dari PDF diubah menjadi gambar vektor SVG. Ini bisa lambat. Sebagai gantinya, gambar dapat diubah menjadi PNG. Untuk memungkinkan hal ini, Aspose.PDF memiliki opsi untuk menggunakan SVG untuk vektor atau membuat PNG.

Untuk sepenuhnya menghapus rendering gambar sebagai format SVG saat mengonversi file PDF ke format HTML, silakan coba menggunakan potongan kode berikut.

```java
 // Memuat file PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Membuat objek opsi penyimpanan HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Tentukan folder tempat gambar SVG disimpan selama konversi PDF ke HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// Simpan file output
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## Mengompresi Gambar SVG Selama Konversi

Untuk mengompresi gambar SVG selama konversi PDF ke HTML, silakan coba menggunakan kode berikut:

```java
// Memuat file PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Membuat HtmlSaveOption dengan fitur yang diuji
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Kompres gambar SVG jika ada
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Konversi PDF ke HTML - Tentukan Folder Gambar

Secara default, ketika mengonversi file PDF ke HTML, gambar dalam PDF disimpan dalam folder terpisah yang dibuat di direktori yang sama dengan output HTML. Namun terkadang, perlu untuk menentukan folder yang berbeda untuk menyimpan gambar saat menghasilkan file HTML. Untuk mencapai ini, kami memperkenalkan [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions). Metode [SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) digunakan untuk menentukan folder target untuk menyimpan gambar.

```java
// Muat file PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Tentukan folder terpisah untuk menyimpan gambar
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Buat File Berikutnya dengan Isi Badan Saja

Dengan potongan kode sederhana berikut, Anda dapat membagi output HTML menjadi halaman. Dalam halaman output, semua objek HTML harus ditempatkan persis di tempatnya sekarang (pemrosesan dan output font, pembuatan dan output CSS, pembuatan dan output gambar), kecuali bahwa output HTML akan berisi konten yang saat ini ditempatkan di dalam tag (sekarang tag "body" akan dihilangkan).

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## Perenderan Teks Transparan

Jika file PDF sumber/input berisi teks transparan yang dibayangi oleh gambar latar depan, maka mungkin ada masalah perenderan teks. Jadi untuk mengatasi skenario seperti itu, metode `setSaveShadowedTextsAsTransparentTexts` dan `setSaveTransparentTexts` dapat digunakan.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Memulai objek HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// Simpan dokumen
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## Rendering lapisan dokumen PDF

Kita dapat merender lapisan dokumen PDF dalam elemen tipe lapisan terpisah selama konversi PDF ke HTML:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// Memperkenalkan objek HTML SaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Menentukan untuk merender lapisan dokumen PDF secara terpisah dalam output HTML
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// Simpan dokumen
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

Konversi PDF ke HTML adalah salah satu fitur Aspose.PDF yang paling populer karena memungkinkan untuk melihat konten file PDF di berbagai platform tanpa menggunakan penampil dokumen PDF. HTML output sesuai dengan standar WWW dan dapat dengan mudah ditampilkan di semua browser web. Dengan menggunakan fitur ini, file PDF dapat dilihat di perangkat genggam karena Anda tidak perlu menginstal aplikasi penampil PDF, tetapi dapat menggunakan browser web sederhana.

## PDF ke HTML - Kecualikan Sumber Daya Font

Jika Anda berniat untuk mengecualikan semua atau beberapa sumber daya font selama konversi PDF ke HTML, Aspose.PDF untuk Java API memungkinkan Anda mencapai ini dengan bantuan kelas HtmlSaveOptions. API menawarkan dua opsi untuk tujuan ini.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - untuk mencegah ekspor semua font
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - adalah untuk mencegah ekspor font tertentu (nama font harus disebutkan tanpa hash)

Untuk mengonversi PDF ke HTML dengan mengecualikan sumber daya font, gunakan langkah-langkah berikut:

1. Definisikan objek baru dari kelas HtmlSaveOptions
1. Definisikan dan atur nama font yang akan dicegah dari ekspor di HtmlSaveOptions.ExcludeFontNameList
1. Konversikan PDF ke HTML menggunakan metode save

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```