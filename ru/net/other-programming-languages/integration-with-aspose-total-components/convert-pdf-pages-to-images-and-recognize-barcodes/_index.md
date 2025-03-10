---
title: Преобразование страниц PDF в изображения и распознавание штрих-кодов
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "Новая функция позволяет легко преобразовывать страницы PDF в различные форматы изображений, что упрощает распознавание встроенных штрих-кодов с помощью Aspose.Barcode для .NET. Эта функциональность упрощает обработку документов, позволяя пользователям преобразовывать содержимое PDF в изображения и точно считывать штрих-коды для эффективной работы с данными",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Ознакомьтесь с следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Документы PDF обычно содержат текст, изображения, таблицы, вложения, графики, аннотации и другие объекты. Некоторым нашим клиентам необходимо встраивать в документы штрихкоды, а затем идентифицировать штрихкоды в файле PDF. В следующей статье объясняется, как преобразовать страницы файла PDF в изображения и идентифицировать штрихкоды на изображениях с помощью Aspose.Barcode для .NET.

{{% /alert %}}

## Преобразование страниц в изображения и распознавание штрихкодов

{{% alert color="primary" %}}

Aspose.PDF for .NET — очень мощный продукт для управления PDF-документами. Он позволяет легко конвертировать страницы в PDF-документах в изображения. Aspose.BarCode для .NET — не менее мощный продукт для создания и распознавания штрихкодов.

Класс PdfConverter в пространстве имён Aspose.Pdf.Facades поддерживает преобразование PDF-страниц в различные форматы изображений. PngDevice в пространстве имён Aspose.Pdf.Devices поддерживает преобразование PDF-страниц в файлы PNG. Любой из этих классов можно использовать для преобразования страниц PDF-файла в изображения.

Когда страницы преобразованы в формат изображения, мы можем использовать Aspose.BarCode для .NET для идентификации штрихкодов внутри них. Приведённые ниже примеры кода показывают, как конвертировать страницы с помощью PdfConverter или PngDevice.

{{% /alert %}}

### Использование Aspose.Pdf.Facades

{{% alert color="primary" %}}

Класс PdfConverter содержит метод с именем GetNextImage, который генерирует изображение из текущей страницы PDF. Чтобы указать выходной формат изображения, этот метод принимает аргумент из перечисления System.Drawing.Imaging.ImageFormat.

Aspose.Barcode содержит пространство имён BarCodeRecognition, которое содержит класс BarCodeReader. Класс BarCodeReader позволяет считывать, определять и идентифицировать штрихкоды из файлов изображений.

Для этого примера сначала преобразуйте страницу в файле PDF в изображение с помощью Aspose.Pdf.Facades.PdfConverter. Затем используйте класс Aspose.BarCodeRecognition.BarCodeReader для распознавания штрихкода на изображении.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

В приведённых выше фрагментах кода выходное изображение сохраняется в объекте MemoryStream. Изображение также можно сохранить на диск. Для этого замените объект MemorStream строкой, представляющей путь к файлу, в методе GetNextImage класса PdfConverter.

{{% /alert %}}

#### Использование класса PngDevice

В Aspose.Pdf.Devices есть класс PngDevice. Этот класс позволяет конвертировать страницы PDF-документов в PNG-изображения.

Для этого примера загрузите исходный PDF-файл в документ Document, преобразуйте страницы документа в PNG-изображения. Когда изображения будут созданы, используйте класс BarCodeReader в Aspose.BarCodeRecognition для идентификации и считывания штрихкодов на изображениях.

{{% alert color="primary" %}}

Приведённые здесь примеры кода перебирают страницы PDF-документа и пытаются идентифицировать штрихкоды на каждой странице.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

Дополнительную информацию по темам, затронутым в этой статье, см. в разделах:

- Преобразование PDF-страниц в разные форматы изображений (Facades).
- Конвертация всех PDF-страниц в PNG-изображения.
- [Считывание штрихкодов](https://docs.aspose.com/barcode/net/barcode-recognition/).

{{% /alert %}}