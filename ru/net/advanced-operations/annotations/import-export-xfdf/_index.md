---
title: Импорт и экспорт аннотаций в XFDF
linktitle: Импорт и экспорт аннотаций в XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/import-export-xfdf/
description: Вы можете импортировать и экспортировать аннотации в формате XFDF с помощью C# и библиотеки Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Effortless XFDF Annotation Import and Export",
    "abstract": "Новая функциональность импорта и экспорта для XFDF в библиотеке Aspose.PDF для .NET упрощает управление PDF-документами, позволяя беспрепятственно передавать данные аннотаций. Эта функция позволяет пользователям легко интегрировать аннотации из файлов XFDF и экспортировать их обратно, способствуя эффективному обмену данными и возможностям архивирования для PDF-форм",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Annotations, Export Annotations, XFDF Format, Aspose.PDF for .NET, PdfAnnotationEditor, ImportAnnotationFromXfdf, ExportAnnotationsXfdf, PDF Forms Manipulation",
    "wordcount": "670",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Вы можете импортировать и экспортировать аннотации в формате XFDF с помощью C# и библиотеки Aspose.PDF для .NET."
}
</script>

{{% alert цвет="основной" %}}

XFDF означает формат данных XML-форм. Это файл формата на основе XML. Этот формат файла используется для представления данных формы или аннотаций, содержащихся в PDF-форме. XFDF может использоваться для самых разных целей, но в нашем случае его можно использовать либо для отправки или получения данных формы или аннотаций на другие компьютеры или серверы и т.д., либо его можно использовать для архивирования данных формы или аннотаций. В этой статье мы увидим, как Aspose.Pdf.Facades учёл эту концепцию и как мы можем импортировать и экспортировать данные аннотаций в файл XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** — это многофункциональный компонент, когда речь заходит о редактировании PDF-документов. Как мы знаем, XFDF является важным аспектом управления PDF-формами, пространство имён Aspose.Pdf.Facades в Aspose.PDF for .NET хорошо это продумало и предоставило методы для импорта и экспорта данных аннотаций в файлы XFDF.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfannotationeditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF. Метод [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) обеспечивает возможность экспорта аннотаций из PDF-документа в файл XFDF, а метод [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) позволяет импортировать аннотации из существующего файла XFDF. Чтобы импортировать или экспортировать аннотации, нам нужно указать типы аннотаций. Мы можем указать эти типы в виде перечисления, а затем передать это перечисление в качестве аргумента любому из этих методов. Таким образом, будут импортированы или экспортированы в файл XFDF только аннотации указанных типов.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как экспортировать аннотации в файл XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAnnotationsToXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationDemo1.pdf");

        // Define the annotation types to export
        var annotType = new Aspose.Pdf.Annotations.AnnotationType[] { Aspose.Pdf.Annotations.AnnotationType.Line, Aspose.Pdf.Annotations.AnnotationType.Square };

        // Export annotations to XFDF file
        using (var fileStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
        }
    }
}
```

Следующий фрагмент кода описывает, как импортировать аннотации из файла XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Define the export file name
            var exportFileName = dataDir + "exportannotations.xfdf";

            // Import annotations from the XFDF file
            annotationEditor.ImportAnnotationsFromXfdf(exportFileName);

            // Save PDF document
            document.Save(dataDir + "ImportAnnotationFromXfdf_out.pdf");
        }
    }
}
```

## Ещё один способ экспортировать/импортировать аннотации сразу

В приведённом ниже коде метод ImportAnnotations позволяет импортировать аннотации непосредственно из другого PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var documentFrom = new Aspose.Pdf.Document(dataDir + "some_doc.pdf"))
    {
        // Create PDF document
        using (var documentTo = new Aspose.Pdf.Document())
        {
            // Add page
            var page = documentTo.Pages.Add();

            // Export/import
            using (var ms = new MemoryStream())
            {
                documentFrom.ExportAnnotationsToXfdf(ms);
                documentTo.ImportAnnotationsFromXfdf(ms);
            }

            // Save PDF document
            documentTo.Save(dataDir + "AnnotationDemo3_out.pdf");
        }
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