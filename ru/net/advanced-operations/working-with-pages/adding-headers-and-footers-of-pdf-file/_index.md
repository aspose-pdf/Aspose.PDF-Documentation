---
title: Добавить заголовок и нижний колонтитул в PDF
linktitle: Добавить заголовок и нижний колонтитул в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET позволяет добавлять заголовки и нижние колонтитулы в ваш PDF-файл с помощью класса TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET представляет собой мощную функцию, которая позволяет пользователям обогащать свои PDF-документы, добавляя настраиваемые заголовки и нижние колонтитулы. Используя классы TextStamp и ImageStamp, разработчики могут легко интегрировать как текст, так и изображения, настраивая их размещение и внешний вид в соответствии с различными форматами и стилями документов. Это повышает профессионализм и читаемость документа, что делает его идеальным для отчетов, счетов и других официальных коммуникаций.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET позволяет добавлять заголовки и нижние колонтитулы в ваш PDF-файл с помощью класса TextStamp."
}
</script>

**Aspose.PDF for .NET** позволяет вам добавлять заголовок и нижний колонтитул в ваш существующий PDF-файл. Вы можете добавлять изображения или текст в PDF-документ. Также попробуйте добавить разные заголовки в один PDF-файл с помощью C#.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление текста в заголовок PDF-файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/textstamp) для добавления текста в заголовок PDF-файла. Класс TextStamp предоставляет свойства, необходимые для создания текстового штампа, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить текст в заголовок, вам нужно создать объект Document и объект TextStamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить текст в заголовок PDF.

Вам нужно установить свойство TopMargin таким образом, чтобы оно регулировало текст в области заголовка вашего PDF. Вам также нужно установить HorizontalAlignment в Center и VerticalAlignment в Top.

Следующий фрагмент кода показывает, как добавить текст в заголовок PDF-файла с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## Добавление текста в нижний колонтитул PDF-файла

Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул PDF-файла. Класс TextStamp предоставляет свойства, необходимые для создания текстового штампа, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить текст в нижний колонтитул, вам нужно создать объект Document и объект TextStamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить текст в нижний колонтитул PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство Bottom Margin таким образом, чтобы оно регулировало текст в области нижнего колонтитула вашего PDF. Вам также нужно установить HorizontalAlignment в Center и VerticalAlignment в Bottom.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF-файла с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## Добавление изображения в заголовок PDF-файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/ImageStamp) для добавления изображения в заголовок PDF-файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page/methods/addstamp) страницы, чтобы добавить изображение в заголовок PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство TopMargin таким образом, чтобы оно регулировало изображение в области заголовка вашего PDF. Вам также нужно установить HorizontalAlignment в Center и VerticalAlignment в Top.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF-файла с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## Добавление изображения в нижний колонтитул PDF-файла

Вы можете использовать класс Image Stamp для добавления изображения в нижний колонтитул PDF-файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить изображение в нижний колонтитул, вам нужно создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в нижний колонтитул PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство [BottomMargin](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp/properties/bottommargin) таким образом, чтобы оно регулировало изображение в области нижнего колонтитула вашего PDF. Вам также нужно установить [HorizontalAlignment](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp/properties/horizontalalignment) в `Center` и [VerticalAlignment](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp/properties/verticalalignment) в `Bottom`.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## Добавление разных заголовков в один PDF-файл

Мы знаем, что можем добавлять TextStamp в раздел заголовка/нижнего колонтитула документа, используя свойства TopMargin или Bottom Margin, но иногда у нас может возникнуть необходимость добавить несколько заголовков/нижних колонтитулов в один PDF-документ. **Aspose.PDF for .NET** объясняет, как это сделать.

Чтобы выполнить это требование, мы создадим отдельные объекты TextStamp (количество объектов зависит от количества необходимых заголовков/нижних колонтитулов) и добавим их в PDF-документ. Мы также можем указать различную информацию о форматировании для каждого отдельного объекта штампа. В следующем примере мы создали объект Document и три объекта TextStamp, а затем использовали метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page/methods/addstamp) страницы, чтобы добавить текст в раздел заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с помощью Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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