---
title: Konversi PDF ke DOC
linktitle: Konversi PDF ke DOC
type: docs
weight: 70
url: /id/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: Konversi file PDF ke format DOC dengan mudah dan kontrol penuh dengan Aspose.PDF for Android via Java. Pelajari lebih lanjut cara menyempurnakan konversi file Microsoft Word Doc ke PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang memudahkan manipulasi konten. Aspose.PDF for Android via Java memungkinkan Anda mengonversi file PDF ke DOC.

**Aspose.PDF for Android via Java** dapat membuat dokumen PDF dari awal dan merupakan toolkit yang hebat untuk memperbarui, mengedit, dan memanipulasi dokumen PDF yang ada. Fitur penting adalah kemampuan untuk mengonversi halaman dan seluruh dokumen PDF menjadi gambar. Fitur populer lainnya adalah konversi PDF ke Microsoft Word DOC, yang memudahkan manipulasi konten. (Sebagian besar pengguna tidak dapat mengedit dokumen PDF tetapi dapat dengan mudah bekerja dengan tabel, teks, dan gambar di Microsoft Word.)

Untuk membuat semuanya sederhana dan mudah dipahami, Aspose.PDF for Android via Java menyediakan kode dua baris untuk mengubah file PDF sumber menjadi file DOC.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Potongan kode berikut menunjukkan proses mengonversi file PDF ke format DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


