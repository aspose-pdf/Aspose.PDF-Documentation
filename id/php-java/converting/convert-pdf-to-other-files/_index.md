---
title: Konversi file PDF ke format lain
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: id/php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: Topik ini menunjukkan cara Aspose.PDF memungkinkan konversi file PDF ke format file lain.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Konversi PDF ke EPUB

{{% alert color="success" %}}
**Coba konversi PDF ke EPUB secara online**

Aspose.PDF untuk PHP menyajikan aplikasi online gratis ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba meneliti fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (singkatan dari electronic publication) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF).
 Files have the extension .epub.EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan penerbit dan rumah konversi di dalam rumah, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk PHP mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk PHP memiliki kelas bernama [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) yang dapat digunakan sebagai argumen kedua untuk metode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) untuk menghasilkan file EPUB. Silakan coba gunakan potongan kode berikut untuk memenuhi persyaratan ini.

```php
// Buat instance baru dari kelas Document dan muat file PDF input
$document = new Document($inputFile);

// Buat instance baru dari kelas EpubSaveOptions
$saveOption = new EpubSaveOptions();

// Simpan dokumen dalam format EPUB menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOption);
```

## Konversi PDF ke LaTeX/TeX

**Aspose.PDF untuk PHP** mendukung konversi PDF ke LaTeX/TeX. Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk typesetting berkualitas tinggi.

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) yang menyediakan metode `setOutDirectoryPath` untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses konversi file PDF ke format TEX dengan Java.

```php
// Buat objek Document baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek LaTeXSaveOptions baru
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Simpan dokumen sebagai LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk PHP mempersembahkan aplikasi online gratis ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke Teks

**Aspose.PDF untuk PHP** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Mengonversi seluruh dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan metode Visit dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Cuplikan kode berikut menjelaskan cara mengekstraksi teks dari semua halaman.

```php
// Memuat dokumen PDF
$document = new Document($inputFile);

// Membuat objek TextAbsorber untuk mengekstrak teks dari dokumen
$textAbsorber = new TextAbsorber();

// Mengekstrak teks dari dokumen
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Menyimpan teks yang diekstraksi ke file output
file_put_contents($outputFile, $content);

// Mendapatkan ukuran file dari file output
$fileSize = filesize($outputFile);
```


{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke Teks secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi online gratis ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Konversi halaman PDF ke file teks

Anda dapat mengonversi dokumen PDF ke file TXT dengan Aspose.PDF untuk PHP. Anda harus menggunakan metode Visit dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) untuk menyelesaikan tugas ini.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari halaman tertentu.

```php
// Muat dokumen PDF
$document = new Document($inputFile);

// Buat objek TextAbsorber untuk mengekstrak teks dari dokumen
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Simpan teks yang diekstrak ke dalam file output
    file_put_contents($outputFile, $content);
}
```


## Convert PDF to XPS

**Aspose.PDF untuk PHP** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Java.

{{% alert color="success" %}}
**Coba mengonversi PDF ke XPS secara online**

Aspose.PDF untuk PHP memberikan Anda aplikasi gratis online ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Tipe file XPS terutama dikaitkan dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya bernama kode Metro dan mencakup konsep pemasaran Jalur Cetak Generasi Berikutnya (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) yang digunakan sebagai argumen kedua untuk konstruktor Document.save(..) untuk menghasilkan file XPS.
 The following code snippet shows the process of converting PDF files into XPS format.

```php
// Buat objek Document baru dan muat file PDF masukan
$document = new Document($inputFile);

// Buat objek XpsSaveOptions baru
$saveOption = new XpsSaveOptions();

// Simpan dokumen sebagai XPS menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOption);
```