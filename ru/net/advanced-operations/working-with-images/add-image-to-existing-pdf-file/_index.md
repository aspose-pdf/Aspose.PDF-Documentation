---
title: Добавить изображение в PDF с использованием C#
linktitle: Добавить изображение
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-image-to-existing-pdf-file/
description: Этот раздел описывает, как добавить изображение в существующий PDF-файл с использованием библиотеки C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "Новая функциональность в библиотеке Aspose.PDF позволяет пользователям без труда добавлять изображения в существующие PDF-файлы с использованием C#. Эта функция упрощает манипуляции с PDF, позволяя точно позиционировать и масштабировать изображения непосредственно в документе, обеспечивая высококачественную интеграцию и контроль над визуальными элементами. С поддержкой различных форматов изображений и конфигураций этот инструмент повышает гибкость управления содержимым PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "1433",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Этот раздел описывает, как добавить изображение в существующий PDF-файл с использованием библиотеки C#."
}
</script>

## Добавить изображение в существующий PDF-файл

Каждая страница PDF содержит свойства ресурсов и содержимого. Ресурсы могут быть изображениями и формами, например, в то время как содержимое представлено набором операторов PDF. Каждый оператор имеет свое имя и аргумент. Этот пример использует операторы для добавления изображения в PDF-файл.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Чтобы добавить изображение в существующий PDF-файл:

- Создайте объект Document и откройте входной PDF-документ.
- Получите страницу, в которую вы хотите добавить изображение.
- Добавьте изображение в коллекцию ресурсов страницы.
- Используйте операторы для размещения изображения на странице:
- Используйте оператор GSave, чтобы сохранить текущее графическое состояние.
- Используйте оператор ConcatenateMatrix, чтобы указать, где должно быть размещено изображение.
- Используйте оператор Do, чтобы нарисовать изображение на странице.
- Наконец, используйте оператор GRestore, чтобы сохранить обновленное графическое состояние.
- Сохраните файл.
Следующий фрагмент кода показывает, как добавить изображение в PDF-документ.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

По умолчанию качество JPEG установлено на 100%. Чтобы применить лучшее сжатие и качество, используйте следующие перегрузки:

{{% /alert %}}

- перегрузка метода Replace добавлена в класс XImageCollection: public void Replace(int index, Stream stream, int quality)
- перегрузка метода Add добавлена в класс XImageCollection: public void Add(Stam stream, int quality)

## Добавить изображение в существующий PDF-файл (Facade)

Существует также альтернативный, более простой способ добавить изображение в PDF-файл. Вы можете использовать метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) класса [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). Метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) требует изображение, которое нужно добавить, номер страницы, на которую нужно добавить изображение, и информацию о координатах. После этого сохраните обновленный PDF-файл, используя метод Close. Следующий фрагмент кода показывает, как добавить изображение в существующий PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

Иногда необходимо обрезать изображение перед вставкой его в PDF. Вы можете использовать метод `AddImage()`, чтобы поддерживать добавление обрезанных изображений:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Разместить изображение на странице и сохранить (контролировать) соотношение сторон

Если мы не знаем размеры изображения, существует вероятность получения искаженного изображения на странице. Следующий пример показывает один из способов избежать этого.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

## Определить, является ли изображение внутри PDF цветным или черно-белым

Разные типы сжатия могут применяться к изображениям для уменьшения их размера. Тип сжатия, применяемого к изображению, зависит от ColorSpace исходного изображения, т.е. если изображение цветное (RGB), то применяйте сжатие JPEG2000, а если оно черно-белое, то должно применяться сжатие JBIG2/JBIG2000. Поэтому определение каждого типа изображения и использование соответствующего типа сжатия создаст лучший/оптимизированный результат.

PDF-файл может содержать текст, изображения, графики, вложения, аннотации и т.д., и если исходный PDF-файл содержит изображения, мы можем определить цветовое пространство изображения и применить соответствующее сжатие для уменьшения размера PDF-файла. Следующий фрагмент кода показывает шаги для определения, является ли изображение внутри PDF цветным или черно-белым.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## Контроль качества изображения

Можно контролировать качество изображения, которое добавляется в PDF-файл. Используйте перегруженный метод [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) в классе [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

Следующий фрагмент кода демонстрирует, как преобразовать все изображения документа в JPEG с использованием 80% качества для сжатия.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## Поддержка применения маски обрезки к изображениям

Размещение векторной формы поверх базового растрового изображения функционирует как маска, открывая только ту часть базового дизайна, которая совпадает с векторной формой. Все области вне формы будут скрыты.

Фрагмент кода загружает PDF, открывает два файла изображений и применяет эти изображения в качестве трафаретных масок к первым двум изображениям на первой странице PDF.

Маска трафарета может быть добавлена с помощью метода 'XImage.AddStencilMask(Stream maskStream)':

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
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