---
title: Bekerja dengan lapisan PDF menggunakan C#
linktitle: Bekerja dengan lapisan PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/work-with-pdf-layers/
description: Tugas berikut menjelaskan cara mengunci lapisan PDF, mengekstrak elemen lapisan PDF, meratakan PDF bertingkat, dan menggabungkan semua lapisan di dalam PDF menjadi satu.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "Rasakan peningkatan manajemen dokumen PDF dengan fitur baru Aspose.PDF for .NET yang memungkinkan pengguna untuk bekerja secara efektif dengan lapisan PDF. Fungsionalitas ini memungkinkan penguncian dan pembukaan kunci lapisan, mengekstrak elemen ke dalam file terpisah, meratakan konten bertingkat, dan menggabungkan beberapa lapisan menjadi satu, memberikan kontrol yang lebih besar atas visibilitas dan organisasi dokumen. Buka potensi dokumen PDF Anda dan permudah alur kerja Anda dengan alat yang kuat ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Lapisan PDF memungkinkan dokumen PDF untuk berisi set konten yang berbeda yang dapat dilihat atau disembunyikan secara selektif. Setiap lapisan dalam PDF dapat mencakup teks, gambar, atau grafik, dan pengguna dapat menghidupkan atau mematikan lapisan ini, tergantung pada kebutuhan mereka. Lapisan sering digunakan dalam dokumen kompleks di mana konten yang berbeda perlu diorganisir atau dipisahkan.

## Kunci lapisan PDF

Dengan Aspose.PDF for .NET Anda dapat membuka PDF, mengunci lapisan tertentu di halaman pertama, dan menyimpan dokumen dengan perubahan tersebut.

Sejak rilis 24.5, fitur ini telah diterapkan.

Ada dua metode baru dan satu properti yang ditambahkan:

- Layer.Lock(); - Mengunci lapisan.
- Layer.Unlock(); - Membuka kunci lapisan.
- Layer.Locked; - Properti, menunjukkan status terkunci lapisan.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## Ekstrak elemen lapisan PDF

Perpustakaan Aspose.PDF for .NET memungkinkan ekstraksi setiap lapisan dari halaman pertama dan menyimpan setiap lapisan ke dalam file terpisah.

Untuk membuat PDF baru dari sebuah lapisan, potongan kode berikut dapat digunakan:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

Rilis 24.9 telah menghasilkan pembaruan untuk fitur ini.

Dimungkinkan untuk mengekstrak elemen lapisan PDF dan menyimpannya ke dalam aliran file PDF baru:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## Ratakan PDF bertingkat

Perpustakaan Aspose.PDF for .NET membuka PDF, mengiterasi melalui setiap lapisan di halaman pertama, dan meratakan setiap lapisan, menjadikannya permanen di halaman.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

Metode 'Layer.Flatten(bool cleanupContentStream)' menerima parameter boolean yang menentukan apakah akan menghapus penanda grup konten opsional dari aliran konten. Mengatur parameter cleanupContentStream ke false mempercepat proses perataan.

## Gabungkan Semua Lapisan di dalam PDF menjadi satu

Perpustakaan Aspose.PDF for .NET memungkinkan penggabungan semua lapisan PDF atau lapisan tertentu di halaman pertama menjadi lapisan baru dan menyimpan dokumen yang diperbarui.

Dua metode ditambahkan untuk menggabungkan semua lapisan di halaman:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

Parameter kedua memungkinkan penggantian nama penanda grup konten opsional. Nilai default adalah "oc1" (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```