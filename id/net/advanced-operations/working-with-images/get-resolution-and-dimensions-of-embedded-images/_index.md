---
title: Dapatkan Resolusi dan Dimensi Gambar
linktitle: Dapatkan Resolusi dan Dimensi
type: docs
weight: 40
url: id/net/get-resolution-and-dimensions-of-embedded-images/
description: Bagian ini menunjukkan detail dalam mendapatkan resolusi dan dimensi Gambar Tersemat
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dapatkan Resolusi dan Dimensi Gambar",
    "alternativeHeadline": "Cara mendapatkan Resolusi dan Dimensi Gambar Tersemat",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, dapatkan resolusi, dapatkan dimensi",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menunjukkan detail dalam mendapatkan resolusi dan dimensi Gambar Tersemat"
}
</script>

Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

Topik ini menjelaskan cara menggunakan kelas operator dalam ruang nama Aspose.PDF yang memberikan kemampuan untuk mendapatkan informasi resolusi dan dimensi tentang gambar tanpa harus mengekstraknya.

Ada beberapa cara untuk mencapai ini. Artikel ini menjelaskan cara menggunakan `arraylist` dan [kelas penempatan gambar](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Pertama, muat file PDF sumber (dengan gambar).
1. Kemudian buat objek ArrayList untuk menampung nama-nama gambar dalam dokumen.
1. Dapatkan gambar menggunakan properti Page.Resources.Images.
1. Buat objek tumpukan untuk menampung keadaan grafis gambar dan gunakan untuk melacak berbagai keadaan gambar.
1.
1. Karena kita dapat memodifikasi matriks dengan ConcatenateMatrix, kita mungkin juga perlu kembali ke keadaan gambar asli. Gunakan operator GSave dan GRestore. Operator ini dipasangkan sehingga harus dipanggil bersamaan. Sebagai contoh, jika Anda melakukan pekerjaan grafis dengan transformasi yang kompleks dan akhirnya mengembalikan transformasi kembali ke keadaan awal, pendekatannya akan seperti ini:

```csharp
// Menggambar beberapa teks
GSave

ConcatenateMatrix  // memutar isi setelah operator

// Beberapa pekerjaan grafis

ConcatenateMatrix // mengubah skala (dengan rotasi sebelumnya) isi setelah operator

// Beberapa pekerjaan grafis lainnya

GRestore

// Menggambar beberapa teks
```

Sebagai hasilnya, teks digambar dalam bentuk reguler tetapi beberapa transformasi dilakukan di antara operator teks. Untuk menampilkan gambar atau untuk menggambar objek bentuk dan gambar, kita perlu menggunakan operator Do.

Kami juga memiliki kelas bernama XImage yang menyediakan dua properti, Width dan Height, yang dapat digunakan untuk mendapatkan dimensi gambar.


1. Tampilkan informasi di Command Prompt bersama dengan nama gambar.

Kode berikut menunjukkan cara mendapatkan dimensi dan resolusi gambar tanpa mengeluarkan gambar dari dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Muat file PDF sumber
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Tentukan resolusi default untuk gambar
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Tentukan objek daftar array yang akan menyimpan nama gambar
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Masukkan objek ke tumpukan
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Dapatkan semua operator di halaman pertama dokumen
foreach (Operator op in doc.Pages[1].Contents)
{
    // Gunakan operator GSave/GRestore untuk mengembalikan transformasi ke set sebelumnya
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Instansiasi objek ConcatenateMatrix karena mendefinisikan matriks transformasi saat ini.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Buat operator Do yang menggambar objek dari sumber daya. Ini menggambar objek Form dan objek Gambar
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Simpan keadaan sebelumnya dan dorong keadaan saat ini ke atas tumpukan
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Buang keadaan saat ini dan kembalikan keadaan sebelumnya
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Kalikan matriks saat ini dengan matriks keadaan
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // Dalam kasus ini adalah operator penggambaran gambar
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Buat objek XImage untuk menampung gambar dari halaman pdf pertama
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Dapatkan dimensi gambar
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Dapatkan informasi Tinggi dan Lebar gambar
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Hitung resolusi berdasarkan informasi di atas
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Tampilkan informasi Dimensi dan Resolusi dari setiap gambar
            Console.Out.WriteLine(
                    string.Format(dataDir + "gambar {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
                "availableLanguage": "id"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "id"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "id"
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

