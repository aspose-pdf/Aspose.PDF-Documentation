---
title: Поддержка DICOM-изображений
linktitle: Поддержка DICOM-изображений
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ru/net/support-for-dicom-mages/
description: В этом разделе описывается, как с помощью библиотеки C# обеспечить поддержку DICOM-изображений в PDF-файле.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Support for DICOM Images",
    "alternativeHeadline": "Add DICOM images to PDFs using C# library",
    "abstract": "Aspose.PDF для .NET теперь интегрирует поддержку изображений DICOM, позволяя легко встраивать медицинские изображения в документы PDF. Эта новая функция использует библиотеку C# для эффективной обработки изображений DICOM в процессе создания PDF-файлов. Функция упрощает рабочий процесс включения изображений DICOM в PDF-файлы.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "DICOM images, PDF, C#, Aspose.PDF, DICOM to PDF, add DICOM to PDF, .NET library, ImageFileType.Dicom",
    "wordcount": "194",
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
    "url": "/net/support-for-dicom-mages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/support-for-dicom-mages/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел описывает, как реализовать поддержку DICOM-изображений в PDF-файле с помощью библиотеки на C#."
}
</script>

Стандарт DICOM был разработан Национальной ассоциацией производителей электрооборудования. Этот формат охватывает функции создания, хранения, передачи и печати отдельных кадров изображений, серий кадров, информации о пациентах, исследований, оборудования, учреждений, медицинского персонала, проводящего обследование, и тому подобного.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

**Aspose.PDF for .NET** поддерживает функцию добавления DICOM-изображений в PDF-документы. Следующий фрагмент кода показывает, как использовать эту функцию.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDicomImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create an image instance and set its properties
        var image = new Aspose.Pdf.Image
        {
            FileType = Aspose.Pdf.ImageFileType.Dicom,
            ImageStream = new FileStream(dataDir + "DicomImage.dcm", FileMode.Open, FileAccess.Read)
        };

        // Add image to the first page
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "PdfWithDicomImage_out.pdf");
    }
}
```


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