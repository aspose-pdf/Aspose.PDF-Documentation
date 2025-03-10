---
title: Mengonversi FDF ke format XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/converting-an-fdf-to-xml-format/
description: Bagian ini menjelaskan bagaimana Anda dapat mengonversi FDF ke format XML dengan Kelas FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Temukan cara untuk mengonversi file FDF ke format XML dengan efisien menggunakan kelas FormDataConverter di Aspose.PDF for .NET. Fungsionalitas ini menyederhanakan penanganan data dengan mengubah pasangan kunci/nilai dari FDF menjadi struktur XML yang mudah dibaca, meningkatkan interoperabilitas dan manajemen data dalam aplikasi Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) di [Aspose.PDF for .NET](/pdf/net/) mendukung AcroForms dengan sangat baik. Ini juga mendukung impor dan ekspor data formulir ke berbagai format file seperti FDF, XFDF, dan XML. Namun, terkadang pengembang mungkin perlu mengonversi satu format ke format lainnya. Artikel ini melihat fitur yang mengonversi FDF menjadi XML.

{{% /alert %}}

## Detail implementasi

FDF adalah singkatan dari Forms Data Format, dan file FDF berisi nilai formulir dalam pasangan kunci/nilai. Kita juga tahu bahwa file XML berisi nilai sebagai tag. Di mana, biasanya kunci diwakili sebagai nama tag dan nilai diwakili sebagai nilai di dalam tag tersebut. Sekarang, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memberikan kita fleksibilitas untuk mengonversi format file FDF menjadi format XML.

Kita dapat menggunakan kelas [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) untuk tujuan ini. Kelas ini menyediakan kita berbagai metode untuk mengonversi satu format data ke format lainnya. Dalam artikel ini, kita hanya akan menggunakan satu metode bernama [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Metode ini mengambil file FDF sebagai input atau aliran sumber dan menyimpannya dalam format XML.

Potongan kode berikut menunjukkan kepada Anda bagaimana mengonversi file FDF menjadi file XML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```