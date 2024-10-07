---
title: Cara mencetak file PDF di .NET Core
linktitle: Mencetak PDF di .NET Core
type: docs
weight: 40
url: /net/print-dotnetcore/
keywords: "print pdf .net core"
description: Halaman ini menjelaskan cara mengonversi dokumen PDF menjadi XPS di .NET Core dan menambahkannya sebagai pekerjaan ke antrian printer lokal.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cara mencetak file PDF di .NET Core",
    "alternativeHeadline": "Mencetak file PDF di .NET Core",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pdf di .NET Core",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2022-02-04",
    "description": "Halaman ini menjelaskan cara mengonversi dokumen PDF menjadi XPS dan menambahkannya sebagai pekerjaan ke antrian printer lokal."
}
</script>
Potongan kode berikut juga dapat digunakan dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **Mencetak Dokumen Pdf di .NET Core**

Pustaka Aspose.PDF memungkinkan kita untuk mengonversi file PDF ke XPS. Fungsi ini dapat berguna untuk mengatur pencetakan dokumen. Mari kita lihat contoh penggunaan printer default:

```csharp
class Program
{
    static void Main()
    {
        // Buat thread sekunder dan berikan metode pencetakan untuk
        // parameter delegasi ThreadStart dari konstruktor.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // Atur thread yang akan menggunakan PrintQueue.AddJob menjadi single threading.
        printingThread.SetApartmentState(ApartmentState.STA);

        // Mulai thread pencetakan. Metode yang diberikan ke konstruktor
        // Thread akan dieksekusi.
        printingThread.Start();
    }//end Main

    private static void PrintPDF(string pdfFileName)
    {
        // Buat server cetak dan antrian cetak.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // Cetak file Xps sambil memberikan validasi XPS dan notifikasi kemajuan.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0} tidak dapat ditambahkan ke antrian cetak.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\tIni bukan file XPS yang valid. Gunakan alat isXPS Conformance Tool untuk debug.");
            }
            Console.WriteLine("\tLanjutkan dengan file XPS berikutnya.\n");
        }
    }
}//end Program class
```
Pada contoh ini, kita mengonversi dokumen PDF ke XPS dan menambahkannya sebagai pekerjaan ke antrian printer lokal.

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
    "applicationCategory": "Pustaka Manipulasi PDF untuk .NET",
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

