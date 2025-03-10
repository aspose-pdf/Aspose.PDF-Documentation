---
title: Temukan apakah PDF berisi gambar atau teks
linktitle: Periksa keberadaan teks dan gambar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/find-whether-pdf-file-contains-images-or-text-only/
description: Topik ini menjelaskan cara menemukan apakah file PDF hanya berisi gambar atau teks dengan Kelas PdfExtractor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Find whether PDF contains images or text",
    "alternativeHeadline": "Determine PDF Content: Text, Images, or Both",
    "abstract": "Temukan fungsionalitas yang memungkinkan pengguna untuk secara efisien menentukan apakah file PDF berisi teks, gambar, atau keduanya, menggunakan Kelas PdfExtractor. Fitur ini menyederhanakan proses analisis konten PDF, memberikan output yang jelas tentang keberadaan teks dan gambar dalam file. Dengan hanya beberapa baris kode, pengguna dapat secara efektif mengklasifikasikan dokumen PDF mereka berdasarkan jenis konten",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "265",
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
    "url": "/net/find-whether-pdf-file-contains-images-or-text-only/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/find-whether-pdf-file-contains-images-or-text-only/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Latar Belakang

File PDF dapat berisi teks dan gambar. Terkadang, pengguna mungkin perlu mengetahui apakah file PDF hanya berisi teks, atau hanya berisi gambar. Kita juga dapat menemukan apakah itu berisi keduanya atau tidak ada.

{{% alert color="primary" %}}

Potongan kode berikut menunjukkan kepada Anda bagaimana memenuhi persyaratan ini.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Instantiate a memoryStream object to hold the extracted text from Document
    using (var ms = new MemoryStream())
    {
        // Create the PdfExtractor
        using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
        {
            // Bind PDF document
            extractor.BindPdf(dataDir + "FilledForm.pdf");
            // Extract text from the input PDF document
            extractor.ExtractText();
            // Save the extracted text to a text file
            extractor.GetText(ms);
            // Check if the MemoryStream length is greater than or equal to 1

            bool containsText = ms.Length >= 1;

            // Extract images from the input PDF document
            extractor.ExtractImage();

            // Calling HasNextImage method in while loop. When images will finish, loop will exit
            bool containsImage = extractor.HasNextImage();

            // Now find out whether this PDF is text only or image only

            if (containsText && !containsImage)
            {
                Console.WriteLine("PDF contains text only");
            }
            else if (!containsText && containsImage)
            {
                Console.WriteLine("PDF contains image only");
            }
            else if (containsText && containsImage)
            {
                Console.WriteLine("PDF contains both text and image");
            }
            else if (!containsText && !containsImage)
            {
                Console.WriteLine("PDF contains neither text or nor image");
            }
        }
    }
}
```