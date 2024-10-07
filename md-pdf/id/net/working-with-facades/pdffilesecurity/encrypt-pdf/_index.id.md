---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: Topik ini menjelaskan cara Mengenkripsi File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Mengenkripsi dokumen PDF melindungi isinya dari akses tidak sah dari luar, terutama selama berbagi atau pengarsipan file.

Dokumen PDF rahasia dapat dienkripsi dan dilindungi kata sandi. Hanya pengguna yang mengetahui kata sandi yang akan dapat mendekripsi, membuka, dan melihat dokumen-dokumen ini.

Mari kita lihat bagaimana enkripsi PDF bekerja dengan perpustakaan Aspose.PDF.

## Mengenkripsi File PDF menggunakan Berbagai Jenis Enkripsi dan Algoritma

Untuk mengenkripsi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Anda dapat meneruskan kata sandi pengguna, kata sandi pemilik, dan hak istimewa ke metode [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Anda juga perlu meneruskan nilai KeySize dan Algorithm ke metode ini.

Tinjau daftar kemungkinan [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm):

|**Nama anggota**|**Nilai**|**Deskripsi**|
| :- | :- | :- |
|RC4x40|0|RC4 dengan panjang kunci 40.|
|RC4x128|1|RC4 dengan panjang kunci 128.|
|AESx128|2|AES dengan panjang kunci 128.|
|AESx256|3|AES dengan panjang kunci 256.|

Cuplikan kode berikut menunjukkan kepada Anda cara mengenkripsi file PDF.

```csharp
public static void EncryptPDFFile()
        {
            // Buat objek PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // Enkripsi file menggunakan enkripsi 256-bit
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```