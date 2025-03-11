---
title: Извлечение изображений из PDF и распознавание штрих-кодов
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "Узнайте, как эффективно извлекать изображения из PDF документов и точно распознавать встроенные штрих-коды с помощью Aspose.PDF for .NET. Эта новая функция упрощает процесс идентификации информации о штрих-кодах, обрабатывая изображения, извлеченные с каждой страницы PDF, улучшая извлечение и управление данными. Изучите подробные шаги и реализацию кода, чтобы оптимизировать ваши рабочие процессы обработки документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/extract-images-from-pdf-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

PDF документы обычно состоят из текста, изображений, таблиц, вложений, графиков, аннотаций и других связанных объектов. Бывают случаи, когда штрих-коды встроены в PDF файл, и некоторые клиенты требуют идентифицировать штрих-коды, присутствующие в PDF файле. В следующей статье объясняются шаги по извлечению изображений из страниц PDF и идентификации штрих-кодов внутри них.

{{% /alert %}}

Согласно модели объектов документа Aspose.PDF for .NET, PDF файл содержит одну или несколько страниц, где каждая страница содержит коллекцию изображений, форм и шрифтов в объекте ресурсов. Таким образом, чтобы извлечь изображения из PDF файла, мы будем проходить через отдельные страницы PDF файла, получать коллекцию изображений с конкретной страницы и сохранять их в объекте MemoryStream для дальнейшей обработки с помощью класса BarCodeReader из Aspose.BarCodeRecognition.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through individual pages of PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Traverse through each image extracted from PDF pages
            foreach (var xImage in document.Pages[pageCount].Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save PDF document image
                    xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        
                    // Set the stream position to the begining of Stream
                    imageStream.Position = 0;
        
                    // Instantiate BarCodeReader object
                    var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
        
                    while (barcodeReader.Read())
                    {
                        // Get BarCode text from BarCode image
                        var code = barcodeReader.GetCodeText();
        
                        // Write the BarCode text to Console output
                        Console.WriteLine("BARCODE : " + code);
                    }
        
                    // Close BarCodeReader object to release the Image file
                    barcodeReader.Close();
                }
            }
        }
    }
}
```

Для получения дополнительной информации по темам, рассмотренным в этой статье, посетите следующие ссылки:

- [Извлечение изображений из PDF файла](/net/extract-images-from-the-pdf-file/)
- [Чтение штрих-кодов](https://docs.aspose.com/barcode/net/barcode-recognition/)