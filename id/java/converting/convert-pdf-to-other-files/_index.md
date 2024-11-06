---
title: Konversi File PDF ke Format Lain 
linktitle: Konversi PDF ke format lain 
type: docs
weight: 90
url: id/java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke format file lain.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Konversi PDF ke EPUB

{{% alert color="success" %}}
**Coba konversi PDF ke EPUB secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (singkatan dari electronic publication) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF).
 Files have the extension .epub.EPUB dirancang untuk konten yang dapat diatur ulang, artinya pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan oleh penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk Java mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk Java memiliki kelas bernama [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) yang dapat digunakan sebagai argumen kedua untuk metode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..), untuk menghasilkan file EPUB. Silakan coba gunakan potongan kode berikut untuk memenuhi kebutuhan ini.

```java
// Muat dokumen PDF
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Instansiasi opsi simpan Epub
EpubSaveOptions options = new EpubSaveOptions();
// Tentukan tata letak untuk konten
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// Simpan dokumen ePUB
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## Konversi PDF ke LaTeX/TeX

**Aspose.PDF untuk Java** mendukung konversi PDF ke LaTeX/TeX. Format file LaTeX adalah format file teks dengan penandaan khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penyusunan berkualitas tinggi.

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) yang menyediakan metode `setOutDirectoryPath` untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses konversi file PDF ke format TEX dengan Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Buat objek Dokumen
Document document = new Document(documentFileName);

// Instansiasi opsi simpan LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// Tentukan direktori output
String pathToOutputDirectory = DATA_DIR.toString();

// Setel jalur direktori output untuk objek opsi simpan
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// Simpan file PDF ke dalam format LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk Java menyajikan aplikasi online gratis ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke Teks

**Aspose.PDF untuk Java** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Konversi seluruh dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan metode Visit dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```java
// Buka dokumen
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Muat dokumen PDF
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// Simpan teks yang diekstrak dalam file teks
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**Coba untuk mengonversi PDF ke Teks secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba untuk menyelidiki fungsi dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Mengonversi halaman PDF ke file teks

Anda dapat mengonversi dokumen PDF ke file TXT dengan Aspose.PDF untuk Java. Anda harus menggunakan metode Visit dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) untuk menyelesaikan tugas ini.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari halaman tertentu.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Memuat dokumen PDF
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// Menyimpan teks yang diekstrak dalam file teks
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## Mengonversi PDF ke XPS

**Aspose.PDF untuk Java** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari coba gunakan cuplikan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Java.

{{% alert color="success" %}}
**Coba mengonversi PDF ke XPS secara online**

Aspose.PDF untuk Java menyajikan aplikasi online gratis ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Tipe file XPS terutama dikaitkan dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya diberi nama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan tampilan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) yang digunakan sebagai argumen kedua untuk konstruktor Document.save(..) untuk menghasilkan file XPS.
 Cuplikan kode berikut menunjukkan proses konversi file PDF ke dalam format XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Buat objek Dokumen
Document document = new Document(documentFileName);

// Instansiasi opsi Simpan XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// Simpan output dalam format XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```