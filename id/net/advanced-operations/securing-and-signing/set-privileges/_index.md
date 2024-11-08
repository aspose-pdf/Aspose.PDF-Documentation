---
title: Atur Hak Akses, Enkripsi dan Dekripsi PDF
linktitle: Enkripsi dan Dekripsi Berkas PDF
type: docs
weight: 20
url: /id/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Enkripsi Berkas PDF dengan C# menggunakan Berbagai Tipe dan Algoritma Enkripsi. Juga, dekripsi Berkas PDF menggunakan Kata Sandi Pemilik.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Atur Hak Akses, Enkripsi dan Dekripsi PDF",
    "alternativeHeadline": "Cara mengenkripsi dan mendekripsi berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, enkripsi pdf, dekripsi pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Enkripsi Berkas PDF dengan C# menggunakan Berbagai Tipe dan Algoritma Enkripsi. Juga, dekripsi Berkas PDF menggunakan Kata Sandi Pemilik."
}
</script>

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengatur Privilese pada File PDF yang Ada

Untuk mengatur privilese pada file PDF, buat objek dari kelas [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) dan tentukan hak yang ingin Anda terapkan pada dokumen. Setelah privilese telah ditentukan, lewatkan objek ini sebagai argumen ke metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf). Potongan kode berikut menunjukkan cara mengatur privilese dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Muat file PDF sumber
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instansiasi objek Privilese Dokumen
    // Terapkan pembatasan pada semua privilese
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Hanya izinkan pembacaan layar
    documentPrivilege.AllowScreenReaders = true;
    // Enkripsi file dengan kata sandi Pengguna dan Pemilik.
    // Perlu mengatur kata sandi, sehingga begitu pengguna melihat file dengan kata sandi pengguna,
    // Hanya opsi pembacaan layar yang diaktifkan
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Simpan dokumen yang telah diperbarui
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## Mengenkripsi File PDF Menggunakan Berbagai Jenis dan Algoritma Enkripsi

Anda dapat menggunakan metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) untuk mengenkripsi file PDF. Anda dapat memasukkan kata sandi pengguna, kata sandi pemilik, dan izin ke metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Selain itu, Anda dapat memasukkan nilai apa pun dari enum [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Enum ini menyediakan kombinasi yang berbeda dari algoritma enkripsi dan ukuran kunci. Anda dapat memasukkan nilai pilihan Anda. Terakhir, simpan file PDF yang telah dienkripsi menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Harap tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

- **Kata sandi Pengguna**, jika diatur, adalah apa yang Anda butuhkan untuk memberikan untuk membuka PDF.
- **Kata Sandi Pengguna**, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF.
- **Kata Sandi Pemilik**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal-hal tersebut berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

Berikut ini potongan kode yang menunjukkan cara mengenkripsi file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Buka dokumen
Document document = new Document(dataDir+ "Encrypt.pdf");
// Enkripsi PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Simpan PDF yang telah diperbarui
document.Save(dataDir);
```

## Mendekripsi File PDF menggunakan Kata Sandi Pemilik

Semakin banyak, pengguna bertukar file PDF dengan enkripsi untuk mencegah akses tidak sah ke dokumen, seperti mencetak/menyalin/membagi/mengekstrak informasi tentang isi file PDF.
Semakin banyak, pengguna bertukar file PDF yang dienkripsi untuk mencegah akses tidak sah ke dokumen, seperti mencetak/menyalin/membagi/mengekstrak informasi tentang isi file PDF.
Dalam hal ini, ada kebutuhan untuk mengakses file PDF yang terenkripsi, karena akses seperti itu hanya bisa diperoleh oleh pengguna yang berwenang. Juga, orang mencari berbagai solusi untuk mendekripsi file PDF melalui Internet.

Lebih baik untuk menyelesaikan masalah ini sekali dengan menggunakan perpustakaan Aspose.PDF.

Untuk mendekripsi file PDF, Anda pertama-tama perlu membuat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan membuka PDF menggunakan kata sandi pemilik.
Untuk mendekripsi file PDF, Anda pertama-tama perlu membuat objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan membuka PDF menggunakan kata sandi pemilik.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Buka dokumen
Document document = new Document(dataDir + "Decrypt.pdf", "password");
// Dekripsi PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Simpan PDF yang telah diperbarui
document.Save(dataDir);
```

## Mengubah Kata Sandi File PDF

Jika Anda ingin mengubah kata sandi file PDF, Anda pertama-tama perlu membuka file PDF menggunakan kata sandi pemilik dengan objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Jika Anda ingin mengubah kata sandi dari file PDF, Anda terlebih dahulu perlu membuka file PDF menggunakan kata sandi pemilik dengan objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- Kata sandi Pengguna, jika diatur, adalah apa yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
>- Kata sandi Pemilik, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

Potongan kode berikut menunjukkan cara mengubah kata sandi dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Buka dokumen
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// Ubah kata sandi
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Simpan PDF yang telah diperbarui
document.Save(dataDir);
```
## Cara Menentukan Apakah PDF Bersumber Dilindungi Kata Sandi

**Aspose.PDF for .NET** menyediakan kemampuan hebat dalam menangani dokumen PDF. Saat menggunakan kelas Dokumen dari namespace Aspose.PDF untuk membuka dokumen PDF yang dilindungi kata sandi, kita perlu menyediakan informasi kata sandi sebagai argumen ke konstruktor Dokumen dan jika informasi ini tidak disediakan, pesan kesalahan akan dihasilkan. Sebenarnya, saat mencoba membuka file PDF dengan objek Dokumen, konstruktor mencoba membaca isi file PDF dan jika kata sandi yang benar tidak disediakan, pesan kesalahan dihasilkan (hal ini terjadi untuk mencegah akses tidak sah terhadap dokumen)

Saat menangani file PDF yang terenkripsi, Anda mungkin menemukan skenario di mana Anda tertarik untuk mendeteksi apakah PDF memiliki kata sandi buka dan/atau kata sandi edit.
Saat berurusan dengan file PDF terenkripsi, Anda mungkin menemukan skenario di mana Anda tertarik untuk mendeteksi apakah PDF memiliki kata sandi buka dan/atau kata sandi edit.

### Dapatkan informasi tentang keamanan dokumen PDF

PdfFileInfo memiliki tiga properti untuk mendapatkan informasi tentang keamanan dokumen PDF.

1. property PasswordType mengembalikan nilai enumerasi PasswordType:
    - PasswordType.None - dokumen tidak dilindungi kata sandi
    - PasswordType.User - dokumen dibuka dengan kata sandi pengguna (atau kata sandi buka dokumen)
    - PasswordType.Owner - dokumen dibuka dengan kata sandi pemilik (atau kata sandi izin, edit)
    - PasswordType.Inaccessible - dokumen dilindungi kata sandi tetapi kata sandi diperlukan untuk membukanya sementara kata sandi yang tidak valid (atau tanpa kata sandi) disediakan.
2. properti boolean HasOpenPassword - digunakan untuk menentukan apakah file masukan memerlukan kata sandi saat membukanya.
3. properti boolean HasEditPassword - digunakan untuk menentukan apakah file masukan memerlukan kata sandi untuk mengedit isinya.

### Tentukan kata sandi yang benar dari Array
### Tentukan password yang benar dari Array

Terkadang ada kebutuhan untuk menentukan password yang benar dari serangkaian password dan membuka dokumen dengan password yang benar. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengulang melalui array password dan mencoba membuka dokumen dengan password yang benar.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Muat file PDF sumber
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Tentukan jika PDF sumber dienkripsi
Console.WriteLine("File terproteksi password " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Jumlah Halaman dalam dokumen adalah = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + " tidak benar");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

