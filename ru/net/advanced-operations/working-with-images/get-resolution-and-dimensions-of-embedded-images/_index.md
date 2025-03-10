---
title: Получение разрешения и размеров изображений
linktitle: Получить разрешение и размеры
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/get-resolution-and-dimensions-of-embedded-images/
description: Узнайте, как получить разрешение и размеры встроенных изображений из PDF-файла в .NET с помощью Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "Extract Image Resolution and Dimensions Efficiently",
    "abstract": "Узнайте, как эффективно получить разрешение и размеры встроенных изображений в PDF-документах с помощью библиотеки Aspose.PDF. Эта функция позволяет разработчикам напрямую обращаться к свойствам изображений без извлечения, оптимизируя процесс работы с изображениями в PDF-файлах и улучшая функциональность и контроль над данными изображений",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Get Resolution, Dimensions of Images, Embedded Images, Aspose.PDF.Drawing, ArrayList, Image Placement Classes, ConcatenateMatrix, XImage, PDF Manipulation Library, Image Resolution Computation",
    "wordcount": "827",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел показывает подробности получения разрешения и размеров встроенных изображений"
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

В этой теме объясняется, как использовать классы операторов в пространстве имён Aspose.PDF, которые предоставляют возможность получать информацию о разрешении и размерах изображений без необходимости их извлечения.

Существуют разные способы достижения этой цели. В этой статье объясняется, как использовать `ArrayList` и [классы размещения изображений](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Сначала загрузите исходный PDF-файл (с изображениями).
1. Затем создайте объект `ArrayList`, чтобы сохранить имена всех изображений в документе.
1. Получите изображения с помощью свойства Page.Resources.Images.
1. Создайте объект стека для хранения графического состояния изображения и используйте его для отслеживания различных состояний изображения.
1. Создайте объект ConcatenateMatrix, который определяет текущее преобразование. Он также поддерживает масштабирование, поворот и перекос любого содержимого. Он объединяет новую матрицу с предыдущей. Обратите внимание, что мы не можем определить преобразование с нуля, а только изменить существующее преобразование.
1. Поскольку мы можем изменять матрицу с помощью ConcatenateMatrix, нам также может потребоваться вернуться к исходному состоянию изображения. Используйте операторы GSave и GRestore. Эти операторы используются попарно, поэтому их следует вызывать вместе. Например, если вы выполняете графическую работу со сложными преобразованиями и, наконец, возвращаете преобразования в исходное состояние, подход будет примерно таким:

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

В результате текст рисуется в обычном виде, но между текстовыми операторами выполняются некоторые преобразования. Чтобы отобразить изображение или нарисовать объекты формы и изображения, нам нужно использовать оператор Do.

У нас также есть класс с именем XImage, который предоставляет два свойства, Width и Height, которые можно использовать для получения размеров изображения.

1. Выполните некоторые вычисления для определения разрешения изображения.
1. Отобразите информацию в командной строке вместе с именем изображения.

Приведённый ниже фрагмент кода показывает, как получить размеры и разрешение изображения без извлечения изображения из PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageInformationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInformation.pdf"))
    {
        // Define the default resolution for image
        int defaultResolution = 72;
        var graphicsState = new Stack();

        // Define list which will hold image names
        var imageNames = new List<string>(document.Pages[1].Resources.Images.Names);

        // Insert an object to stack
        graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        foreach (var op in document.Pages[1].Contents)
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            var opSaveState = op as Aspose.Pdf.Operators.GSave;
            var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
            var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
            var opDo = op as Aspose.Pdf.Operators.Do;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.Pop();
            }
            else if (opCtm != null)
            {
                var cm = new System.Drawing.Drawing2D.Matrix(
                   (float)opCtm.Matrix.A,
                   (float)opCtm.Matrix.B,
                   (float)opCtm.Matrix.C,
                   (float)opCtm.Matrix.D,
                   (float)opCtm.Matrix.E,
                   (float)opCtm.Matrix.F);

                // Multiply current matrix with the state matrix
                ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.Contains(opDo.Name))
                {
                    var lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    // Create XImage object to hold images of first pdf page
                    var image = document.Pages[1].Resources.Images[opDo.Name];

                    // Get image dimensions
                    double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
                    double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.Width;
                    double originalHeight = image.Height;

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    Console.Out.WriteLine(
                            string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                         opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                         resVertical));
                }
            }
        }
    }
}
```

<!-- 7188229067 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "Издатель": {
        "@type": "Организация",
        "Название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternativeName": "Aspose",
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
    "предложения": {
        "@type": "Предложение",
        "цена": "1199",
        "валюта цены": "USD"
    },
    "категория приложения": "Библиотека управления PDF для .NET",
    "URL загрузки": "https://www
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