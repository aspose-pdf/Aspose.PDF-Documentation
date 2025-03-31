---
title: كيفية طباعة ملف PDF في .NET Core
linktitle: طباعة PDF في .NET Core
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/print-dotnetcore/
description: تشرح هذه الصفحة كيفية تحويل مستند PDF إلى XPS في .NET Core وإضافته كوظيفة إلى قائمة الانتظار للطابعة المحلية.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to print PDF file in .NET Core",
    "alternativeHeadline": "Print PDFs as XPS in .NET Core with ease",
    "abstract": "اكتشف الوظيفة الجديدة في .NET Core التي تبسط عملية طباعة مستندات PDF عن طريق تحويلها إلى تنسيق XPS وإدارة مهام الطباعة بكفاءة في قائمة الانتظار للطابعة المحلية. تتيح هذه الميزة أيضًا تحكمًا معززًا في مصادر الورق بناءً على أحجام صفحات PDF، مما يضمن تجربة طباعة مخصصة. قم بتحسين إدارة مستنداتك مع خيارات قياس دقيقة مباشرة من مربع حوار الطباعة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print PDF, .NET Core, convert PDF to XPS, print queue, Aspose.PDF, paper source by PDF page size, print dialog presets, page scaling, document printing, local printer",
    "wordcount": "606",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2024-11-25",
    "description": "تشرح هذه الصفحة كيفية تحويل مستند PDF إلى XPS وإضافته كوظيفة إلى قائمة الانتظار للطابعة المحلية."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## **طباعة مستند PDF في .NET Core**

تتيح لنا مكتبة Aspose.PDF تحويل ملفات PDF إلى XPS. يمكن أن تكون هذه الوظيفة مفيدة لتنظيم طباعة المستندات. دعونا نلقي نظرة على مثال لاستخدام الطابعة الافتراضية.

في هذا المثال، نقوم بتحويل مستند PDF إلى XPS وإضافته كوظيفة إلى قائمة الانتظار للطابعة المحلية:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Convert PDF to XPS
    using (var document = new Aspose.Pdf.Document(pdfFileName))
    {
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName, SaveFormat.Xps);

        // Print the Xps file while providing XPS validation and progress notifications.
        using (PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false))
        {
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFileName);

    // Convert PDF to XPS
    var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
    document.Save(xpsFileName,SaveFormat.Xps);

    // Print the Xps file while providing XPS validation and progress notifications.
    using PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
    Console.WriteLine(xpsPrintJob.JobIdentifier);
}
```
{{< /tab >}}
{{< /tabs >}}

## اختيار مصدر الورق حسب حجم صفحة PDF

منذ إصدار 24.4، أصبح من الممكن اختيار مصدر الورق حسب حجم صفحة PDF في مربع حوار الطباعة. يمكّن مقتطف الشيفرة التالي من اختيار درج الطابعة بناءً على حجم صفحة PDF.

يمكن تشغيل هذه الميزة وإيقافها باستخدام خاصية [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/picktraybypdfsize/) .

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose a paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;

    // Save PDF document
    document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إعدادات مربع حوار الطباعة قياس الصفحة

يهدف مقتطف الشيفرة التالي إلى ضمان تطبيق خاصية [PrintScaling](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/printscaling/) بشكل صحيح وحفظها في PDF.

تمت إضافة خاصية [PrintScaling](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/printscaling/) إلى فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) مع القيم `Aspose.Pdf.PrintScaling.AppDefault` أو `Aspose.Pdf.PrintScaling.None` .

خيار قياس الصفحة الذي يجب اختياره عند عرض مربع حوار الطباعة لهذا المستند. القيم الصالحة هي `None`، مما يشير إلى عدم وجود قياس للصفحة، و `AppDefault`، مما يشير إلى قياس الطباعة الافتراضي للقارئ المتوافق. إذا كانت هذه الإدخال تحتوي على قيمة غير معروفة، يجب استخدام `AppDefault`. القيمة الافتراضية: `AppDefault` .

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    document.Pages.Add();

    // Disable print scaling
    document.PrintScaling = PrintScaling.None;

    // Save PDF document
    document.Save(dataDir + "SetPrintScaling_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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