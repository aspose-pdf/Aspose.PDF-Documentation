---
title: Импорт и экспорт полей формы
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/import-export-form-field/
description: Заполнение полей формы с использованием DataTable с помощью класса FormEditor от Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "Функция импорта и экспорта полей формы в Aspose.PDF for .NET позволяет пользователям без проблем заполнять и изменять поля PDF-форм, используя различные источники данных, такие как FDF, XFDF, XML и даже объекты System.Data.DataTable. Этот мощный API позволяет автоматизировать обработку данных, повышая эффективность управления PDF-формами и упрощая процесс ввода данных.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
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
    "url": "/net/import-export-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-form-field/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Aspose.PDF for .NET предоставляет отличные возможности для создания/изменения полей формы внутри PDF-документа. С помощью этого API вы можете программно заполнять поля формы внутри PDF-файла, заполнять поля формы, импортируя данные из [FDF в PDF-файл](/pdf/ru/net/import-and-export-data/), [XFDF в PDF-файл](/pdf/ru/net/import-and-export-data/), [XML в PDF-файл](/pdf/ru/net/import-and-export-data/) или даже вы можете импортировать данные из объекта [System.Data.DataTable](https://reference.aspose.com/pdf/ru/net/aspose.pdf.table/importdatatable/methods/1).

## Импорт данных из PDF в FDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Import data fdf
        using (var xfdfInputStream  = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(xfdfInputStream);
        }
                
        // Import data XML
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            form.ImportXml(xfdfInputStream);
        }
                
        // Import data XFDF
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xfdf", FileMode.Open))
        {
            form.ImportXfdf(xfdfInputStream);
        }
                
        // Save PDF document
        form.Save(dataDir + "ImportDataUpdated_out.pdf");
    }
}
```

## Экспорт данных из FDF в PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");
                
        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "data_out.fdf", FileMode.Create))
        {
            form.ExportXfdf(fdfOutputStream);
        }
                
        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "data_out.xml", FileMode.Create))
        {
            form.ExportXfdf(xmlOutputStream);
        }
            
        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "data_out.xfdf", FileMode.Create))
        {
            form.ExportXfdf(xfdfOutputStream);
        }              
    }
} 
```