---
title: Konversi PDF ke Microsoft PowerPoint 
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF memungkinkan Anda untuk mengonversi PDF ke format PowerPoint menggunakan PHP. Salah satu caranya adalah dengan mengonversi PDF ke PPTX dengan Slide sebagai Gambar.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF untuk PHP** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX.
Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Dalam Aspose.PDF untuk PHP, kami telah memperkenalkan fitur untuk mengubah dokumen PDF menjadi format PPTX. Selama konversi ini, halaman individu dari file PDF diubah menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke PPTX, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya, bukan dirender sebagai gambar.
 Silakan perhatikan bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama PptxSaveOptions. Sebuah objek dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) diberikan sebagai argumen kedua ke metode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Periksa cuplikan kode berikut untuk menyelesaikan tugas Anda dengan konversi PDF ke format PowerPoint:

```php
// Memuat dokumen PDF input
$document = new Document($inputFile);

// Membuat instance dari PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Menyimpan dokumen PDF sebagai file PPTX
$document->save($outputFile, $saveOption);
```

## Mengonversi PDF ke PPTX dengan Slide sebagai Gambar

Jika Anda perlu mengonversi PDF yang dapat dicari ke PPTX sebagai gambar alih-alih teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Untuk mencapai ini, setel properti SlidesAsImages dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) ke 'true' seperti yang ditunjukkan dalam contoh kode berikut.

Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF ke dalam format PPTX Slides sebagai Gambar.

```php
// Muat dokumen PDF input
$document = new Document($inputFile);

// Buat instance dari PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Simpan dokumen PDF sebagai file PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Muat dokumen PDF
        Document doc = new Document(pdfDocumentFileName);
        // Instansiasi instance PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Simpan output dalam format PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke PowerPoint secara online**

Aspose.PDF untuk PHP mempersembahkan aplikasi gratis online ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}