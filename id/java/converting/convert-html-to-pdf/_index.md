---
title: Mengonversi HTML ke file PDF di Java
linktitle: Mengonversi HTML ke file PDF
type: docs
weight: 40
url: /id/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi format HTML dan MHTML ke file PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Ikhtisar

Artikel ini menjelaskan bagaimana mengonversi HTML ke PDF menggunakan Java. Kodenya sangat sederhana, cukup muat HTML ke kelas Document dan simpan sebagai output PDF. Mengonversi MHTML ke PDF di Java juga serupa. Ini mencakup topik-topik berikut

- [Java HTML ke PDF](#convert-html-to-pdf)
- [Java MHTML ke PDF](#convert-mhtml-to-pdf)
- [Java Mengonversi HTML ke PDF](#convert-html-to-pdf)
- [Java Mengonversi MHTML ke PDF](#convert-mhtml-to-pdf)
- [Java PDF dari HTML](#convert-html-to-pdf)
- [Java PDF dari MHTML](#convert-mhtml-to-pdf)
- [Java HTML ke PDF Konverter - Cara Mengonversi Halaman Web ke PDF](#convert-html-to-pdf)

- [Java HTML ke PDF Perpustakaan, API atau Kode untuk Merender, Menyimpan, Menghasilkan atau Membuat PDF Secara Program dari HTML](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java** adalah API manipulasi PDF yang memungkinkan Anda mengonversi dokumen HTML yang ada ke PDF dengan mulus. Proses konversi HTML ke PDF dapat disesuaikan dengan fleksibel.

## Mengonversi HTML ke PDF

Contoh kode Java berikut menunjukkan cara mengonversi dokumen HTML ke PDF.

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Inisialisasi objek [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Simpan dokumen PDF keluaran dengan memanggil metode **Document.save(String)**.

```java
// Buka dokumen PDF sumber
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instansiasi objek HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Simpan dokumen
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Cobalah mengonversi HTML ke PDF secara online**

Aspose menghadirkan aplikasi online gratis ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat mencoba meneliti fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Konversi lanjutan dari HTML ke PDF

Mesin Konversi HTML memiliki beberapa opsi yang memungkinkan kita mengontrol proses konversi.

### Dukungan Media Queries

1. Buat [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. Atur mode Cetak atau Layar.
1. Inisialisasi [objek Dokumen](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Simpan dokumen PDF keluaran.

Media queries adalah teknik populer untuk memberikan lembar gaya yang disesuaikan ke perangkat yang berbeda. Kita dapat mengatur jenis perangkat menggunakan properti [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// Buat HTML LoadOptions
HtmlLoadOptions options = new HtmlLoadOptions();

// Atur mode Cetak atau Layar
options.setHtmlMediaType(HtmlMediaType.Print);

// Inisialisasi objek dokumen
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Simpan dokumen PDF keluaran
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### Mengaktifkan (menonaktifkan) penyematan font

1. Tambahkan [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) Html baru.
1. Aktifkan/Nonaktifkan penyematan font.
1. Simpan Dokumen baru.

Halaman HTML sering menggunakan font (misalnya, font dari folder lokal, Google Fonts, dll). Kita juga dapat mengontrol penyematan font dalam dokumen dengan menggunakan properti [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Aktifkan/Nonaktifkan penyematan font
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Mengelola pemuatan sumber daya eksternal

Mesin Konversi menyediakan mekanisme yang memungkinkan Anda mengontrol pemuatan sumber daya tertentu yang terkait dengan dokumen HTML.

Kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) memiliki properti [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) yang dapat kita gunakan untuk mendefinisikan perilaku pemuat sumber daya.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Membuat sumber daya template kosong untuk menggantikan:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Mengembalikan array byte kosong jika server i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Memproses sumber daya dengan pemuat sumber daya default
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Mengonversi MHTML ke PDF

{{% alert color="success" %}}
**Coba konversi MHTML ke PDF secara online**


Aspose.PDF untuk Java menghadirkan aplikasi online gratis ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi MHTML ke PDF menggunakan Aplikasi Gratis](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, singkatan dari MIME HTML, adalah format arsip halaman web yang digunakan untuk menggabungkan sumber daya yang biasanya direpresentasikan oleh tautan eksternal (seperti gambar, animasi Flash, applet Java, dan file audio) dengan kode HTML menjadi satu file. Konten dari file MHTML dikodekan seolah-olah itu adalah pesan email HTML, menggunakan tipe MIME multipart/related.

Cuplikan kode berikut menunjukkan cara mengubah file MHTML ke format PDF dengan Java:

```java
// Buat instance dari MhtLoadOptions untuk menentukan opsi pemuatan untuk
// file MHTML.
MhtLoadOptions options = new MhtLoadOptions();

// Tetapkan jalur dari file MHTML.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Muat file MHTML ke dalam objek Dokumen.
Document document = new Document(mhtmlFileName, options);

// Simpan dokumen sebagai file PDF.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Tutup dokumen.
document.close();
```