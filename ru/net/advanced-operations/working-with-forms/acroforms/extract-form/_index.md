---
title: Извлечение AcroForm — извлечение данных формы из PDF в C#
linktitle: Извлечение AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/extract-form/
description: Извлеките форму из вашего PDF-документа с помощью библиотеки Aspose.PDF for .NET. Получите значение из отдельного поля PDF-файла.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm - Extract Form Data from PDF in C#",
    "alternativeHeadline": "Effortlessly Extract PDF Form Data Using C#",
    "abstract": "Новая функция Extract AcroForm в Aspose.PDF для .NET позволяет разработчикам легко извлекать данные форм из PDF-документов. Эта функциональность позволяет пользователям получать значения из отдельных полей или всех полей в PDF, улучшая возможности управления данными и их обработки в приложениях на C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract form data, PDF in C#, Aspose.PDF for .NET, AcroForm extraction, get field values PDF, PDF form fields, individual field value, get fields in region, manipulate PDF forms, C# PDF library",
    "wordcount": "673",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Извлеките форму из вашего PDF-документа с помощью библиотеки Aspose.PDF для .NET. Получите значение из отдельного поля PDF-файла"
}
</script>

Следующий фрагмент кода также работает с библиотекой Aspose.PDF.Drawing.

## Извлечение данных из формы

### Получение значений из всех полей PDF-документа

Чтобы получить значения из всех полей в PDF-документе, вам нужно пройти по всем полям формы, а затем получить значение с помощью свойства Value. Получите каждое поле из коллекции Form в базовом типе поля Field и получите доступ к его свойству Value.

В следующих фрагментах кода на C# показано, как получить значения всех полей из PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValuesFromFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValuesFromAllFields.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

### Получить значение из отдельного поля PDF-документа

Свойство Value поля формы позволяет получить значение определённого поля. Чтобы получить значение, извлеките поле формы из коллекции Form объекта Document. В этом примере на C# выбирается TextBoxField и извлекается его значение с помощью свойства Value.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValueFromField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get a field
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            // Get field value
            Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
            Console.WriteLine("Value : {0} ", textBoxField.Value);
        }
    }
}
```

Чтобы получить URL-адрес кнопки отправки, используйте следующие строки кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSubmitFormActionUrl()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get the SubmitFormAction from the form field
        if (document.Form[1].OnActivated is Aspose.Pdf.Annotations.SubmitFormAction act)
        {
            // Output the URL of the SubmitFormAction
            Console.WriteLine(act.Url.Name);
        }
    }
}
```

### Получение полей формы из определённой области PDF-файла

Иногда вы можете знать, где в документе находится поле формы, но не знаете его имени. Например, если всё, что у вас есть, это схема печатной формы. С Aspose.PDF for .NET это не проблема. Вы можете узнать, какие поля находятся в заданном регионе PDF-файла. Чтобы получить поля формы из определённой области PDF-файла:

1. Откройте PDF-файл с помощью объекта Document.
1. Получите форму из коллекции Forms документа.
1. Укажите прямоугольную область и передайте её методу GetFieldsInRect объекта Form. Возвращается коллекция Fields.
1. Используйте её для управления полями.

В следующем фрагменте кода на C# показано, как получить поля формы в определённой прямоугольной области PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldsFromRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf"))
    {
        // Create rectangle object to get fields in that area
        var rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

        // Get the PDF form
        var form = document.Form;

        // Get fields in the rectangular area
        var fields = form.GetFieldsInRect(rectangle);

        // Display Field names and values
        foreach (var field in fields)
        {
            // Display image placement properties for all placements
            Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
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