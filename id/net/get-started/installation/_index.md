---
title: Cara Menginstal Aspose.PDF for .NET
linktitle: Instalasi
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/installation/
description: Bagian ini menunjukkan deskripsi produk dan instruksi untuk menginstal Aspose.PDF for .NET secara mandiri, serta menggunakan NuGet.
lastmod: "2024-09-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Install Aspose.PDF for .NET",
    "alternativeHeadline": "Seamless PDF Creation with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET adalah komponen yang kuat yang memungkinkan pengembang untuk menghasilkan dan memanipulasi dokumen PDF secara programatis tanpa bergantung pada Adobe Acrobat. Dengan dukungan untuk menyisipkan elemen kompleks seperti tabel, gambar, dan font kustom, serta fitur keamanan yang kuat dan integrasi yang mulus melalui NuGet, alat serbaguna ini meningkatkan produktivitas dan efisiensi dalam aplikasi .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Aspose.PDF, PDF documents, .NET component, NuGet installation, C# API, Temporary License, multithread safe, eval version limitations, .NET Core support, font installation",
    "wordcount": "1214",
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
    "url": "/net/installation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/installation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Komponen Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF adalah komponen .NET** yang dibangun untuk memungkinkan pengembang membuat dokumen PDF, baik sederhana maupun kompleks, secara programatis. Aspose.PDF for .NET memungkinkan pengembang untuk menyisipkan tabel, grafik, gambar, hyperlink, font kustom - dan lebih banyak lagi - ke dalam dokumen PDF. Selain itu, juga dimungkinkan untuk mengompres dokumen PDF. Aspose.PDF for .NET menyediakan fitur keamanan yang sangat baik untuk mengembangkan dokumen PDF yang aman. Dan fitur paling khas dari Aspose.PDF for .NET adalah bahwa ia mendukung pembuatan dokumen PDF melalui API dan dari template XML.

{{% /alert %}}

## Deskripsi Produk

**Aspose.PDF for .NET** adalah komponen .NET yang kuat yang memungkinkan pengembang membuat dokumen PDF dari awal tanpa menggunakan Adobe Acrobat. Ini menyediakan Antarmuka Pemrograman Aplikasi (API) yang sederhana yang mudah dipelajari dan digunakan.

**Aspose.PDF for .NET** diimplementasikan menggunakan Managed C# dan dapat digunakan dengan bahasa .NET apa pun seperti C#, VB.NET, dan J# dll. Ini dapat diintegrasikan dengan jenis aplikasi apa pun baik itu Aplikasi Web ASP.NET atau Aplikasi Windows.

Agar pengembang dapat segera mulai, Aspose.PDF for .NET menyediakan demo lengkap dan contoh kerja yang ditulis dalam C#. Menggunakan demo ini, pengembang dapat dengan cepat mempelajari fitur-fitur yang disediakan oleh Aspose.PDF for .NET.

Komponen yang cepat dan ringan ini membuat dokumen PDF secara efisien dan membantu aplikasi Anda berkinerja lebih baik. Aspose.PDF for .NET adalah pilihan pertama pelanggan kami saat membuat dokumen PDF karena harganya, kinerja yang luar biasa, dan dukungan yang hebat.

**Aspose.PDF for .NET** aman multithread selama hanya satu thread yang bekerja pada satu dokumen pada satu waktu. Ini adalah skenario umum untuk memiliki satu thread yang bekerja pada satu dokumen. Thread yang berbeda dapat bekerja dengan aman pada dokumen yang berbeda pada saat yang sama.

## Deklarasi

Semua komponen Aspose .NET memerlukan izin Full Trust. Alasannya adalah, komponen Aspose .NET perlu mengakses pengaturan registri, file sistem selain direktori virtual untuk operasi tertentu seperti parsing font dll. Selain itu, Komponen Aspose .NET didasarkan pada kelas sistem .NET inti yang juga memerlukan izin Full Trust dalam banyak kasus.

Penyedia Layanan Internet yang menghosting beberapa aplikasi dari perusahaan yang berbeda sebagian besar memberlakukan tingkat keamanan Medium Trust. Dalam kasus .NET 2.0, tingkat keamanan tersebut menerapkan batasan berikut:

- **OleDbPermission tidak tersedia.** Ini berarti Anda tidak dapat menggunakan penyedia data OLE DB yang dikelola ADO.NET untuk mengakses basis data.
- **EventLogPermission tidak tersedia.** Ini berarti Anda tidak dapat mengakses log peristiwa Windows.
- **ReflectionPermission tidak tersedia.** Ini berarti Anda tidak dapat menggunakan refleksi.
- **RegistryPermission tidak tersedia.** Ini berarti Anda tidak dapat mengakses registri.
- **WebPermission dibatasi.** Ini berarti aplikasi Anda hanya dapat berkomunikasi dengan alamat atau rentang alamat yang Anda definisikan dalam elemen `<trust>`.
- **FileIOPermission dibatasi.** Ini berarti Anda hanya dapat mengakses file dalam hierarki direktori virtual aplikasi Anda.
Karena alasan yang disebutkan di atas, komponen Aspose .NET tidak dapat digunakan di server yang memberikan izin set selain Full Trust.

## Instalasi

### Evaluasi Aspose.PDF for .NET

Anda dapat dengan mudah mengunduh Aspose.PDF for .NET untuk evaluasi. Unduhan evaluasi adalah sama dengan unduhan yang dibeli. Versi evaluasi hanya menjadi berlisensi ketika Anda menambahkan beberapa baris kode untuk menerapkan lisensi.

Versi evaluasi dari Aspose.PDF (tanpa lisensi yang ditentukan) menyediakan fungsionalitas produk penuh. Namun, ia memiliki dua batasan: ia menyisipkan watermark evaluasi, dan hanya empat halaman pertama dari dokumen apa pun yang dapat dilihat/diedit.

{{% alert color="primary" %}}

Jika Anda ingin menguji Aspose.PDF for .NET tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara 30 hari. Silakan lihat [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

### Menginstal Aspose.PDF for .NET melalui NuGet

NuGet adalah sistem manajemen paket sumber terbuka yang gratis dan berfokus pada pengembang untuk platform .NET yang bertujuan menyederhanakan proses menggabungkan pustaka pihak ketiga ke dalam aplikasi .NET selama pengembangan. Ini adalah ekstensi Visual Studio yang memudahkan untuk menambahkan, menghapus, dan memperbarui pustaka dan alat dalam proyek Visual Studio yang menggunakan .NET Framework. Sebuah pustaka atau alat dapat dengan mudah dibagikan dengan pengembang lain dengan membuat paket NuGet dan menyimpannya di dalam repositori NuGet. Ketika Anda menginstal paket, NuGet menyalin file ke solusi Anda dan secara otomatis membuat perubahan yang diperlukan, seperti menambahkan referensi dan mengubah file app.config atau web.config Anda. Jika Anda memutuskan untuk menghapus pustaka, NuGet menghapus file dan membalikkan perubahan apa pun yang dibuatnya pada proyek Anda sehingga tidak ada kekacauan yang tersisa.

### Mereferensikan Aspose.PDF for .NET

#### Instal paket menggunakan Package Manager Console

- Buka aplikasi .NET Anda di Visual Studio.
- Di menu Tools, pilih **NuGet Package Manager** dan kemudian **Package Manager Console**.
- Ketik perintah `Install-Package Aspose.PDF` untuk menginstal rilis penuh terbaru, atau ketik perintah `Install-Package Aspose.PDF -prerelease` untuk menginstal rilis terbaru termasuk hotfix.
- Tekan `Enter`.

#### Memperbarui paket menggunakan Package Manager Console

Jika Anda sudah mereferensikan komponen melalui NuGet, ikuti langkah-langkah ini untuk memperbarui referensi ke versi terbaru:

- Buka aplikasi .NET Anda di Visual Studio.
- Di menu Tools, pilih **NuGet Package Manager** dan kemudian **Package Manager Console**.
- Ketik perintah `Update-Package Aspose.PDF` untuk mereferensikan rilis penuh terbaru, atau ketik perintah `Update-Package Aspose.PDF -prerelease` untuk menginstal rilis terbaru termasuk hotfix.

#### Instal Paket menggunakan GUI Package Manager

Ikuti langkah-langkah ini untuk mereferensikan komponen menggunakan GUI package manager:

- Buka aplikasi .NET Anda di Visual Studio.

- Dari menu Project pilih **Manage NuGet Packages**.

![Installation_step](../images/install_step.png)

- Pilih tab **Broswe**.

![Installation_step1](../images/install_step1.png)

- Ketik Aspose.PDF ke dalam kotak pencarian untuk menemukan Aspose.PDF for .NET.

- Klik Instal/Perbarui di sebelah versi terbaru dari Aspose.PDF for .NET.

![Installation_step2](../images/Install_step2.png)

- Dan klik Terima di jendela pop-up.

![Installation_step3](../images/Install_step3.png)

![Installation](../images/install.gif)

### Bekerja dengan DLL .NET Core di Lingkungan Non-Windows

Karena Aspose.PDF for .NET menyediakan dukungan .NET Standard 2.0 (.NET Core 2.0), maka dapat digunakan dalam Aplikasi Core yang berjalan di sistem operasi seperti Linux. Kami terus bekerja untuk meningkatkan dukungan .NET Core dalam API kami. Namun, ada beberapa operasi berikut yang kami sarankan kepada pelanggan kami untuk dilakukan, guna mendapatkan hasil yang lebih baik saat menggunakan fitur Aspose.PDF for .NET:

Silakan instal:

- paket libgdiplus
- paket dengan font yang kompatibel dengan Microsoft: **ttf-mscorefonts-installer**. (misalnya `sudo apt-get install ttf-mscorefonts-installer`)
Font-font ini harus ditempatkan di direktori "/usr/share/fonts/truetype/msttcorefonts" karena Aspose.PDF for .NET memindai folder ini di sistem operasi seperti Linux. Jika sistem operasi memiliki folder/direktori default lain untuk font, Anda harus menggunakan baris kode berikut sebelum melakukan operasi apa pun menggunakan Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```

#### Siapkan Aspose.PDF for .NET di Visual Studio Code
- Instal .NET SDK

1. Kunjungi [situs resmi Microsoft .NET](https://dotnet.microsoft.com/download).
2. Unduh .NET SDK terbaru.
3. Jalankan penginstal.
4. Buka terminal dan verifikasi instalasi dengan menjalankan:
```bash
dotnet --version
```

- Instal Visual Studio Code

1. Pergi ke https://code.visualstudio.com/.
2. Unduh versi yang sesuai untuk sistem operasi Anda.

- Instal Ekstensi VS Code yang Diperlukan

1. Buka Visual Studio Code.
2. Klik pada ikon tampilan Ekstensi (ikon persegi di sidebar kiri).
3. Cari dan instal ekstensi berikut:
   - "C#" oleh Microsoft
   - "C# Dev Kit" oleh Microsoft
   - ".NET Core Test Explorer" (opsional, tetapi disarankan)

- Buat proyek .NET baru

1. Buka Visual Studio Code
2. Pergi ke Terminal > Terminal Baru
3. Navigasikan ke direktori proyek yang Anda inginkan
```bash
# Create a new console application
dotnet new console -n AsposePDFNetDemo
# Navigate into the project directory
cd AsposePDFNetDemo
```

- Tambahkan paket NuGet

```bash
# Install Aspose.PDF package
dotnet add package Aspose.PDF
```

- Verifikasi instalasi paket

1. Buka file `.csproj`
2. Konfirmasi referensi paket Aspose.PDF telah ditambahkan:
```xml
<ItemGroup>
  <PackageReference Include="Aspose.PDF" Version="x.x.x" />
</ItemGroup>
```

- Buat Konfigurasi Debug

1. Tekan Ctrl+Shift+P (Cmd+Shift+P di Mac).
2. Ketik ">.NET: Generate Assets for Build and Debug".
3. Pilih proyek Anda.
4. Buat atau modifikasi `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net7.0/AsposePDFNetDemo.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopAtEntry": false
        }
    ]
}
```

- Tulis kode contoh Program.cs

Ganti konten `Program.cs` dengan:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
using System;
using Aspose.Pdf;
using Aspose.Pdf.Text;

class Program 
{
    static void Main(string[] args)
    {
        // Activate your license, you can comment out these codelines to use library in Evaluation mode
        var license = new Aspose.Pdf.License();
        license.SetLicense("Aspose.PDF.NET.lic");

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            
            // Create a text fragment
            var textFragment = new Aspose.Pdf.Text.TextFragment("Hello, Aspose.PDF for .NET!");
            textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
            
            // Add text to the page
            page.Paragraphs.Add(textFragment);
            
            // Save PDF document
            document.Save("sample.pdf");
        }
    }
}
```

- Bangun dan jalankan

```bash
dotnet restore
dotnet build
dotnet run
```