---
title: Hapus Tanda Tangan dari File PDF
type: docs
weight: 20
url: id/java/remove-signature-from-pdf/
description: Bagian ini menjelaskan cara bekerja dengan Tanda Tangan dalam File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Hapus Tanda Tangan Digital dari File PDF

Ketika tanda tangan telah ditambahkan ke file PDF, adalah mungkin untuk menghapusnya. Anda dapat menghapus tanda tangan tertentu, atau semua tanda tangan dalam sebuah file. Metode tercepat untuk menghapus tanda tangan juga menghapus bidang tanda tangan, tetapi dimungkinkan untuk hanya menghapus tanda tangan, menyisakan bidang tanda tangan sehingga file dapat ditandatangani lagi.

Metode RemoveSignature kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) memungkinkan Anda menghapus tanda tangan dari file PDF.
 Metode ini mengambil nama tanda tangan sebagai input. Anda dapat menentukan nama tanda tangan secara langsung, untuk menghapus semua tanda tangan, dapatkan nama tanda tangan menggunakan metode [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

Cuplikan kode berikut menunjukkan cara menghapus tanda tangan digital dari file PDF.

```java
 public static void RemoveSignature() {
        // Buat objek PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Buka dokumen PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // Dapatkan daftar nama tanda tangan
        List<String> sigNames = pdfSign.getSignNames();
        // Hapus semua tanda tangan dari file PDF
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removed " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // Simpan file PDF yang telah diperbarui
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### Hapus Tanda Tangan tetapi Pertahankan Bidang Tanda Tangan

Seperti yang ditunjukkan di atas, metode [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) memungkinkan Anda menghapus bidang tanda tangan dari file PDF. Ketika menggunakan metode ini dengan versi sebelum 9.3.0, baik tanda tangan maupun bidang tanda tangan akan dihapus. Beberapa pengembang ingin menghapus hanya tanda tangan dan mempertahankan bidang tanda tangan sehingga dapat digunakan untuk menandatangani kembali dokumen tersebut. Untuk mempertahankan bidang tanda tangan dan hanya menghapus tanda tangan, silakan gunakan cuplikan kode berikut.

```java
 public static void RemoveSignatureButKeepField() {
        // Buat objek PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Buka dokumen PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // Simpan file PDF yang diperbarui
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


Contoh berikut menunjukkan cara menghapus semua tanda tangan dari bidang.

```java
public static void RemoveSignatureButKeepField2() {
        // Buat objek PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Buka dokumen PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // Simpan file PDF yang diperbarui
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```