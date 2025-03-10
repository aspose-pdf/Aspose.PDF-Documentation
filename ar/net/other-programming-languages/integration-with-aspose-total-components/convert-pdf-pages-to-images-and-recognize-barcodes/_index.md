---
title: تحويل صفحات PDF إلى صور والتعرف على الرموز الشريطية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "تتيح الميزة الجديدة تحويل صفحات PDF بسلاسة إلى تنسيقات صور متنوعة، مما يسهل التعرف على الرموز الشريطية المدمجة باستخدام Aspose.Barcode لـ .NET. تعمل هذه الوظيفة على تبسيط معالجة المستندات من خلال السماح للمستخدمين بتحويل محتوى PDF إلى صور والتعرف بدقة على الرموز الشريطية من أجل إدارة البيانات بشكل فعال.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تتكون مستندات PDF عادةً من نصوص وصور وجداول ومرفقات ورسوم بيانية وتعليقات وأشياء أخرى. يحتاج بعض عملائنا إلى تضمين الرموز الشريطية في المستندات ثم التعرف على الرموز الشريطية في ملف PDF. تشرح المقالة التالية كيفية تحويل الصفحات في ملف PDF إلى صور والتعرف على الرموز الشريطية في الصور باستخدام Aspose.Barcode لـ .NET.

{{% /alert %}}

## تحويل الصفحات إلى صور والتعرف على الرموز الشريطية

{{% alert color="primary" %}}

Aspose.PDF for .NET هو منتج قوي جدًا لإدارة مستندات PDF. يسهل تحويل الصفحات في مستندات PDF إلى صور. Aspose.BarCode لـ .NET هو منتج قوي بنفس القدر لتوليد والتعرف على الرموز الشريطية.

تدعم الفئة PdfConverter تحت مساحة أسماء Aspose.Pdf.Facades تحويل صفحات PDF إلى تنسيقات صور متنوعة. تدعم PngDevice تحت مساحة أسماء Aspose.Pdf.Devices تحويل صفحات PDF إلى ملفات PNG. يمكن استخدام أي من هاتين الفئتين لتحويل صفحات ملف PDF إلى صور.

عندما يتم تحويل الصفحات إلى تنسيق صورة، يمكننا استخدام Aspose.BarCode لـ .NET للتعرف على الرموز الشريطية داخلها. تعرض عينات الكود أدناه كيفية تحويل الصفحات باستخدام إما PdfConverter أو PngDevice.

{{% /alert %}}

### استخدام Aspose.Pdf.Facades

{{% alert color="primary" %}}

تحتوي فئة PdfConverter على طريقة تسمى GetNextImage التي تولد صورة من الصفحة الحالية في PDF. لتحديد تنسيق الصورة الناتجة، تقبل هذه الطريقة وسيطًا من تعداد System.Drawing.Imaging.ImageFormat.

تحتوي Aspose.Barcode على مساحة أسماء، BarCodeRecognition، التي تحتوي على فئة BarCodeReader. تتيح لك فئة BarCodeReader قراءة وتحديد والتعرف على الرموز الشريطية من ملفات الصور.

لأغراض هذا المثال، قم أولاً بتحويل صفحة في ملف PDF إلى صورة باستخدام Aspose.Pdf.Facades.PdfConverter. ثم استخدم فئة Aspose.BarCodeRecognition.BarCodeReader للتعرف على الرمز الشريطي في الصورة.

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

في مقتطفات الكود أعلاه، يتم حفظ الصورة الناتجة في كائن MemoryStream. يمكن أيضًا حفظ الصورة على القرص. للقيام بذلك، استبدل كائن MemoryStream بكائن سلسلة يمثل مسار الملف إلى طريقة GetNextImage لفئة PdfConverter.

{{% /alert %}}

#### استخدام فئة PngDevice

في Aspose.Pdf.Devices، توجد PngDevice. تتيح لك هذه الفئة تحويل الصفحات في مستندات PDF إلى صور PNG.

لأغراض هذا المثال، قم بتحميل ملف PDF المصدر إلى صفحات المستند وتحويلها إلى صور PNG. عندما يتم إنشاء الصور، استخدم فئة BarCodeReader تحت Aspose.BarCodeRecognition للتعرف على وقراءة الرموز الشريطية في الصور.

{{% alert color="primary" %}}

تتجول عينات الكود المقدمة هنا عبر صفحات مستند PDF وتحاول التعرف على الرموز الشريطية في كل صفحة.

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

لمزيد من المعلومات حول الموضوعات التي تم تناولها في هذه المقالة، انتقل إلى:

- تحويل صفحات PDF إلى تنسيقات صور مختلفة (Facades)
- تحويل جميع صفحات PDF إلى صور PNG
- [قراءة الرموز الشريطية](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}