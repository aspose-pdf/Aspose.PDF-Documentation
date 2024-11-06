---
title: Mengubah PDF ke PowerPoint 
linktitle: Mengubah PDF ke PowerPoint
type: docs
weight: 110
url: id/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF memungkinkan Anda mengubah PDF ke format PowerPoint. Salah satu caranya adalah dengan mengubah PDF ke PPTX dengan Slide sebagai Gambar.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengubah file PPT/PPTX ke format PDF. Dalam Aspose.PDF untuk Java, kami telah memperkenalkan fitur untuk mengubah dokumen PDF menjadi format PPTX. Selama konversi ini, halaman individu dari file PDF diubah menjadi slide terpisah dalam file PPTX.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Selama konversi PDF ke PPTX, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya, alih-alih dirender sebagai gambar. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama PptxSaveOptions. Objek dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) diteruskan sebagai argumen kedua ke metode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Periksa cuplikan kode berikut untuk menyelesaikan tugas Anda dengan konversi PDF ke format PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Memuat dokumen PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Membuat objek ExcelSave Option
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Menyimpan keluaran dalam format PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Menyimpan file ke dalam format PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```