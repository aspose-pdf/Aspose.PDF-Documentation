---
title: Atur Hak, Enkripsi dan Dekripsi PDF
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Enkripsi File PDF dengan C# menggunakan Berbagai Jenis dan Algoritma Enkripsi. Juga, dekripsi File PDF menggunakan Kata Sandi Pemilik.
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "Fitur baru ini memungkinkan pengguna untuk secara efisien mengenkripsi dan mendekripsi file PDF menggunakan C# dengan berbagai jenis dan algoritma enkripsi. Dengan memanfaatkan kata sandi pengguna dan pemilik, fitur ini memberikan kontrol yang kuat atas akses dan izin dokumen, memastikan kerahasiaan dan integritas konten PDF sambil menyederhanakan manajemen keamanan bagi pengembang.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Enkripsi File PDF dengan C# menggunakan Berbagai Jenis dan Algoritma Enkripsi. Juga, dekripsi File PDF menggunakan Kata Sandi Pemilik."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Atur Hak pada File PDF yang Ada

Untuk mengatur hak pada file PDF, buat objek dari kelas [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) dan tentukan hak yang ingin Anda terapkan pada dokumen. Setelah hak ditentukan, berikan objek ini sebagai argumen ke metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Potongan kode berikut menunjukkan cara mengatur hak file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## Enkripsi File PDF menggunakan Berbagai Jenis dan Algoritma Enkripsi

Anda dapat menggunakan metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) untuk mengenkripsi file PDF. Anda dapat memberikan kata sandi pengguna, kata sandi pemilik, dan izin ke metode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Selain itu, Anda dapat memberikan nilai apa pun dari enum [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Enum ini menyediakan berbagai kombinasi algoritma enkripsi dan ukuran kunci. Anda dapat memberikan nilai pilihan Anda. Akhirnya, simpan file PDF yang telah dienkripsi menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Silakan tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

- **Kata sandi pengguna**, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi pemilik**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal-hal ini berdasarkan pengaturan izin. Acrobat akan meminta kata sandi ini jika Anda ingin mengatur/mengubah izin.

Potongan kode berikut menunjukkan cara mengenkripsi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Semakin banyak, pengguna bertukar file PDF dengan enkripsi untuk mencegah akses tidak sah ke dokumen, seperti mencetak/mengcopy/membagikan / mengekstrak informasi tentang konten file PDF. Saat ini, ini adalah pilihan terbaik untuk mengenkripsi file PDF karena menjaga kerahasiaan dan integritas konten.
Dalam hal ini, ada kebutuhan untuk mengakses file PDF yang dienkripsi, karena akses tersebut hanya dapat diperoleh oleh pengguna yang berwenang. Selain itu, orang-orang mencari berbagai solusi untuk mendekripsi file PDF di Internet.

Lebih baik menyelesaikan masalah ini sekali dengan menggunakan pustaka Aspose.PDF.

Untuk mendekripsi file PDF, Anda pertama-tama perlu membuat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan membuka PDF menggunakan kata sandi pemilik. Setelah itu, Anda perlu memanggil metode [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Akhirnya, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Potongan kode berikut menunjukkan cara mendekripsi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## Ubah Kata Sandi File PDF

Jika Anda ingin mengubah kata sandi file PDF, Anda pertama-tama perlu membuka file PDF menggunakan kata sandi pemilik dengan objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Setelah itu, Anda perlu memanggil metode [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Anda perlu memberikan kata sandi pemilik saat ini bersama dengan kata sandi pengguna baru dan kata sandi pemilik baru ke metode ini. Akhirnya, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- Kata sandi pengguna, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
>- Kata sandi pemilik, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal-hal ini berdasarkan pengaturan izin. Acrobat akan meminta kata sandi ini jika Anda ingin mengatur/mengubah izin.

Potongan kode berikut menunjukkan cara mengubah kata sandi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## Cara - menentukan apakah PDF sumber dilindungi kata sandi

**Aspose.PDF for .NET** menyediakan kemampuan hebat untuk menangani dokumen PDF. Saat menggunakan kelas Document dari namespace Aspose.PDF untuk membuka dokumen PDF yang dilindungi kata sandi, kita perlu memberikan informasi kata sandi sebagai argumen ke konstruktor Document dan jika informasi ini tidak diberikan, pesan kesalahan akan dihasilkan. Sebenarnya, saat mencoba membuka file PDF dengan objek Document, konstruktor mencoba membaca konten file PDF dan jika kata sandi yang benar tidak diberikan, pesan kesalahan dihasilkan (ini terjadi untuk mencegah akses tidak sah ke dokumen).

Saat menangani file PDF yang dienkripsi, Anda mungkin menemui skenario di mana Anda ingin mendeteksi apakah PDF memiliki kata sandi buka dan/atau kata sandi edit. Terkadang ada dokumen yang tidak memerlukan informasi kata sandi saat membukanya, tetapi memerlukan informasi untuk mengedit konten file. Jadi untuk memenuhi persyaratan di atas, kelas PdfFileInfo yang ada di bawah Aspose.PDF.Facades menyediakan properti yang dapat membantu dalam menentukan informasi yang diperlukan.

### Dapatkan informasi tentang keamanan dokumen PDF

PdfFileInfo memiliki tiga properti untuk mendapatkan informasi tentang keamanan dokumen PDF.

1. properti PasswordType mengembalikan nilai enumerasi PasswordType:
    - PasswordType.None - dokumen tidak dilindungi kata sandi.
    - PasswordType.User - dokumen dibuka dengan kata sandi pengguna (atau kata sandi buka dokumen).
    - PasswordType.Owner - dokumen dibuka dengan kata sandi pemilik (atau izin, edit).
    - PasswordType.Inaccessible - dokumen dilindungi kata sandi tetapi kata sandi diperlukan untuk membukanya sementara kata sandi yang tidak valid (atau tidak ada kata sandi) diberikan.
2. properti boolean HasOpenPassword - digunakan untuk menentukan apakah file input memerlukan kata sandi saat membukanya.
3. properti boolean HasEditPassword - digunakan untuk menentukan apakah file input memerlukan kata sandi untuk mengedit kontennya.

### Menentukan kata sandi yang benar dari Array

Terkadang ada kebutuhan untuk menentukan kata sandi yang benar dari array kata sandi dan membuka dokumen dengan kata sandi yang benar. Potongan kode berikut menunjukkan langkah-langkah untuk mengiterasi melalui array kata sandi dan mencoba membuka dokumen dengan kata sandi yang benar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
        }
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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