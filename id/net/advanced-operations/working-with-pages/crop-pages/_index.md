---
title: Memotong Halaman PDF secara Programatik C#
linktitle: Memotong Halaman
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/crop-pages/
description: Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur baru yang kuat yang memungkinkan pengembang untuk mengakses dan memanipulasi berbagai properti halaman dari PDF secara programatik, termasuk media box, bleed box, trim box, art box, dan crop box. Fungsionalitas ini menyederhanakan proses penyesuaian tata letak PDF, memastikan presisi dalam presentasi dokumen dan meningkatkan kualitas cetak sambil meminimalkan tepi putih. Dengan potongan kode yang mudah digunakan, pengguna dapat dengan mulus mengintegrasikan kemampuan ini ke dalam aplikasi mereka, meningkatkan manajemen dan manipulasi PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1133",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2025-04-11",
    "description": "Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF for .NET."
}
</script>

## Mendapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF memungkinkan Anda untuk mengakses properti ini.

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih saat dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang meluas di luar tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("trimmed"), tinta akan sampai ke tepi halaman. Bahkan jika halaman dipotong tidak tepat - sedikit terpotong dari tanda trim - tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten aktual halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke aplikasi lain.
- **Crop box**: Crop box adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat. Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Batas Halaman.
- **Page.Rect**: irisan (rectangle yang umumnya terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti ini.
Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan di bawah ini menunjukkan cara memotong halaman:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

Dalam contoh ini, kami menggunakan file contoh [di sini](crop_page.pdf). Awalnya halaman kami terlihat seperti yang ditunjukkan pada Gambar 1.

Setelah perubahan, halaman akan terlihat seperti Gambar 2.

### Memotong ruang putih di sekitar halaman

Misalnya, Anda dapat memotong ruang putih di sekitar halaman menggunakan pustaka grafis apa pun yang dapat memuat bitmap:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf"))
    {
        var device = new Aspose.Pdf.Devices.PngDevice(new Aspose.Pdf.Devices.Resolution(300));

        using (var imageStr = new MemoryStream())
        {
            // Convert page to PNG image
            device.Process(document.Pages[1], imageStr);
            using (var pageBitmap = new Bitmap(imageStr))
            {
                document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);
            }
        }
        // Save PDF document
        document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
    }
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {
        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf");
    var device = new Aspose.Pdf.Devices.PngDevice(new Aspose.Pdf.Devices.Resolution(300));

    using var imageStr = new MemoryStream();

    // Convert page to PNG image
    device.Process(document.Pages[1], imageStr);
    using var pageBitmap = new Bitmap(imageStr);
    document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);

    // Save PDF document
    document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {
        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}
{{< /tabs >}}

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