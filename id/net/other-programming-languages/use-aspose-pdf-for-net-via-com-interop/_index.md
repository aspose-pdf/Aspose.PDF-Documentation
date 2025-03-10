---
title: Aspose.PDF for .NET melalui COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/use-aspose-pdf-for-net-via-com-interop/
description: Temukan cara menggunakan Aspose.PDF for .NET melalui COM Interop untuk integrasi yang mulus dengan aplikasi non-.NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET sekarang mendukung integrasi yang mulus dengan berbagai bahasa pemrograman melalui COM Interop, memungkinkan pengembang untuk memanfaatkan kemampuan manipulasi PDF yang kuat di luar kerangka kerja .NET. Fitur ini meningkatkan fleksibilitas dengan mengubah objek Aspose.PDF menjadi objek COM, menyederhanakan interaksi dengan kode tidak terkelola sambil mempertahankan kinerja tinggi melalui teknik pengikatan awal dan akhir.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Informasi dalam topik ini berlaku untuk skenario di mana Anda ingin menggunakan [Aspose.PDF for .NET](/pdf/net/) melalui COM Interop dalam salah satu bahasa pemrograman berikut:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Bekerja dengan COM Interop

Aspose.PDF for .NET dijalankan di bawah kendali .NET Framework dan ini disebut kode terkelola. Kode yang ditulis dalam semua bahasa di atas berjalan di luar .NET Framework dan disebut kode tidak terkelola. Interaksi antara kode tidak terkelola dan Aspose.PDF terjadi melalui fasilitas .NET yang disebut COM Interop.

Objek Aspose.PDF adalah objek .NET, tetapi ketika digunakan melalui COM Interop, mereka muncul sebagai objek COM dalam bahasa pemrograman Anda. Oleh karena itu, sebaiknya pastikan Anda tahu cara membuat dan menggunakan objek COM dalam bahasa pemrograman Anda, sebelum Anda mulai menggunakan [Aspose.PDF for .NET](/pdf/net/).

{{% alert color="primary" %}}

- Di dunia COM kita membedakan antara server COM dan klien COM. Server COM menyimpan kelas COM sementara klien COM meminta server COM untuk instance kelas, yaitu objek COM.
- Klien COM atau aplikasi klien sederhana dapat mengetahui tentang konten kelas COM atau tidak sama sekali menyadari metode dan propertinya. Oleh karena itu, aplikasi klien dapat menemukan struktur kelas COM saat kompilasi/membangun atau hanya selama eksekusi. Proses "penemuan" ini dikenal sebagai pengikatan dan kita memiliki **pengikatan awal** dan **pengikatan akhir**.
- secara singkat kelas COM seperti kotak hitam dan untuk bekerja dengannya, pustaka tipe diperlukan, file biner ini memiliki deskripsi metode, properti kelas COM dan bahasa tingkat tinggi mana pun yang mendukung bekerja dengan objek COM sering memiliki ekspresi sintaks untuk menambahkan pustaka tipe, misalnya ini adalah [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) dalam C++.
- pustaka tipe digunakan untuk pengikatan awal.
- objek COM dapat mengekspos metode dan propertinya dengan dua cara: melalui **antarmuka pengiriman** (dispinterface) dan dalam **vtable** (tabel fungsi virtual).
- dalam **dispinterface**, setiap metode dan properti diidentifikasi oleh anggota unik; anggota ini adalah pengidentifikasi pengiriman fungsi (atau **DispID**).
- **vtable** hanyalah sekumpulan pointer ke fungsi yang didukung oleh antarmuka kelas COM.
- objek yang mengekspos metodenya melalui kedua antarmuka mendukung **antarmuka ganda**.
- ada keuntungan untuk kedua jenis pengikatan. Pengikatan awal memberi Anda peningkatan kinerja dan pemeriksaan sintaks waktu kompilasi. Pengikatan akhir paling menguntungkan ketika Anda menulis klien yang Anda maksudkan untuk ***kompatibel dengan versi mendatang*** dari kelas COM Anda. Dengan pengikatan akhir, informasi dari pustaka tipe tidak "terkait keras" ke klien Anda, sehingga Anda dapat memiliki keyakinan yang lebih besar bahwa klien Anda dapat bekerja dengan versi mendatang dari kelas COM tanpa perubahan kode.
- mekanisme pengikatan akhir memiliki keuntungan besar: jika pembuat DLL COM memutuskan untuk merilis versi baru, dengan tata letak antarmuka fungsi yang berbeda, kode apa pun yang memanggil metode tersebut tidak akan crash kecuali metode tersebut tidak lagi tersedia; bahkan jika **vtable** berbeda, pengikatan akhir berhasil menemukan DISPIDs baru dan memanggil metode yang sesuai.
{{% /alert %}}

Berikut adalah topik yang perlu Anda kuasai:
{{% alert color="primary" %}}

- Menggunakan objek COM dalam bahasa pemrograman Anda. Lihat dokumentasi bahasa pemrograman Anda dan topik spesifik bahasa lebih lanjut dalam dokumentasi ini.

- Bekerja dengan objek COM yang diekspos oleh .NET COM Interop. Lihat [Interoperasi Dengan Kode Tidak Terkelola](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) dan [Mengekspos Komponen .NET Framework ke COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) di MSDN.

- Model objek dokumen Aspose.PDF. Lihat [Panduan Programmer Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) dan [Referensi API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Mendaftarkan Aspose.PDF for .NET dengan COM Interop

Anda perlu menginstal Aspose.PDF for .NET dan memastikan bahwa itu terdaftar dengan COM Interop (memastikan bahwa itu dapat dipanggil dari kode tidak terkelola).

{{% alert color="primary" %}}

Untuk mendaftarkan Aspose.PDF for .NET untuk COM Interop secara manual:

1. Dari menu **Start**, pilih **All Programs**, kemudian **Microsoft Visual Studio**, **Visual Studio Tools** dan, akhirnya, **Visual Studio Command Prompt**.
1. Masukkan perintah untuk mendaftarkan assembly:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Perhatikan bahwa /codebase hanya diperlukan jika Aspose.PDF.dll tidak ada di GAC, menggunakan opsi ini membuat regasm menempatkan jalur untuk assembly di registri.

{{% alert color="primary" %}}

regasm.exe adalah alat yang disertakan dalam .NET Framework SDK. Semua alat .NET Framework SDK terletak di direktori *\Microsoft .NET\Framevork\<FrameworkVersion>*, misalnya *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Jika Anda menggunakan Visual Studio .NET:
Dari menu **Start**, pilih **Programs**, diikuti oleh **Visual Studio 2022**, akhirnya, **Developer Command Prompt for VS 2022**.
Ini menjalankan prompt perintah dengan semua variabel lingkungan yang diperlukan diatur.

{{% /alert %}}

### ProgIDs

ProgID adalah singkatan dari “identifikasi programatik”. Ini adalah nama kelas COM yang digunakan untuk membuat objek. ProgIDs terdiri dari nama pustaka "Aspose.PDF" dan nama kelas.

### Pustaka Tipe

{{% alert color="primary" %}}

Jika bahasa pemrograman Anda (misalnya Visual Basic atau Delphi) memungkinkan Anda untuk merujuk pustaka tipe COM, maka tambahkan referensi ke Aspose.PDF.tlb dan untuk melihat semua kelas, metode, properti, dan enumerasi Aspose.PDF for .NET di Browser Objek Anda.

Untuk menghasilkan file TLB:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Membuat Objek COM

Pembuatan objek COM mirip dengan pembuatan objek .NET biasa:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

Setelah dibuat, Anda dapat mengakses metode dan properti objek, seolah-olah itu adalah objek COM:

```vb
'Add page to the document
document.Pages.Add()
```

Beberapa metode memiliki overload dan mereka akan diekspos oleh COM Interop dengan akhiran numerik ditambahkan ke mereka, kecuali untuk metode pertama yang tetap tidak berubah. Misalnya, overload metode Document.Save menjadi Document.Save, Document.Save_2, dan seterusnya.

Untuk informasi lebih lanjut, lihat artikel spesifik bahasa lebih lanjut dalam dokumentasi ini.

## Membuat Assembly Pembungkus

Jika Anda perlu menggunakan banyak kelas, metode, dan properti Aspose.PDF for .NET, pertimbangkan untuk membuat assembly pembungkus (menggunakan C# atau bahasa pemrograman .NET lainnya). Assembly pembungkus membantu menghindari penggunaan Aspose.PDF for .NET secara langsung dari kode tidak terkelola.

Pendekatan yang baik adalah mengembangkan assembly .NET yang merujuk Aspose.PDF for .NET dan melakukan semua pekerjaan dengannya, dan hanya mengekspos seperangkat kelas dan metode minimal ke kode tidak terkelola. Aplikasi Anda kemudian harus bekerja hanya dengan pustaka pembungkus Anda.

Mengurangi jumlah kelas dan metode yang perlu Anda panggil melalui COM Interop menyederhanakan proyek. Menggunakan kelas .NET melalui COM Interop sering kali memerlukan keterampilan tingkat lanjut.