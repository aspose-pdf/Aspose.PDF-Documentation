---
title: PDF-стикеры с заметками на C#
linktitle: Стикер-заметки
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/sticky-annotations/
description: Узнайте, как создавать стикеры-заметки в PDF-файлах с помощью Aspose.PDF на .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF sticky Annotations using C#",
    "alternativeHeadline": "Add Sticky Watermark Annotations to PDF with C#",
    "abstract": "Представляем новую функцию C# PDF Sticky Annotations, которая позволяет пользователям создавать и настраивать водяные знаки непосредственно в PDF-документах. Эта функция поддерживает установку определённых позиций текста, контроль непрозрачности и эффективное повторное использование изображений, улучшая общее представление документа и оптимизируя размер файлов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF sticky annotations, C# sticky annotations, Watermark Annotation, Aspose.PDF.Drawing, PDF document generation, opacity property, XImageCollection, optimize PDF size",
    "wordcount": "453",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Эта тема посвящена липким аннотациям, в качестве примера мы показываем аннотацию-водяной знак в тексте"
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление водяного знака

Водяной знак должен использоваться для представления графики, которая должна печататься в фиксированном размере и положении на странице независимо от размеров печатной страницы.

Вы можете добавить текст водяного знака с помощью [WatermarkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/watermarkannotation) в определённое место на странице PDF. Непрозрачностью водяного знака также можно управлять с помощью свойства opacity.

Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы добавить WatermarkAnnotation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "source.pdf"))
    {
        // Load Page object to add Annotation
        var page = document.Pages[1];

        // Create Watermark Annotation
        var wa = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 400, 600));

        // Add annotation into Annotation collection of Page
        page.Annotations.Add(wa);

        // Create TextState for Font settings
        var ts = new Aspose.Pdf.Text.TextState();
        ts.ForegroundColor = Aspose.Pdf.Color.Blue;
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        ts.FontSize = 32;

        // Set opacity level of Annotation Text
        wa.Opacity = 0.5;

        // Add Text in Annotation
        wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

        // Save PDF document
        document.Save(dataDir + "AddWatermarkAnnotation_out.pdf");
    }
}
```

## Добавить ссылку на одно изображение несколько раз в PDF-документ

Иногда нам требуется использовать одно и то же изображение в PDF-документе несколько раз. Добавление нового экземпляра увеличивает результирующий PDF-документ. Мы добавили новый метод XImageCollection.Add(XImage) в версии Aspose.PDF for .NET 17.1.0. Этот метод позволяет добавить ссылку на тот же PDF-объект, что и исходное изображение, что оптимизирует размер PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarkAnnotationWithImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Define the rectangle for the image
    var imageRectangle = new Aspose.Pdf.Rectangle(0, 0, 30, 15);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Open the image stream
        using (var imageStream = File.Open(dataDir + "icon.png", FileMode.Open))
        {
            XImage image = null;

            // Iterate through each page in the document
            foreach (Page page in document.Pages)
            {
                // Create a Watermark Annotation
                var annotation = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, page.Rect);
                XForm form = annotation.Appearance["N"];
                form.BBox = page.Rect;

                string name;

                // Add the image to the form resources if it hasn't been added yet
                if (image == null)
                {
                    name = form.Resources.Images.Add(imageStream);
                    image = form.Resources.Images[name];
                }
                else
                {
                    name = form.Resources.Images.Add(image);
                }

                // Add operators to the form contents to place the image
                form.Contents.Add(new Aspose.Pdf.Operators.GSave());
                form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(new Aspose.Pdf.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
                form.Contents.Add(new Aspose.Pdf.Operators.Do(name));
                form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

                // Add the annotation to the page
                page.Annotations.Add(annotation, false);

                // Adjust the image rectangle size for the next iteration
                imageRectangle = new Aspose.Pdf.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddWatermarkAnnotationWithImage_out.pdf");
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