---
title: Konversi PDF ke PowerPoint
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 110
url: /id/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF memungkinkan Anda mengonversi PDF ke format PowerPoint. Salah satu cara adalah kemungkinan untuk mengonversi PDF ke PPTX dengan Slide sebagai Gambar.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Pada Aspose.PDF for Java, kami telah memperkenalkan fitur untuk mengubah dokumen PDF menjadi format PPTX. Selama konversi ini, halaman individu dari file PDF dikonversi menjadi slide terpisah dalam file PPTX.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Selama konversi PDF ke PPTX, teks dirender sebagai Teks yang dapat Anda pilih/perbarui, bukan sebagai gambar. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama PptxSaveOptions. Sebuah objek dari [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) kelas diteruskan sebagai argumen kedua ke [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)metode .save(..)

Periksa potongan kode berikut untuk menyelesaikan tugas Anda dengan konversi PDF ke format PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

