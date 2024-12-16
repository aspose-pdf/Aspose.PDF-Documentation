---
title: Remove Signature from PDF File
type: docs
weight: 20
url: /id/net/remove-signature-from-pdf/
description: Bagian ini menjelaskan cara menghapus tanda tangan dari File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Hapus Tanda Tangan Digital dari File PDF

Ketika tanda tangan telah ditambahkan ke file PDF, mungkin untuk menghapusnya. Anda dapat menghapus baik tanda tangan tertentu, atau semua tanda tangan dalam file. Metode tercepat untuk menghapus tanda tangan juga menghapus bidang tanda tangan, tetapi mungkin untuk hanya menghapus tanda tangan, mempertahankan bidang tanda tangan sehingga file dapat ditandatangani lagi.

Metode RemoveSignature kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk menghapus tanda tangan dari file PDF. Metode ini mengambil nama tanda tangan sebagai input. Anda dapat menentukan nama tanda tangan secara langsung, untuk menghapus semua tanda tangan, dapatkan nama tanda tangan menggunakan metode [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

Cuplikan kode berikut menunjukkan cara menghapus tanda tangan digital dari file PDF.

```csharp
 public static void RemoveSignature()
        {
            // Buat objek PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // Buka dokumen PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // Dapatkan daftar nama tanda tangan
            var sigNames = pdfSign.GetSignNames();
            // Hapus semua tanda tangan dari file PDF
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // Simpan file PDF yang diperbarui
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### Hapus Tanda Tangan tetapi Tetap Pertahankan Bidang Tanda Tangan

Seperti yang ditunjukkan di atas, metode [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) memungkinkan Anda menghapus bidang tanda tangan dari file PDF. Saat menggunakan metode ini dengan versi sebelum 9.3.0, baik tanda tangan maupun bidang tanda tangan akan dihapus. Beberapa pengembang ingin menghapus hanya tanda tangan dan mempertahankan bidang tanda tangan sehingga dapat digunakan untuk menandatangani ulang dokumen. Untuk mempertahankan bidang tanda tangan dan hanya menghapus tanda tangan, silakan gunakan cuplikan kode berikut.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // Buat objek PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Buka dokumen PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // Simpan file PDF yang diperbarui
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

Contoh berikut menunjukkan cara menghapus semua tanda tangan dari bidang.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // Buat objek PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Buka dokumen PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // Simpan file PDF yang diperbarui
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```