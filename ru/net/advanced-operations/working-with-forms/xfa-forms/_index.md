---
title: Работа с формами XFA
linktitle: Формы XFA
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/xfa-forms/
description: API Aspose.PDF for .NET позволяет работать с полями XFA и XFA Acroform в PDF-документе. Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF для .NET теперь предлагает расширенные возможности для работы с формами XFA, позволяя разработчикам заполнять, преобразовывать и управлять полями Acroform XFA в PDF-документах. Эта функция упрощает управление динамическими формами, обеспечивая беспрепятственный доступ к значениям и свойствам полей, а также эффективное преобразование из XFA в стандартные AcroForms. Усовершенствуйте рабочий процесс обработки PDF-файлов с помощью этого надёжного решения для работы со сложными структурами форм.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF для .NET API позволяет работать с полями XFA и XFA Acroform в PDF-документе. Aspose.Pdf.Facades"
}
</script>

{{% alert color="primary" %}}

Динамические формы основаны на XML-спецификации, известной как XFA (Архитектура XML-форм). Она также может преобразовывать динамическую форму XFA в стандартный Acroform. Информация о форме (что касается PDF) очень расплывчата — она указывает на то, что поля существуют со свойствами и событиями JavaScript, но не определяет никакого рендеринга. Объекты формы XFA рисуются при загрузке документа.

{{% /alert %}}

Класс Form предоставляет возможность работать со статическими AcroForm, и вы можете получить конкретный экземпляр поля, используя метод Form class’ GetFieldFacade(..). Однако доступ к полям XFA невозможен через метод Form.GetFieldFacade(..). Вместо этого используйте [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) для получения/установки значений полей и управления шаблоном полей XFA (установка свойств полей).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Заполнение полей XFA

В следующем фрагменте кода показано, как заполнять поля в форме XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## Преобразование из XFA в Acroform

{{% alert color="primary" %}}

Попробуйте онлайн
Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Динамические формы основаны на XML-спецификации, известной как XFA (Архитектура XML-форм). Информация о форме (что касается PDF) очень расплывчата — она указывает на то, что поля существуют со свойствами и событиями JavaScript, но не определяет никакого рендеринга.

В настоящее время PDF поддерживает два различных метода интеграции данных и PDF-форм:

- AcroForms (также известные как формы Acrobat), представленные и включённые в спецификацию формата PDF 1.2.
- Формы Adobe XML Forms Architecture (XFA), представленные в спецификации формата PDF 1.5 в качестве дополнительной функции (спецификация XFA не включена в спецификацию PDF, на неё только ссылаются).

Мы не можем извлекать или управлять страницами форм XFA, поскольку содержимое формы генерируется во время выполнения (во время просмотра формы XFA) в приложении, пытающемся отобразить или отрисовать форму XFA. В Aspose.PDF есть функция, которая позволяет разработчикам преобразовывать формы XFA в стандартные формы AcroForms.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## Получение свойств поля XFA

Чтобы получить доступ к свойствам поля, сначала используйте Document.Form.XFA.Template для доступа к шаблону поля. Следующий фрагмент кода показывает шаги получения координат X и Y поля формы XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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