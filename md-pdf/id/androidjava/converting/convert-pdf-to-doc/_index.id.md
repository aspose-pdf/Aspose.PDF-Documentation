---
title: Mengonversi PDF ke DOC 
linktitle: Mengonversi PDF ke DOC
type: docs
weight: 70
url: /androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Mengonversi file PDF ke format DOC dengan mudah dan kontrol penuh dengan Aspose.PDF untuk Android via Java. Pelajari lebih lanjut bagaimana menyesuaikan konversi file Microsoft Word Doc ke PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Salah satu fitur yang paling populer adalah konversi PDF ke Microsoft Word DOC, yang membuat konten mudah dimanipulasi. Aspose.PDF untuk Android via Java memungkinkan Anda mengonversi file PDF ke DOC.

**Aspose.PDF untuk Android via Java** dapat membuat dokumen PDF dari awal dan merupakan toolkit yang hebat untuk memperbarui, mengedit, dan memanipulasi dokumen PDF yang ada.
 Fitur penting adalah kemampuan untuk mengubah halaman dan seluruh dokumen PDF menjadi gambar. Fitur populer lainnya adalah konversi PDF ke Microsoft Word DOC, yang membuat konten mudah dimanipulasi. (Sebagian besar pengguna tidak dapat mengedit dokumen PDF tetapi dapat dengan mudah bekerja dengan tabel, teks, dan gambar di Microsoft Word.)

Untuk membuat segalanya sederhana dan mudah dipahami, Aspose.PDF untuk Android melalui Java menyediakan kode dua baris untuk mengubah file PDF sumber menjadi file DOC.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Cuplikan kode berikut menunjukkan proses konversi file PDF menjadi format DOC.

```java
 public void convertPDFtoDOC() {
        // Buka dokumen PDF sumber
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Simpan file ke dalam format dokumen MS
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```