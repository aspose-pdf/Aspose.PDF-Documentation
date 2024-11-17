---
title: كيفية طباعة ملف PDF في .NET Core
linktitle: طباعة PDF في .NET Core
type: docs
weight: 40
url: /ar/net/print-dotnetcore/
description: تشرح هذه الصفحة كيفية تحويل مستند PDF إلى XPS في .NET Core وإضافته كمهمة إلى قائمة الطابعة المحلية.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية طباعة ملف PDF في .NET Core",
    "alternativeHeadline": "طباعة ملف PDF في .NET Core",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, pdf in .NET Core",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "تشرح هذه الصفحة كيفية تحويل مستند PDF إلى XPS وإضافته كمهمة إلى قائمة الطابعة المحلية."
}
</script>
يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## **طباعة مستند PDF في .NET Core**

تسمح لنا مكتبة Aspose.PDF بتحويل ملفات PDF إلى XPS. يمكن أن تكون هذه الوظيفة مفيدة لتنظيم طباعة المستندات. دعونا نلقي نظرة على مثال لاستخدام الطابعة الافتراضية:

```csharp
class Program
{
    static void Main()
    {
        // إنشاء الخيط الثانوي وتمرير طريقة الطباعة لمعامل ThreadStart المفوض للمنشئ.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // ضبط الخيط الذي سيستخدم PrintQueue.AddJob لخيط واحد.
        printingThread.SetApartmentState(ApartmentState.STA);

        // بدء الخيط الطباعي. ستنفذ الطريقة الممررة إلى منشئ الخيط.
        printingThread.Start();
    }//end Main

    private static void PrintPDF(string pdfFileName)
    {
        // إنشاء خادم الطباعة وطابور الطباعة.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // طباعة ملف Xps مع توفير التحقق من XPS وإشعارات التقدم.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0} لم يتم إضافته إلى قائمة الطباعة.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\tليس ملف XPS صالح. استخدم أداة التوافق isXPS لتصحيحه.");
            }
            Console.WriteLine("\tالاستمرار مع الملف XPS التالي.\n");
        }
    }
}//end Program class
```
في هذا المثال، نحول مستند PDF إلى XPS ونضيفه كمهمة إلى قائمة الطابعة المحلية.

