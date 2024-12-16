---
title: Setel Hak Istimewa pada PDF
type: docs
weight: 50
url: /id/net/set-privileges/
description: Topik ini menjelaskan cara menyetel hak istimewa pada file PDF yang ada menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Setel Hak Istimewa pada File PDF yang Ada

Untuk menyetel hak istimewa file PDF, buat objek [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) dan panggil metode SetPrivilege. Anda dapat menentukan hak istimewa menggunakan objek DocumentPrivilege dan kemudian meneruskan objek ini ke metode SetPrivilege. Cuplikan kode berikut menunjukkan cara menyetel hak istimewa dari file PDF.

```csharp
public static void SetPrivilege1()
 {
    // Buat objek DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Buat objek PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

Lihat metode berikut dengan menentukan kata sandi:

```csharp
 public static void SetPrivilege2()
 {
    // Buat objek DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Buat objek PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Hapus Fitur Hak Diperpanjang dari PDF

Dokumen PDF mendukung fitur hak diperpanjang untuk memungkinkan pengguna akhir mengisi data ke dalam bidang formulir dengan menggunakan Adobe Acrobat Reader dan kemudian menyimpan salinan formulir yang telah diisi. Namun, ini memastikan bahwa file PDF tidak dimodifikasi dan jika ada modifikasi pada struktur PDF, fitur hak diperluas akan hilang. Ketika melihat dokumen semacam itu, pesan kesalahan ditampilkan, menyatakan bahwa hak diperluas dihapus karena dokumen telah dimodifikasi. Baru-baru ini, kami menerima permintaan untuk menghapus hak diperluas dari dokumen PDF.

Untuk menghapus hak diperluas dari file PDF, metode baru bernama RemoveUsageRights() telah ditambahkan ke kelas PdfFileSignature. Metode lain bernama ContainsUsageRights() ditambahkan untuk menentukan apakah sumber PDF mengandung hak diperluas.

{{% alert color="primary" %}}
Mulai Aspose.PDF untuk .NET 9.5.0, nama dari metode berikut diperbarui. Harap dicatat bahwa metode sebelumnya masih ada di API tetapi telah ditandai sebagai usang dan akan dihapus. Oleh karena itu, disarankan untuk mencoba menggunakan metode yang diperbarui.

- Metode IsContainSignature(.) diubah namanya menjadi ContainsSignature(..).

- Metode IsCoversWholeDocument(..) diubah namanya menjadi CoversWholeDocument(..).{{% /alert %}}

Kode berikut menunjukkan cara menghapus hak penggunaan dari dokumen:

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```