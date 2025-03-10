---
title: استخراج الصور من PDF والتعرف على الرموز الشريطية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "اكتشف كيفية استخراج الصور بكفاءة من مستندات PDF والتعرف بدقة على الرموز الشريطية المدمجة باستخدام Aspose.PDF for .NET. تسهل هذه الوظيفة الجديدة عملية تحديد معلومات الرموز الشريطية من خلال معالجة الصور المستخرجة من كل صفحة من صفحات PDF، مما يعزز استرجاع البيانات وإدارتها. استكشف الخطوات التفصيلية وتنفيذ الكود لتحسين سير عمل معالجة المستندات الخاصة بك.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

عادةً ما تتكون مستندات PDF من نصوص وصور وجداول ومرفقات ورسوم بيانية وتعليقات وأشياء ذات صلة أخرى. هناك حالات يتم فيها تضمين الرموز الشريطية داخل ملف PDF وبعض العملاء لديهم متطلبات لتحديد الرموز الشريطية الموجودة داخل ملف PDF. تشرح المقالة التالية الخطوات اللازمة لاستخراج الصور من صفحات PDF وتحديد الرموز الشريطية داخلها.

{{% /alert %}}

وفقًا لنموذج كائن المستندات من Aspose.PDF for .NET، يحتوي ملف PDF على صفحة واحدة أو أكثر حيث تحتوي كل صفحة على مجموعة من الصور والنماذج والخطوط في كائن الموارد. لذلك، لاستخراج الصور من ملف PDF، سنقوم بالتنقل عبر الصفحات الفردية لملف PDF، والحصول على مجموعة الصور من صفحة معينة وحفظها في كائن MemoryStream لمزيد من المعالجة باستخدام فئة BarCodeReader من Aspose.BarCodeRecognition.

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

لمزيد من التفاصيل حول الموضوعات التي تم تناولها في هذه المقالة، قم بزيارة الروابط التالية:

- [استخراج الصور من ملف PDF](/net/extract-images-from-the-pdf-file/)
- [قراءة الرموز الشريطية](https://docs.aspose.com/barcode/net/barcode-recognition/)