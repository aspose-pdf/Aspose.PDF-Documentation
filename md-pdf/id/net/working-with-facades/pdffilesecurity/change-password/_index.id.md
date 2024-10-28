---
title: Ubah Kata Sandi File PDF
type: docs
weight: 40
url: /net/change-password/
description: Topik ini menjelaskan cara mengubah kata sandi pada File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Ubah Kata Sandi File PDF

Untuk mengubah kata sandi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Anda perlu memberikan kata sandi pemilik yang ada dan kata sandi pengguna dan pemilik baru ke metode [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- **Kata sandi Pengguna**, jika disetel, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi Pemilik**, jika disetel, mengontrol izin, seperti pencetakan, pengeditan, ekstraksi, komentar, dll. Acrobat/Reader akan menolak hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara mengubah kata sandi dari file PDF.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Buat objek PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```