---
title: Decrypt PDF File
type: docs
weight: 20
url: id/net/decrypt-pdf-file/
description: Topik ini menjelaskan cara Mendekripsi File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Dokumen PDF yang dienkripsi dengan kata sandi atau sertifikat harus dibuka sebelum operasi lain dapat dilakukan. Jika Anda mencoba untuk mengoperasikan dokumen PDF yang dienkripsi, Anda akan mendapatkan pengecualian. Setelah membuka kunci PDF yang dienkripsi, Anda dapat melakukan satu atau lebih operasi pada dokumen tersebut.

## Mendekripsi File PDF menggunakan Kata Sandi Pemilik

{{% alert color="primary" %}}
Coba online <br>
Anda dapat mencoba membuka kunci dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Untuk mendekripsi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Anda juga perlu memasukkan kata sandi pemilik ke metode [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Cuplikan kode berikut menunjukkan cara mendekripsi file PDF.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Buat objek PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Mendekripsi dokumen PDF
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```