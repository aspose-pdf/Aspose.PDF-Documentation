---
title: Menambahkan Gambar ke PDF menggunakan C#
linktitle: Tambah Gambar
type: docs
weight: 10
url: /id/net/add-image-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan perpustakaan C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Gambar ke PDF menggunakan C#",
    "alternativeHeadline": "Cara menambahkan Gambar ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, menambahkan gambar ke pdf",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan perpustakaan C#."
}
</script>
## Menambahkan Gambar dalam File PDF yang Sudah Ada

Setiap halaman PDF mengandung properti Sumber Daya dan Konten. Sumber Daya bisa berupa gambar dan formulir, misalnya, sementara konten diwakili oleh sekumpulan operator PDF. Setiap operator memiliki nama dan argumen. Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk menambahkan gambar ke file PDF yang sudah ada:

- Buat objek Dokumen dan buka dokumen PDF masukan.
- Dapatkan halaman yang ingin Anda tambahkan gambar.
- Tambahkan gambar ke koleksi Sumber Daya halaman.
- Gunakan operator untuk meletakkan gambar di halaman:
- Gunakan operator GSave untuk menyimpan keadaan grafis saat ini.
- Gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan ditempatkan.
- Gunakan operator Do untuk menggambar gambar di halaman.
- Akhirnya, gunakan operator GRestore untuk menyimpan keadaan grafis yang diperbarui.
- Simpan file.
Potongan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Setel koordinat
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Dapatkan halaman di mana gambar perlu ditambahkan
Page page = pdfDocument.Pages[1];
// Muat gambar ke dalam aliran
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Tambahkan gambar ke koleksi Gambar dari Sumber Daya Halaman
page.Resources.Images.Add(imageStream);
// Menggunakan operator GSave: operator ini menyimpan keadaan grafis saat ini
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Buat objek Rectangle dan Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Menggunakan ConcatenateMatrix (matriks concatenate) operator: menentukan bagaimana gambar harus ditempatkan
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Menggunakan operator Do: operator ini menggambar gambar
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Menggunakan operator GRestore: operator ini mengembalikan keadaan grafis
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Simpan dokumen yang diperbarui
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}
Secara default, kualitas JPEG diatur ke 100%. Untuk menerapkan kompresi dan kualitas yang lebih baik, gunakan overload berikut:
{{% /alert %}}

- overload metode Replace ditambahkan ke dalam kelas XImageCollection: public void Replace(int index, Stream stream, int quality)
- overload metode Add ditambahkan ke dalam kelas XImageCollection: public void Add(Stream stream, int quality)

## Menambahkan Gambar ke dalam File PDF yang Sudah Ada (Facades)

Ada juga cara alternatif, lebih mudah untuk menambahkan Gambar ke file PDF.
Ada juga cara alternatif yang lebih mudah untuk menambahkan gambar ke file PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## Tempatkan gambar di halaman dan jaga (kontrol) rasio aspek

Jika kita tidak mengetahui dimensi gambar, ada kemungkinan besar mendapatkan gambar yang terdistorsi di halaman. Contoh berikut menunjukkan salah satu cara untuk menghindarinya.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## Tentukan jika Gambar dalam PDF Berwarna atau Hitam Putih

Jenis kompresi yang berbeda dapat diterapkan pada gambar untuk mengurangi ukurannya. Jenis kompresi yang diterapkan pada gambar tergantung pada ColorSpace dari gambar sumber yaitu jika gambar berwarna (RGB), maka terapkan kompresi JPEG2000, dan jika Hitam & Putih, maka kompresi JBIG2/JBIG2000 harus diterapkan. Oleh karena itu, mengidentifikasi setiap jenis gambar dan menggunakan jenis kompresi yang sesuai akan menciptakan hasil yang terbaik/optimal.

File PDF dapat berisi elemen Teks, Gambar, Grafik, Lampiran, Anotasi, dll dan jika file PDF sumber mengandung gambar, kita dapat menentukan ruang warna gambar dan menerapkan kompresi yang sesuai untuk gambar untuk mengurangi ukuran file PDF. Cuplikan kode berikut menunjukkan langkah-langkah untuk Menentukan jika gambar dalam PDF Berwarna atau Hitam Putih.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Penghitung untuk gambar skala abu-abu
int grayscaled = 0;
// Penghitung untuk gambar RGB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Mendapatkan jumlah gambar di halaman tertentu
        Console.WriteLine("Total Gambar = {0} di nomor halaman {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Gambar {0} adalah Skala Abu-abu...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Gambar {0} adalah RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## Kontrol Kualitas Gambar

Anda dapat mengontrol kualitas gambar yang ditambahkan ke file PDF. Gunakan metode [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) yang berlebihan di kelas [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

Potongan kode berikut menunjukkan cara mengonversi semua gambar dokumen menjadi JPEG yang menggunakan kualitas kompresi 80%.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
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

