---
title: Mengonversi PDF ke Dokumen Microsoft Word di Java
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: id/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Mengonversi file PDF ke format DOC dan DOCX dengan mudah dan kendali penuh menggunakan Aspose.PDF untuk Java. Pelajari lebih lanjut cara mengatur konversi PDF ke dokumen Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tinjauan

Artikel ini menjelaskan cara mengonversi PDF ke Word menggunakan Java. Kodenya sangat sederhana, cukup muat PDF ke kelas Document dan simpan sebagai output format Microsoft Word DOC atau DOCX. Ini mencakup topik-topik berikut

- [Java PDF ke Word](#convert-pdf-to-doc)
- [Java PDF ke DOC](#convert-pdf-to-doc)
- [Java PDF ke DOCX](#convert-pdf-to-docx)
- [Java Mengonversi PDF ke Word](#convert-pdf-to-docx)
- [Java Mengonversi PDF ke DOC](#convert-pdf-to-doc)
- [Java Mengonversi PDF ke DOCX](#convert-pdf-to-docx)
- [Java Cara mengonversi file PDF ke Word DOC](#convert-pdf-to-doc) atau [Word DOCX](#convert-pdf-to-docx)

- [Java PDF ke Word Library, API atau Kode untuk Menyimpan, Menghasilkan atau Membuat Dokumen Word Secara Program dari PDF](#convert-pdf-to-docx)

## Mengonversi PDF ke DOC

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang membuat konten mudah untuk dimanipulasi. Aspose.PDF untuk Java memungkinkan Anda mengonversi file PDF ke DOC.

**Aspose.PDF untuk Java** dapat membuat dokumen PDF dari awal dan merupakan alat yang hebat untuk memperbarui, mengedit, dan memanipulasi dokumen PDF yang ada. Sebuah fitur penting adalah kemampuan untuk mengonversi halaman dan seluruh dokumen PDF ke gambar. Fitur populer lainnya adalah konversi PDF ke Microsoft Word DOC, yang membuat konten mudah untuk dimanipulasi. (Kebanyakan pengguna tidak dapat mengedit dokumen PDF tetapi dapat dengan mudah bekerja dengan tabel, teks, dan gambar di Microsoft Word.)

Untuk membuatnya sederhana dan mudah dipahami, Aspose.PDF untuk Java menyediakan kode dua baris untuk mengubah file PDF sumber menjadi file DOC.

Cuplikan kode Java berikut menunjukkan proses mengonversi file PDF ke format DOC.

1. Buat instance objek [Document](https://reference.aspose.com/page/java/com.aspose.page/document) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.Doc** dengan memanggil metode **Document.save()**.

```java
public static void convertPDFtoWord() {
    // Buka dokumen PDF sumber
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Simpan file ke dalam format dokumen MS
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## Menggunakan Kelas DocSaveOptions

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) menyediakan berbagai properti yang meningkatkan proses konversi file PDF ke format DOC. Di antara properti-properti ini, Mode memungkinkan Anda untuk menentukan mode pengenalan untuk konten PDF. Anda dapat menentukan nilai apa pun dari enumerasi RecognitionMode untuk properti ini. Setiap nilai ini memiliki keuntungan dan keterbatasan spesifik:

- Mode [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) cepat dan bagus untuk menjaga tampilan asli file PDF, tetapi kemampuan edit dari dokumen yang dihasilkan bisa terbatas.
 Setiap blok teks yang dikelompokkan secara visual dalam PDF asli diubah menjadi kotak teks dalam dokumen keluaran. Ini mencapai kemiripan maksimal dengan aslinya sehingga dokumen keluaran terlihat bagus, tetapi sepenuhnya terdiri dari kotak teks dan bisa membuat pengeditan di Microsoft Word menjadi sulit.

- Flow adalah mode pengenalan penuh, di mana mesin melakukan pengelompokan dan analisis multi-level untuk mengembalikan dokumen asli sesuai dengan maksud penulis sambil menghasilkan dokumen yang mudah diedit. Keterbatasannya adalah dokumen keluaran mungkin terlihat berbeda dari aslinya.

- Properti RelativeHorizontalProximity dapat digunakan untuk mengontrol kedekatan relatif antara elemen teks dan berarti bahwa jarak dinormalkan oleh ukuran font. Font yang lebih besar mungkin memiliki jarak yang lebih besar antara suku kata dan masih dianggap sebagai satu kesatuan. Ini ditentukan sebagai persentase dari ukuran font, misalnya, 1 = 100%. Ini berarti bahwa dua karakter berukuran 12pt yang ditempatkan 12 pt terpisah dianggap berdekatan.

- RecognitionBullets digunakan untuk mengaktifkan pengenalan bullet selama konversi.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // Tentukan format keluaran sebagai DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // Atur mode pengenalan sebagai Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // Atur kedekatan horizontal sebagai 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // Aktifkan nilai untuk mengenali poin selama proses konversi
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**Coba konversi PDF ke DOC secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas cara kerjanya.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Mengubah PDF ke DOCX

Enumerasi DocFormat juga menyediakan opsi untuk memilih DOCX sebagai format keluaran untuk dokumen Word. Untuk merender file PDF sumber ke format DOCX, gunakan potongan kode yang ditentukan di bawah ini.

## Cara mengubah PDF ke DOCX

Potongan kode Java berikut menunjukkan proses mengubah file PDF menjadi format DOCX.

1. Buat instance objek [Document](https://reference.aspose.com/page/java/com.aspose.page/document) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.DocX** dengan memanggil metode **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // Buka dokumen PDF sumber
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Simpan file DOC yang dihasilkan
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) memiliki properti bernama Format yang menyediakan kemampuan untuk menentukan format dokumen hasil, yaitu, DOC atau DOCX.
 Untuk mengonversi file PDF ke format DOCX, silakan lewati nilai Docx dari enumerasi DocSaveOptions.DocFormat.

Silakan lihat potongan kode berikut yang menyediakan kemampuan untuk mengonversi file PDF ke format DOCX dengan Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // Buka dokumen PDF sumber
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // Instansiasi objek DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // Tentukan format keluaran sebagai DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // Atur parameter DocSaveOptions lainnya
    // ....

    // Simpan dokumen dalam format docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**Cobalah mengonversi PDF ke DOCX secara online**


Aspose.PDF untuk Java menyajikan aplikasi gratis online Anda ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.
[![Aspose.PDF Konversi PDF ke DOCX Aplikasi Gratis](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}