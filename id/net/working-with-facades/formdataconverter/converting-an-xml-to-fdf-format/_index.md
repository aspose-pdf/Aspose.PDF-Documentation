---
title: Mengonversi XML ke format FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/converting-an-xml-to-fdf-format/
description: Bagian ini menjelaskan bagaimana Anda dapat mengonversi XML ke format FDF dengan FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "Fitur ini memungkinkan pengembang untuk mengonversi file XML ke format FDF dengan lancar menggunakan kelas FormDataConverter di Aspose.PDF for .NET. Fungsionalitas ini meningkatkan pertukaran data antara format dokumen, memfasilitasi pengelolaan data formulir yang efisien dalam aplikasi",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) di [Aspose.PDF for .NET](/pdf/id/net/) mendukung AcroForms dengan sangat baik. Ini juga mendukung impor dan ekspor data formulir ke berbagai format file seperti FDF, XFDF, dan XML. Namun, terkadang seorang pengembang perlu mengonversi satu format ke format lainnya. Dalam artikel ini, kita akan melihat fitur yang memungkinkan kita untuk mengonversi format FDF menjadi XML.

{{% /alert %}}

## Detail implementasi

FDF adalah singkatan dari Forms Data Format, dan file FDF berisi nilai formulir dalam pasangan kunci/nilai. Kita juga tahu bahwa file XML berisi nilai sebagai tag. Di mana, sebagian besar kunci diwakili sebagai nama tag dan nilai diwakili sebagai nilai di dalam tag tersebut. Sekarang, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memberikan fleksibilitas untuk mengonversi format file XML menjadi format FDF.

Gunakan kelas [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) untuk tujuan ini. Kelas ini menyediakan berbagai metode untuk mengonversi satu format data menjadi format lainnya. Artikel ini menunjukkan cara menggunakan salah satu metode, ConvertXmlToFdf(..), yang mengambil file FDF sebagai input atau aliran sumber dan menyimpannya dalam format XML. Potongan kode berikut menunjukkan cara mengonversi file FDF menjadi file XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```