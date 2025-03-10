---
title: استخراج الصور باستخدام PdfExtractor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/extract-images/
description: يشرح هذا القسم كيفية استخراج الصور باستخدام Aspose.PDF Facades من خلال استخدام فئة PdfExtractor.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "تتيح ميزة PdfExtractor من Aspose.PDF للمستخدمين استخراج الصور بكفاءة من مستندات PDF، مع تقديم خيارات متعددة مثل استخراج الصور من المستند بالكامل، أو صفحات معينة، أو نطاقات محددة. تدعم حفظ الصور مباشرة إلى الملفات أو تدفقات الذاكرة، مما يعزز المرونة للمطورين الذين يعملون مع أصول PDF. تتيح هذه الوظيفة القوية التحكم الدقيق في أوضاع استخراج الصور، مما يسهل التعامل مع أنواع محتوى PDF المختلفة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج الصور من PDF بالكامل إلى ملفات (Facades)

تتيح لك فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) استخراج الصور من ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، استدعِ طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور على القرص، يمكنك استدعاء النسخة الزائدة من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ مسار الملف كوسيط. يوضح لك مقتطف الكود التالي كيفية استخراج الصور من PDF بالكامل إلى ملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## استخراج الصور من PDF بالكامل إلى تدفقات (Facades)

تتيح لك فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) استخراج الصور من ملف PDF إلى تدفقات. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، استدعِ طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور في تدفق، يمكنك استدعاء النسخة الزائدة من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ Stream كوسيط. يوضح لك مقتطف الكود التالي كيفية استخراج الصور من PDF بالكامل إلى تدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## استخراج الصور من صفحة معينة من PDF (Facades)

يمكنك استخراج الصور من صفحة معينة من ملف PDF. من أجل القيام بذلك، تحتاج إلى تعيين خصائص [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) إلى الصفحة المعينة التي تريد استخراج الصور منها. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). ثانيًا، عليك تعيين خصائص [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). بعد ذلك، استدعِ طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. يمكنك إما حفظ الصور على القرص أو في تدفق. تحتاج فقط إلى استدعاء النسخة الزائدة المناسبة من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). يوضح لك مقتطف الكود التالي كيفية استخراج الصور من صفحة معينة من PDF إلى تدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## استخراج الصور من نطاق من صفحات PDF (Facades)

يمكنك استخراج الصور من نطاق من صفحات ملف PDF. من أجل القيام بذلك، تحتاج إلى تعيين خصائص [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) إلى نطاق الصفحات التي تريد استخراج الصور منها. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). ثانيًا، عليك تعيين خصائص [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). بعد ذلك، استدعِ طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. يمكنك إما حفظ الصور على القرص أو في تدفق. تحتاج فقط إلى استدعاء النسخة الزائدة المناسبة من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). يوضح لك مقتطف الكود التالي كيفية استخراج الصور من نطاق من صفحات PDF إلى تدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## استخراج الصور باستخدام وضع استخراج الصور (Facades)

تتيح لك فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) استخراج الصور من ملف PDF. تدعم Aspose.PDF وضعين للاستخراج؛ الأول هو ActuallyUsedImage الذي يستخرج الصور المستخدمة فعليًا في مستند PDF. الوضع الثاني هو [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) الذي يستخرج الصور المحددة في موارد مستند PDF (وضع الاستخراج الافتراضي). أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، حدد وضع استخراج الصورة باستخدام خاصية [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). ثم استدعِ طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة بناءً على الوضع الذي حددته. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور على القرص، يمكنك استدعاء النسخة الزائدة من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ مسار الملف كوسيط.

يوضح لك مقتطف الكود التالي كيفية استخراج الصور من ملف PDF باستخدام خيار ExtractImageMode.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

للتحقق مما إذا كان PDF يحتوي على نص أو صور، استخدم مقتطف الكود التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```