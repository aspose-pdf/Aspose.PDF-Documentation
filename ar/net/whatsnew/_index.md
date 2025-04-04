---
title: ما الجديد
linktitle: ما الجديد
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/whatsnew/
description: في هذه الصفحة يتم تقديم أكثر الميزات الجديدة شعبية في Aspose.PDF for .NET التي تم تقديمها في الإصدارات الأخيرة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-01-31"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats new",
    "alternativeHeadline": "Discover the latest enhancements in Aspose.PDF for .NET",
    "abstract": "اكتشف أحدث التحسينات في Aspose.PDF for .NET، بما في ذلك تقديم خوارزمية توقيع الرقمية باستخدام منحنيات إهليلجية (ECDSA) لتوقيع الوثائق والتحقق منها بشكل قوي، بالإضافة إلى دعم عدة منحنيات إهليلجية. بالإضافة إلى ذلك، تتيح الميزة الجديدة قص الصور عند إدراجها في ملفات PDF وتوليد تقارير الأعطال لتحسين معالجة الأخطاء. تعمل هذه التحديثات على تبسيط إدارة PDF وتعزيز الأمان في سير العمل الوثائقي.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "8022",
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
    "url": "/net/whatsnew/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whatsnew/"
    },
    "dateModified": "2024-12-04",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## ما الجديد في Aspose.PDF 25.2

**أهم التغييرات**

في Aspose.PDF 25.2 أضفنا:
* دعم تحويل [PDF إلى PDF/X-4](https://docs.aspose.com/pdf/net/convert-pdf-to-pdfx/) القياسي.
* [خيار](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-a-pdf-with-hash-signing-function) لتجنب استدعاء مفوض CustomSignHash مرتين أثناء التوقيع.
* طريقة جديدة `GetSignatureNames()` للحصول على معلومات حول [التوقيعات الرقمية](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-pdf-with-digital-signatures) لملف PDF.
* إمكانية إنشاء [TextBoxField](https://docs.aspose.com/pdf/net/create-form/#adding-radiobuttonfield) مع عدة تعليقات توضيحية للعنصر.
> [!NOTE]
> يمكن العثور على معلومات مفصلة حول التغييرات وعينات الاستخدام في صفحة [ملاحظات إصدار Aspose.PDF 25.2](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-2-release-notes/) .

**تحسينات ملحوظة أخرى**

* تحسين ضغط الصور دون فقدان الجودة عند [تحسين PDF](https://docs.aspose.com/pdf/net/optimize-pdf/#shrinking-or-compressing-all-images). تم تقليل حجم الوثيقة المضغوطة.
* تحسين طريقة [إصلاح](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/repair/) الوثيقة. يمكنها الآن التحقق وإصلاح القيم في مصفوفة Annotation.Rect.
* تحديث إصدار الاعتماد على System.Text.Json لتجنب الثغرات المحتملة CVE-2024-43485.
* تحسين اكتشاف هجمات توقيع PDF لمنع الحصول على نتائج إيجابية كاذبة.
* تم توفير واجهة برمجة تطبيقات عامة لتعديل قاموس الموارد:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingNewExtGState()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Graphics state parameter dictionary new name
    var gsName = "GS0";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var page = doc.Pages[1];
        var dictionaryEditor = new DictionaryEditor(page.Resources);
        var states = dictionaryEditor["ExtGState"].ToCosPdfDictionary();

        var newGs = CosPdfDictionary.CreateEmptyDictionary(doc);
        var pairs = new KeyValuePair<string, ICosPdfPrimitive>[3]
        {
            new KeyValuePair<string, ICosPdfPrimitive>("CA", new CosPdfNumber(1)),
            new KeyValuePair<string, ICosPdfPrimitive>("ca", new CosPdfNumber(0.5)),
            new KeyValuePair<string, ICosPdfPrimitive>("BM", new CosPdfName("Normal"))
        };

        foreach (var p in pairs)
        {
            newGs.Add(p);
        }
        states.Add(gsName, newGs);

        // Save PDF document
        doc.Save(outputPath);
    }
}
```

## ما الجديد في Aspose.PDF 25.1

في Aspose.PDF 25.1 أضفنا:
* خيار لحفظ PDF إلى HTML مع تخطي جميع الصور النقطية.
* إمكانية التحقق من توقيع PDF باستخدام خادم سلطة الشهادة (CA).
* التحقق من توقيع PDF عبر الأنظمة الأساسية باستخدام خوارزميات تجزئة SHA-3.

يمكن العثور على معلومات مفصلة حول التغييرات وعينات الاستخدام في صفحة [ملاحظات إصدار Aspose.PDF 25.1](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-1-release-notes/) .

## ما الجديد في Aspose.PDF 24.12

كانت القدرة على تمرير المسار إلى ملف تعريف ICC الخارجي لتحويل PDF/X و PDF/A موجودة بالفعل في المكتبة لعدة سنوات، وتم تفعيلها بواسطة خاصية PdfFormatConversionOptions.IccProfileFileName. الآن من الممكن أيضًا تمرير بيانات لملء خصائص OutputIntent باستخدام كائن من فئة OutputIntent.

تظهر الشيفرة التالية كيفية تحويل مستند التعليق إلى PDF/X-1 باستخدام ملف تعريف ICC FOGRA39:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfx1UsingCustomIccProfile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create conversion options to convert the document to PDF/X-1a with the given ICC profile
        var options = new PdfFormatConversionOptions(PdfFormat.PDF_X_1A, ConvertErrorAction.Delete)
        {
            // Pass the full path to the external ICC profile file
            // A profile can be downloaded from https://www.color.org/registry/Coated_Fogra39L_VIGC_300.xalter
            IccProfileFileName = "Coated_Fogra39L_VIGC_300.icc",

            // Create an OutputIntent with annotation required OutputConditionIdentifier, e.g. FOGRA39
            // If necessary, an OutputCondition and annotation RegistryName may be provided as well
            OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39")
        };

        // During the conversion process, the validation is also performed
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "outputPdfx.pdf");
    }
}
```

تمت إضافة محلل للعثور على الخط الأكثر ملاءمة لتوليد المستندات، والتحويل، واستبدال النص. يتم البحث عن الخط الأكثر ملاءمة في حالة عدم احتواء PDF المصدر على معلومات كافية عن الخط لإكمال العملية المطلوبة. يتم تحديد "الخط الأكثر ملاءمة" بين الخطوط المثبتة في البيئة بناءً على المعلومات حول خط PDF وأيضًا لغة النص المطلوبة ومجموعة الأحرف.

تظهر العينة التالية كيفية استخدام ذلك في تحويل PDF إلى PNG لتجنب تحول النص إلى مربعات فارغة.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToPngWithAnalyzingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.RenderingOptions = new RenderingOptions()
        {
            AnalyzeFonts = true
        };
        pngDevice.Process(document.Pages[1], dataDir + "converted.png");
    }
}
```

بدءًا من Aspose.PDF 24.12، يمكن تطبيق ضبط تلقائي لحجم الخط عند إضافة ختم نصي إلى ملف PDF التعليقي.

توضح الشيفرة التالية كيفية إضافة ختم نصي إلى ملف PDF التعليقي وضبط حجم الخط تلقائيًا ليتناسب مع مستطيل الختم.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```

توضح الشيفرة التالية كيفية إضافة ختم نصي إلى ملف PDF التعليقي وضبط حجم الخط تلقائيًا ليتناسب مع حجم الصفحة.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.11

تمت إضافة طريقة توسيع `PageCollection` لتحديث رقم الصفحة وتاريخ رأس/تذييل الوثيقة عند إضافة أو إدراج صفحات جديدة. يجب تخزين إعدادات رقم الصفحة وتنسيق التاريخ في الوثيقة الأصلية وفقًا لمواصفات PDF، كما هو مطبق بواسطة Adobe Acrobat.

توضح الشيفرة التالية كيفية تحديث الترقيم في الوثيقة:
```csharp
private static void UpdatePagination()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document that contains at least one page with pagination artifacts
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithPaginationArtifacts.pdf"))
    {
        // Update pages
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();

        // Update pagination artifacts
        document.Pages.UpdatePagination();

        // Save PDF document
        document.Save(dataDir + "DocumentWithUpdatedPagination.pdf");
    }
}
```

منذ الإصدار 24.11، أضفنا القدرة على اختيار خوارزمية تجزئة لـ Pkcs7Detached. الافتراضي هو SHA-256. بالنسبة للتوقيعات الرقمية ECDSA، تعتمد خوارزمية التجزئة الافتراضية على طول المفتاح.

يدعم ECDSA SHA-1 وSHA-256 وSHA-384 وSHA-512 وSHA3-256 وSHA3-384 وSHA3-512. تدعم خوارزميات SHA3-256 وSHA3-384 وSHA3-512 فقط لـ .NET 8 والإصدارات الأحدث. لمزيد من التفاصيل حول الأنظمة الأساسية المدعومة لـ SHA-3، يرجى الرجوع إلى [التوثيق](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3).

يدعم RSA SHA-1 وSHA-256 وSHA-384 وSHA-512.

يدعم DSA فقط SHA-1. يرجى ملاحظة أن SHA-1 قديم ولا يتوافق مع معايير الأمان الحالية.

توضح الشيفرة التالية كيفية تعيين خوارزمية التجزئة لـ Pkcs7Detached:
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass, Aspose.Pdf.DigestHashAlgorithm.Sha512);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

تمت إضافة خاصية جديدة `FontEncodingStrategy` إلى فئة `HtmlSaveOptions`. توصي مواصفات PDF باستخدام جدول `ToUnicode` لاستخراج محتوى النص من ملفات PDF. ومع ذلك، يمكن أن يؤدي استخدام جدول CMap الخاص بالخط إلى إنتاج نتائج أفضل لبعض أنواع الوثائق. بدءًا من الإصدار 24.11، يمكنك اختيار الجدول الذي سيتم استخدامه لفك التشفير. بشكل افتراضي، يتم استخدام جدول `ToUnicode`.

توضح العينة التالية الخيار الجديد باستخدام:
```csharp
private static void ConvertPdfToHtmlUsingCMap()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // New option there
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        // Save HTML document
        document.Save(dataDir + "CmapFontHTML_out.html", options);
    }
}
```

## ما الجديد في Aspose.PDF 24.10

تعد خوارزمية توقيع الرقمية باستخدام منحنيات إهليلجية (ECDSA) خوارزمية تشفير حديثة معروفة بتوفير أمان قوي مع أحجام مفاتيح أصغر مقارنة بالخوارزميات التقليدية. منذ الإصدار 24.10، أصبح من الممكن توقيع مستندات PDF باستخدام ECDSA، بالإضافة إلى التحقق من توقيعات ECDSA. المنحنيات الإهليلجية التالية مدعومة لإنشاء والتحقق من التوقيعات الرقمية:
* P-256 (secp256r1).
* P-384 (secp384r1).
* P-521 (secp521r1).
* brainpoolP256r1.
* brainpoolP384r1.
* brainpoolP512r1.

تستخدم خوارزمية تجزئة SHA-256 لتوليد التوقيع. يمكن التحقق من توقيعات ECDSA باستخدام خوارزميات التجزئة التالية: SHA-256 وSHA-384 وSHA-512 وSHA3-256 وSHA3-384 وSHA3-512.

يمكنك استخدام الشيفرة المعتادة لتوقيع المستندات باستخدام ECDSA والتحقق من التوقيعات:
 
```cs
private static void Sign(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}

private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign_out.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Get annotation list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

في بعض الأحيان، من الضروري قص صورة قبل إدراجها في PDF. لقد أضفنا إصدارًا مفرطًا من طريقة `AddImage()` لدعم إضافة الصور المقصوصة:

```cs
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (Stream imgStream = File.OpenRead(Path.Combine(dataDir, "Images", "Sample-01.jpg")))
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

        // Save PDF document
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.9

منذ الإصدار 24.9، أصبح من الممكن توليد تقرير عن الأعطال عندما تلقي المكتبة استثناء. يتضمن تقرير الأعطال معلومات حول نوع الاستثناء، عنوان التطبيق، إصدار Aspose.PDF، إصدار نظام التشغيل، رسالة الخطأ، وأثر المكدس.

توضح الشيفرة التالية سيناريو شائع لتوليد تقرير عن الأعطال:

```cs
private static void GenerateCrashReportExample()
{
    try
    {
        // some code
        // ....

        // Simulate an exception with an inner exception
        throw new Exception("message", new Exception("inner message"));
    }
    catch (Exception ex)
    {
        // Generate annotation crash report using PdfException
        Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
    }
}
```

استخراج عناصر طبقة مستند PDF وحفظها في تدفق PDF جديد متاح الآن. في مستندات PDF، تُستخدم الطبقات (المعروفة أيضًا بمجموعات المحتوى الاختيارية أو OCGs) لأغراض مختلفة، بشكل أساسي لإدارة والتحكم في رؤية المحتوى داخل الوثيقة. هذه الوظيفة مفيدة بشكل خاص في التصميم والهندسة والنشر. على سبيل المثال: جوانب المخطط، مكونات الرسم البياني المعقدة، إصدارات اللغة من نفس المحتوى.

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

تمت إضافة فئة `GraphicalPdfComparer` للمقارنة الرسومية لمستندات وصفحات PDF. تتعامل المقارنة الرسومية مع صور صفحات الوثيقة. تعيد النتيجة ككائن `ImagesDifference` أو كوثيقة PDF تحتوي على صور مدمجة من الأصل والاختلافات. تعتبر المقارنة الرسومية الأكثر فائدة للمستندات التي تحتوي على اختلافات طفيفة في النص أو المحتوى الرسومي.

توضح الشيفرة التالية المقارنة الرسومية بين مستندين PDF وتخزين صورة بالاختلافات في مستند PDF الناتج:

```cs
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare and save result
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```

تم تنفيذ واجهة برمجة التطبيقات لدمج FileFormat.HEIC وAspose.PDF. HEIC (ترميز الصورة عالي الكفاءة) هو تنسيق ملف صورة حديث قدمته Apple مع iOS 11 في عام 2017 كتنسيق الصورة الافتراضي لأجهزة iPhone وiPad.

لتحويل صور HEIC إلى PDF، يجب على المستخدم إضافة المرجع إلى حزمة NuGet `FileFormat.HEIC` واستخدام الشيفرة التالية:

```cs
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```

## ما الجديد في Aspose.PDF 24.8

تحويل مستندات PDF إلى تنسيق PDF/A-4

منذ الإصدار 24.8، أصبح من الممكن تحويل مستندات PDF إلى PDF/A-4. تم نشر الجزء 4 من المعيار، المستند إلى PDF 2.0، في أواخر عام 2020.

توضح الشيفرة التالية كيفية تحويل مستند إلى تنسيق PDF/A-4 عندما يكون مستند الإدخال إصدار PDF أقدم من 2.0.

```cs
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```

منذ 24.8 قدمنا طريقة لتسوية المحتوى الشفاف في مستندات PDF:

```cs
private static void FlattenTransparency()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTransparentImage.pdf"))
    {
        // Flatten image transparency
        document.FlattenTransparency();
        // Save PDF document
        document.Save(dataDir + "PdfWithFlattenedImage.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.7

مقارنة مستندات PDF مع Aspose.PDF for .NET

منذ 24.7، أصبح من الممكن مقارنة محتوى مستندات PDF مع علامات التعليق وإخراج جنبًا إلى جنب:

توضح الشيفرة الأولى كيفية مقارنة الصفحات الأولى من مستندين PDF.

```cs
private static void ComparingSpecificPagesSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1],
                dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

توسع الشيفرة الثانية النطاق لمقارنة المحتوى الكامل لمستندين PDF.

```cs
private static void ComparingEntireDocumentsSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

أيضًا، من هذا الإصدار تمت إضافة Aspose.PDF Security لـ .NET plugin:

ميزة التشفير:

```cs
var input = "sample.pdf";
var output = "encrypted.pdf";

var plugin = new Security();
var opt = new EncryptionOptions("123456789", "123", DocumentPrivilege.ForbidAll);
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

ميزة فك التشفير:

```cs
var input = "encrypted.pdf";
var output = "decrypted.pdf";

var plugin = new Security();
var opt = new DecryptionOptions("123456789");
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

## ما الجديد في Aspose.PDF 24.6

منذ إصدار 24.6، كجزء من تحرير PDF المعنونة، تمت إضافة طرق على **Aspose.Pdf.LogicalStructure.Element**:

- علامة (إضافة علامات إلى مشغلين محددين مثل الصور والنصوص والروابط)
- InsertChild
- RemoveChild
- ClearChilds

أيضًا، في هذا الإصدار أصبح من الممكن إنشاء PDF قابل للوصول باستخدام وظائف منخفضة المستوى:

تعمل الشيفرة التالية مع مستند PDF ومحتواه المعنون، باستخدام مكتبة Aspose.PDF لمعالجته.

```cs
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create annotation span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

منذ 24.6، يسمح Aspose.PDF for .NET بتوقيع PDF باستخدام X509Certificate2 بتنسيق base64:

```cs
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create annotation delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving annotation response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.5

يسمح هذا الإصدار لنا بالعمل مع طبقات PDF. على سبيل المثال:

- قفل طبقة PDF
- استخراج عناصر طبقة PDF
- تسوية PDF متعدد الطبقات
- دمج جميع الطبقات داخل PDF في واحدة

### قفل طبقة PDF

منذ إصدار 24.5، يمكنك فتح PDF، قفل طبقة معينة في الصفحة الأولى، وحفظ الوثيقة مع التغييرات. تمت إضافة طريقتين جديدتين وخصيصة واحدة:

Layer.Lock(); - يقفل الطبقة.
Layer.Unlock(); - يفتح الطبقة.
Layer.Locked; - خاصية، تشير إلى حالة قفل الطبقة.

```cs
private static void LockLayerInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

### استخراج عناصر طبقة PDF

تسمح مكتبة Aspose.PDF for .NET باستخراج كل طبقة من الصفحة الأولى وحفظ كل طبقة في ملف منفصل.

لإنشاء PDF جديد من طبقة، يمكن استخدام الشيفرة التالية:

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

### تسوية PDF متعدد الطبقات

تفتح مكتبة Aspose.PDF for .NET PDF، وتقوم بالتكرار عبر كل طبقة في الصفحة الأولى، وتسوي كل طبقة، مما يجعلها دائمة على الصفحة.

```cs
private static void FlattenPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }

        // Save PDF document
        document.Save(dataDir + "FlattenedLayersPdf_out.pdf");
    }
}
```

تقبل طريقة 'Layer.Flatten(bool cleanupContentStream)' المعامل البولياني الذي يحدد ما إذا كان يجب إزالة علامات مجموعة المحتوى الاختيارية من تدفق المحتوى. يؤدي تعيين معامل cleanupContentStream إلى false إلى تسريع عملية التسوية.

### دمج جميع الطبقات داخل PDF في واحدة

تسمح مكتبة Aspose.PDF for .NET بدمج جميع طبقات PDF أو طبقة معينة في الصفحة الأولى في طبقة جديدة وحفظ الوثيقة المحدثة.

تمت إضافة طريقتين لدمج جميع الطبقات في الصفحة:

- void MergeLayers(string newLayerName);
- void MergeLayers(string newLayerName, string newOptionalContentGroupId); 

يسمح المعامل الثاني بإعادة تسمية علامة مجموعة المحتوى الاختيارية. القيمة الافتراضية هي "oc1" (/OC /oc1 BDC).

```cs
private static void MergePdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        page.MergeLayers("NewLayerName");
        // Or
        // page.MergeLayers("NewLayerName", "OC1");

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.4

يدعم هذا الإصدار تطبيق قناع قص على الصور:

```cs
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

منذ 24.4 يمكنك اختيار مصدر الورق حسب حجم صفحة PDF في مربع حوار الطباعة باستخدام واجهة برمجة التطبيقات

بدءًا من Aspose.PDF 24.4، يمكن تبديل هذا التفضيل تشغيلًا وإيقافًا باستخدام خاصية Document.PickTrayByPdfSize أو واجهة PdfContentEditor:

```cs
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

        // Set the flag to choose annotation paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```

```cs
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose annotation paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```

من هذا الإصدار تمت إضافة Aspose.PDF Signature لـ .NET plugin:

- مثال مع إنشاء حقل جديد وخيارات:

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set extra options
opt.Reason = "my Reason";
opt.Contact = "my Contact";
opt.Location = "my Location";
// perform the process
plugin.Process(opt);
```

- مثال مع حقل فارغ موجود

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path with empty signature field
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set name of existing signature field
opt.Name = "Signature1";
// perform the process
plugin.Process(opt);
```

## ما الجديد في Aspose.PDF 24.3

من هذا الإصدار تمت إضافة PDF/A Converter لـ .NET plugin:

```cs
var options = new PdfAConvertOptions
{
    PdfAVersion = PdfAStandardVersion.PDF_A_3B
};

// Add the source file
options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // replace with your actual file path

// Add the path to save the converted file
options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

// Create the plugin instance
var plugin = new PdfAConverter();

// Run the conversion
plugin.Process(options);
```

- تنفيذ بحث عبر قائمة العبارات في TextFragmentAbsorber:

```cs
private static void SearchMultipleRegex()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

منذ 24.3 أصبح من الممكن إضافة حقل توقيع فارغ على كل صفحة إلى ملف PDF/A

```cs
private static void AddEmptySignatureFieldOnEveryPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var fieldName = "signature_1234";

    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // The new suggested code, using SignatureField object
        var signatureField = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(10, 10, 100, 100));

        // Add the default appearance for the signature field
        signatureField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(signatureField, fieldName, 1);

        // Find annotation associated with the field
        Aspose.Pdf.Annotations.Annotation addedAnnotation = null;
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            if (annotation.FullName == fieldName)
            {
                addedAnnotation = annotation;
                break;
            }
        }

        // Add the annotation to every page except of initial
        if (addedAnnotation != null)
        {
            for (int p = 2; p <= document.Pages.Count; p++)
            {
                document.Pages[p].Annotations.Add(addedAnnotation);
            }
        }

        // Save PDF document
        document.Save(dataDir + "outputPdfaWithSignatureFields.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 24.2

منذ 24.2 أصبح من الممكن الحصول على بيانات المتجه من ملف PDF

تم تنفيذ GraphicsAbsorber للحصول على بيانات المتجه من الوثائق:

```cs
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

## ما الجديد في Aspose.PDF 24.1

منذ إصدار 24.1 أصبح من الممكن استيراد التعليقات التوضيحية بتنسيق FDF إلى PDF:

```cs
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

أيضًا، يدعم الوصول إلى قاموس الصفحة أو فهرس الوثيقة.

إليك أمثلة على الشيفرة لـ DictionaryEditor:

- إضافة قيم جديدة

```cs
/private static void AddNewKeysToPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // example of key's names
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new Aspose.Pdf.DataEditor.CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new Aspose.Pdf.DataEditor.CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new Aspose.Pdf.DataEditor.CosPdfNumber(11.2));

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditor_out.pdf");
    }
}
```

- إضافة وتعيين قيم إلى القاموس

```cs
private static void ModifyKeysInPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("Old data"));
        // Modify existing value
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("New data");

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorEdit_out.pdf");
    }
}
```

- الحصول على قيمة من القاموس

```cs
private static void GetValuesFromPdfPageDicrionary()
{
    string KEY_NAME = "name";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // or 
        Aspose.Pdf.DataEditor.ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
}
```

- إزالة قيمة من القاموس

```cs
private static void RemoveFromPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";
    string EXPECTED_NAME = "name data";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorRemove_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 23.12

يمكن العثور على النموذج واستبدال النص باستخدام الشيفرة التالية:

```cs
private static void ReplaceTextInPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

أو، يمكن إزالة النموذج بالكامل:

```cs
private static void DeleteSpecifiedForm1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

نسخة أخرى من إزالة النموذج:

```cs
private static void DeleteSpecifiedForm2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
``` 

- يمكن حذف جميع النماذج باستخدام الشيفرة التالية:

```cs
private static void RemoveAllForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

- تنفيذ تحويل PDF إلى Markdown:

```cs
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        };
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

- تنفيذ تحويل OFD إلى PDF:

```cs
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```

من هذا الإصدار تمت إضافة Merger plugin:

```cs
private static void PdfMergeUsingPlugin()
{
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Create annotation new instance of Merger
    using (var merger = new Aspose.Pdf.Plugins.Merger())
    {
        // Create MergeOptions
        var opt = new Aspose.Pdf.Plugins.MergeOptions();
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat1.pdf"));
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat2.pdf"));
        opt.AddOutput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "ConcatenatePdfFiles_out.pdf"));

        // Process the PDF merging
        merger.Process(opt);
    }
}
```

أيضًا، من هذا الإصدار تمت إضافة ChatGPT plugin:

```cs
private static async void InvokeChatGptPlugin()
{
    using (var plugin = new Aspose.Pdf.Plugins.PdfChatGpt())
    {
        var options = new Aspose.Pdf.Plugins.PdfChatGptRequestOptions();
        options.AddOutput(new Aspose.Pdf.Plugins.FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
        options.ApiKey = "Your API key."; // You need to provide the key to access the API.
        options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

        // Add the request messages.
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "You are annotation helpful assistant.",
            Role = Aspose.Pdf.Plugins.Role.System
        });
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "What is the biggest pizza diameter ever made?",
            Role = Aspose.Pdf.Plugins.Role.User
        });

        // Process the request.
        var result = await plugin.ProcessAsync(options);

        var fileResultPath = result.ResultCollection[0].Data;

        // The ChatGPT API chat completion object.
        var chatCompletionObject = result.ResultCollection[1].Data as Aspose.Pdf.Plugins.ChatCompletion;
    }
}
```

## ما الجديد في Aspose.PDF 23.11

من هذا الإصدار أصبح من الممكن إزالة النص المخفي من ملف PDF:

```cs
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
}
```

منذ 23.11 يدعم انقطاع الخيوط:

```cs
private static void InterruptExample()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var monitor = new Aspose.Pdf.Multithreading.InterruptMonitor())
    {
        // An class that can produce long-drawn-out work
        RowSpanWorker worker = new RowSpanWorker(dataDir + "RowSpanWorker_out.pdf", monitor);

        var thread = new System.Threading.Thread(new System.Threading.ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption)
        System.Threading.Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }
}

private class RowSpanWorker
{
    private readonly string outputPath;
    private readonly Aspose.Pdf.Multithreading.InterruptMonitor monitor;

    public RowSpanWorker(string outputPath, Aspose.Pdf.Multithreading.InterruptMonitor monitor)
    {
        this.outputPath = outputPath;
        this.monitor = monitor;
    }

    public void Work()
    {
        // This is some large text, used Lorem Ipsum in 10000 characters to cause suspension in processing
        string text = RunExamples.GetLoremIpsumString(10000);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            Aspose.Pdf.Multithreading.InterruptMonitor.ThreadLocalInstance = this.monitor;
            var page = document.Pages.Add();

            var table = new Aspose.Pdf.Table
            {
                DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
            };

            var row0 = table.Rows.Add();

            // Add annotation cell that spans for two rows and contains annotation long-long text
            var cell00 = row0.Cells.Add(text);
            cell00.RowSpan = 2;
            cell00.IsWordWrapped = true;
            row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
            row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

            var row1 = table.Rows.Add();
            row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
            row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

            page.Paragraphs.Add(table);

            try
            {
                // Save PDF document
                document.Save(this.outputPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```

## ما الجديد في Aspose.PDF 23.10

تقدم التحديث الحالي ثلاث نسخ من إزالة العلامات من ملفات PDF المعنونة.

- إزالة بعض عناصر العقدة من documentElement (عنصر شجرة الجذر):

```cs
private static void RemoveStructElement()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as Aspose.Pdf.Structure.StructElement : null;

        if (documentElement.Children.Remove(structElement))
        {
            // Element removed. Save PDF document.
            document.Save(dataDir + "StructureElementsRemoved.pdf");
        }

        // You can also delete the structElement itself
        //if (structElement != null)
        //{
        //    structElement.Remove();
        //    document.Save(outputPdfPath);
        //}
    }
}
```

- إزالة جميع عناصر العلامات من الوثيقة، ولكن الاحتفاظ بعناصر الهيكل:

```cs
private static void RemoveMarkedElementsTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var root = structure.Children[0];
        var queue = new Queue<Aspose.Pdf.Structure.Element>();
        queue.Enqueue(root);

        while (queue.TryDequeue(out var element))
        {
            foreach (var child in element.Children)
            {
                queue.Enqueue(child);
            }

            if (element is Aspose.Pdf.Structure.TextElement || element is Aspose.Pdf.Structure.FigureElement)
            {
                element.Remove();
            }
        }

        // Save PDF document
        document.Save(dataDir + "MarkedElementsTagsRemoved.pdf");
    }
}
```

- إزالة العلامات بالكامل:

```cs
private static void RemoveTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        documentElement.Remove();

        // Save PDF document
        document.Save(dataDir + "TagsRemoved.pdf");
    }
}
```

منذ 23.10 تم تنفيذ ميزة جديدة لقياس ارتفاع الحرف. استخدم الشيفرة التالية لقياس ارتفاع حرف.

```cs
private static void DisplayCharacterHeight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextFragmentAbsorber to get information about state of document text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Get height of 'A' character being displayed with font of first text fragment
        var textState = absorber.TextFragments[1].TextState;
        var height = textState.MeasureHeight('A');
        Console.WriteLine("The height of 'A' character displayed with {0} font size of {1} is {2:N3}", textState.Font.FontName, textState.FontSize,height);
    }
}
```

لاحظ أن القياس يعتمد على الخط المضمن في الوثيقة. إذا كانت أي معلومات عن بُعد مفقودة، فإن هذه الطريقة تعيد 0.

أيضًا، يوفر هذا الإصدار توقيع PDF باستخدام HASH الموقع:

```cs
private static void SignPdfUsingSignedHash(string certP12, string pfxPassword)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(certP12, pfxPassword);

        // Create a delegate to external sign
        pkcs7.CustomSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            X509Certificate2 signerCert = new X509Certificate2(certP12, pfxPassword, X509KeyStorageFlags.Exportable);
            RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);    //not supported on core 2.0
            rsaCSP.FromXmlString(xmlString);                            //not supported on core 2.0

            byte[] signedData = rsaCSP.SignHash(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };

        // Sign PDF file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);

        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Verify
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "SignWithCertificate_out.pdf");

        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}
```

ميزة جديدة أخرى هي إعدادات طباعة مربع الحوار لتكبير الصفحة:

```cs
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

## ما الجديد في Aspose.PDF 23.9

منذ 23.9 دعم إزالة تعليق فرعي من حقل قابل للتعبئة.

```cs
private static void RemoveChildAnnotationFromFillableField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldWithChildAnnots.pdf"))
    {
        // Get field with child annotations
        var field = (Aspose.Pdf.Forms.Field)document.Form["1 Vehicle Identification Number"];
        // Get first child annotation
        var annotation = field[1];
        // Remove the annotation
        document.Pages[annotation.PageIndex].Annotations.Remove(annotation);

        // Save PDF document
        document.Save(dataDir + "RemoveChildAnnotation_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 23.8

منذ 23.8 دعم إضافة اكتشاف التحديثات التزايدية.

تمت إضافة وظيفة لاكتشاف التحديثات التزايدية في مستند PDF. تعيد هذه الوظيفة 'true' إذا تم حفظ مستند مع تحديثات تزايدية؛ خلاف ذلك، تعيد 'false'.

```cs
private static bool HasIncrementalUpdate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithIncrementalUpdate.pdf"))
    {
        // New method
        bool hasIncrementalUpdate = document.HasIncrementalUpdate();

        Console.WriteLine("Document {0} incremental update check returns: {1}", document.FileName, hasIncrementalUpdate);
        return hasIncrementalUpdate;
    }
}
```

أيضًا، 23.8 يدعم طرق العمل مع حقول خانة الاختيار المتداخلة. تحتوي العديد من نماذج PDF القابلة للتعبئة على حقول خانة اختيار تعمل كمجموعات راديو:

- إنشاء حقل خانة اختيار متعدد القيم:

```cs
private static void CreateMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var checkbox = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
        checkbox.ExportValue = "option 1";

        // Add new option right under existing ones
        checkbox.AddOption("option 2");

        // Add new option at the given rectangle
        checkbox.AddOption("option 3", new Aspose.Pdf.Rectangle(100, 100, 120, 120));

        document.Form.Add(checkbox);

        // Select the added checkbox
        checkbox.Value = "option 2";

        // Save PDF document
        document.Save(dataDir + "MultivalueCheckboxField.pdf");
    }
}
```

- الحصول على قيمة خانة اختيار متعددة القيم وتعيينها:

```cs
private static void GetAndSetValueOfMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MultivalueCheckboxField.pdf"))
    {
        var form = document.Form;
        var checkbox = form.Fields[0] as Aspose.Pdf.Forms.CheckboxField;

        // Allowed values may be retrieved from the AllowedStates collection
        // Set the checkbox value using Value property
        checkbox.Value = checkbox.AllowedStates[0];
        var checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

        // The value should be any element of AllowedStates
        checkbox.Value = "option 2";
        checkboxValue = checkbox.Value; // option 2

        // Uncheck boxes by either setting Value to "Off" or setting Checked to false
        checkbox.Value = "Off";
        // or, alternately:
        // checkbox.Checked = false;
        checkboxValue = checkbox.Value; // Off
    }
}
```

## ما الجديد في Aspose.PDF 23.7

من Aspose.PDF 23.7 دعم إضافة استخراج الشكل:

```cs
private static void CopyShape()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Create PDF document
        using (var destDocument = new Aspose.Pdf.Document())
        {
            // Absorb vector graphics from the source document
            var graphicAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();
            graphicAbsorber.Visit(sourceDocument.Pages[1]);

            // Copy the graphics into the destination document specified page and area
            var area = new Aspose.Pdf.Rectangle(90, 250, 300, 400);
            destDocument.Pages[1].AddGraphics(graphicAbsorber.Elements, area);

            // Save PDF document
            destDocument.Save(dataDir + "CopyShape_out.pdf");
        }
    }
}
```

كما يدعم القدرة على اكتشاف Overflow عند إضافة نص:

```cs
private static void FitTextIntoRectangle()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document()) 
    {
        // Generate text to add: "Lorem Ipsum" text of 1000 characters
        var paragraphContent = RunExamples.GetLoremIpsumString(1000);
        // Create a text fragment with the desired text
        var fragment = new Aspose.Pdf.Text.TextFragment(paragraphContent);
        // Declare the rectangle to fit text into
        var rectangle = new Aspose.Pdf.Rectangle(100, 600, 500, 700, false);
        
        // Check whether the text fits into the rectangle
        var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);

        // Iteratively decrease font size until text fits the rectangle
        while (!isFitRectangle)
        {
            fragment.TextState.FontSize -= 0.5f;
            isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
        }

        // Create a paragraph from the text fragment in the specified rectangle. Now you may be sure it fits.
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        paragraph.Rectangle = rectangle;
        paragraph.AppendLine(fragment);

        // Create a text builder to place the paragraph on the document page
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages.Add());
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "FitTextIntoRectangle_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 23.6

من Aspose.PDF 23.6 دعم إضافة المكونات الإضافية التالية:

- Aspose PdfConverter Html إلى PDF 
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

تحديث Aspose.PdfForm 
- إضافة ميزة "تصدير القيم من الحقول في الوثيقة إلى ملف CSV"
- إضافة القدرة على تعيين الخصائص لحقول منفصلة

كما يدعم إضافة القدرة على تعيين عنوان HTML، صفحة Epub:

```cs
private static void SetHtmlTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            ExplicitListOfSavedPages = new[] { 1 },
            SplitIntoPages = false,
            FixedLayout = true,
            CompressSvgGraphicsIfAny = false,
            SaveTransparentTexts = true,
            SaveShadowedTextsAsTransparentTexts = true,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            // New property
            Title = "Title for page"
        };

        // Save HTML document
        document.Save(dataDir + "SetHtmlTitle_out.html", options);
    }
}
```

## ما الجديد في Aspose.PDF 23.5

منذ 23.5 دعم إضافة خيار FontSize لـ RedactionAnnotation. استخدم الشيفرة التالية لحل هذه المهمة:

```cs
private static void AddRedactionAnnotationFontSize() 
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf")) 
    {
        // Create RedactionAnnotation instance for specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1],
            new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
        annot.FillColor = Aspose.Pdf.Color.Black;

        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;
        // Text to be printed on redact annotation
        annot.OverlayText = "(Unknown)";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Repat Overlay text over redact Annotation
        annot.Repeat = false;

        // New property
        annot.FontSize = 20;

        // Add annotation to annotations collection of first page
        document.Pages[1].Annotations.Add(annot);
        // Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)
        annot.Redact();
        // Save PDF document
        document.Save(dataDir + "AddRedactionAnnotationFontSize_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 23.4

أعلنت Aspose.PDF عن إصدار .NET 7 SDK.

## ما الجديد في Aspose.PDF 23.3.1

من Aspose.PDF 23.3 دعم إضافة المكونات الإضافية التالية:

- Aspose.PdfForm
- Aspose.PdfConverter PDF إلى HTML
- Aspose.PdfConverter PDF إلى XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator للصور

## ما الجديد في Aspose.PDF 23.3

قدمت النسخة 23.3 دعمًا للحفاظ على نسب الصورة والدقة أثناء الإدراج على الصفحة. يمكن استخدام طريقتين لحل هذه المشكلة:

```cs
private static void InsertImageWithNativeResolutionAsTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "600"
        };

        for (var j = 0; j < 2; j++)
        {
            var row = table.Rows.Add();
            var cell = row.Cells.Add();
            cell.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsTable_out.pdf");
    }
}
```

والنهج الثاني:

```cs
private static void InsertImageWithNativeResolutionAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        for (var j = 0; j < 2; j++)
        {
            page.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsParagraph_out.pdf");
    }
}
```

سيتم وضع الصورة بحجم مقاس ومعدل دقة أصلي. يمكنك تعيين خصائص FixedWidth أو FixedHeight بالاشتراك مع IsApplyResolution.

## ما الجديد في Aspose.PDF 23.1.1

من Aspose.PDF 23.1.1 دعم إضافة المكونات الإضافية التالية:

- Aspose.PdfOrganizer plugin
- Aspose.PdfExtractor plugin

## ما الجديد في Aspose.PDF 23.1

منذ الإصدار 23.1 دعم إنشاء تعليق PrinterMark.

علامات الطابعة هي رموز رسومية أو نصوص تُضاف إلى صفحة لمساعدة موظفي الإنتاج في تحديد مكونات وظيفة متعددة الألواح والحفاظ على إنتاج متسق أثناء الإنتاج. تشمل الأمثلة الشائعة المستخدمة في صناعة الطباعة:

- أهداف التسجيل لمحاذاة الألواح
- درجات الرمادي وأشرطة الألوان لقياس الألوان وكثافات الحبر
- علامات القطع التي توضح مكان تقليم الوسيط الناتج

سنظهر مثالًا على الخيار مع أشرطة الألوان لقياس الألوان وكثافات الحبر. هناك فئة مجردة أساسية PrinterMarkAnnotation ومن ثم فئة فرعية ColorBarAnnotation - التي تنفذ بالفعل هذه الشرائط. دعونا نتحقق من المثال:

```cs
private static void AddPrinterMarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);

        var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
        var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
        var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

        var colorBarBlack = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectBlack);
        var colorBarCyan = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectCyan,
            Aspose.Pdf.Annotations.ColorsOfCMYK.Cyan);
        var colorBarMagenta = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectMagenta);
        colorBarMagenta.ColorOfCMYK = Aspose.Pdf.Annotations.ColorsOfCMYK.Magenta;
        var colorBarYellow = new Aspose.Pdf.Annotations.ColorBarAnnotation(page,
            new Aspose.Pdf.Rectangle(400, 250, 450, 700), Aspose.Pdf.Annotations.ColorsOfCMYK.Yellow);

        page.Annotations.Add(colorBarBlack);
        page.Annotations.Add(colorBarCyan);
        page.Annotations.Add(colorBarMagenta);
        page.Annotations.Add(colorBarYellow);

        // Save PDF document
        document.Save(dataDir + "PrinterMarkAnnotation_out.pdf");
    }
}
```
كما يدعم استخراج الصور المتجهة. حاول استخدام الشيفرة التالية لاكتشاف واستخراج الرسومات المتجهة:

```cs
private static void SavePdfVectorGraphicToSvg()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Attempt to save the vector graphics into a specified SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "PdfVectorGraphicToSvg.svg");
    }
}
```

## ما الجديد في Aspose.PDF 22.12

من هذا الإصدار دعم تحويل PDF إلى صورة DICOM

```cs
private static void PdfToDicom()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PagesToImages.pdf"))
    {
        var dicom = new Aspose.Pdf.Devices.DicomDevice();
        FileStream outStream = new FileStream(dataDir + "PdfToDicom_out.dcm", FileMode.Create, FileAccess.ReadWrite);
        dicom.Process(document.Pages[1], outStream);
    }
}
```    

## ما الجديد في Aspose.PDF 22.09

منذ 22.09 دعم إضافة خاصية لتعديل ترتيب العناوين الموضوعية (E=، CN=، O=، OU=،) في التوقيع.

```cs
private static void SignPdfWithModifiedOrderOfSubjectRubrics(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password);

        // Set signature custom appearance
        signature.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.CN, Aspose.Pdf.Forms.SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.OU, Aspose.Pdf.Forms.SubjectNameElements.S, Aspose.Pdf.Forms.SubjectNameElements.C }
        };

        // Sign PDF file
        fileSign.Sign(1, true, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithModifiedOrderOfSubjectRubrics_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 22.6

منذ 22.5 دعم استخراج نص SubScript وSuperScript من PDF.

إذا كان مستند PDF يحتوي على نص SubScript وSuperScript مثل H2O، فإن استخراج النص من PDF يجب أن يستخرج أيضًا معلومات التنسيق الخاصة بهم (في النص المستخرج).
إذا كان PDF يحتوي على نص مائل، يجب أيضًا تضمينه في المحتوى المستخرج.

```cs
private static void ExtractTextSuperscript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextWithSubscriptsSuperscripts.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Iterate through text fragments to find superscript text
        foreach (var textFragment in absorber.TextFragments) 
        {
            if (textFragment.TextState.Superscript)
            {
                Console.WriteLine(String.Format("Text {0} at {1} is superscript!", textFragment.Text, textFragment.Position));
            }
        }
    }
}
```

## ما الجديد في Aspose.PDF 22.4

يتضمن هذا الإصدار معلومات لـ Aspose.PDF for .NET:

- PDF إلى ODS: التعرف على النص في النص الفرعي والنص الفوقي؛

**مثال**

```cs
private static void ConvertPdfToOds()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            // Specify the desired table file format
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

- PDF إلى XMLSpreadSheet2003: التعرف على النص في النص الفرعي والنص الفوقي؛

- PDF إلى Excel: التعرف على النص في النص الفرعي والنص الفوقي؛

- إزالة توقيعات UR أثناء حفظ الوثيقة؛

- إزالة علامة الشك في MarkInfo أثناء حفظ الوثيقة؛

- إزالة المعلومات أثناء حفظ الوثيقة

## ما الجديد في Aspose.PDF 22.3

يتضمن هذا الإصدار التحديثات التالية:

- دعم AFRelationship؛

- التحقق من رأس PDF؛

- إزالة adbe.x509.rsa_sha1 subfilter أثناء حفظ الوثيقة؛

- تنسيق الحقل كرقم وتنسيق التاريخ؛

- حظر استخدام تشفير RC4 في FDF 2.0.

## ما الجديد في Aspose.PDF 22.2

من الإصدار 22.2 أصبح من الممكن توقيع مستند باستخدام PdfFileSignature مع LTV، مع القدرة على تغيير التجزئة من SHA1 إلى SHA256.

```csharp
private static void SignPdfWithSha256(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(300, 100, 1, 1);
        var signature = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password)
        {
            UseLtv = true,
            TimestampSettings = new Aspose.Pdf.TimestampSettings("http://freetsa.org/tsr", string.Empty, Aspose.Pdf.DigestHashAlgorithm.Sha256)
        };

        // Sign PDF file
        fileSign.Sign(1, false, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithSha256_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 22.1

الآن، Aspose.PDF for .NET يدعم تحميل المستندات من أحد أكثر تنسيقات المستندات شعبية، تنسيق المستند المحمول (PDF) الإصدار 2.0.

## ما الجديد في Aspose.PDF 21.11

### السماح بحروف غير لاتينية في كلمة المرور

```csharp
private static void EncriptPdfNonlatinPassCharacters()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        bool isSuccessful = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print,
            Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
        Console.WriteLine(isSuccessful);
        // Save PDF document
        fileSecurity.Save(dataDir + "PdfNonlatinPassEncrypted_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 21.10

### كيفية اكتشاف النص المخفي؟

يرجى استخدام TextState.Invisible للحصول على معلومات حول عدم وضوح النص خارج إعداد وضع العرض.

استخدمنا الشيفرة التالية للاختبار:

```csharp
private static void DisplayTextInvisibility()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithHiddenText.pdf"))
    {
        Console.WriteLine(document.FileName);

        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);
        var textFragmentCollection = absorber.TextFragments;

        // Iterate through text fragments to find hidden text
        for (int i = 1; i <= textFragmentCollection.Count; i++)
        {
            var fragment = textFragmentCollection[i];
            Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
            Console.WriteLine("Text: {0}", fragment.Text);
            Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
            Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
            Console.WriteLine("---");
        }
    }
}
```

### كيف يمكن الحصول على معلومات حول عدد الطبقات في مستند PDF؟

```csharp
private static void GetPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithLayers.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;
        // Save each layer to the output path
        foreach (var layer in layers)
        {
            Console.WriteLine("Document {0} contains a layer named: {1} ", document.FileName, layer.Name);
        }
    }
}
```

## ما الجديد في Aspose.PDF 21.9

تخصيص لون الخلفية لمظهر التوقيع ولون خط التسميات في منطقة التوقيع مع Aspose.PDF for .NET.

```csharp
private static void SignPdfWithCustomColorsInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set colors
            ForegroundColor = Aspose.Pdf.Color.DarkGreen,
            BackgroundColor = Aspose.Pdf.Color.LightSeaGreen,
        };
        // Sign PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "SignPdfWithCustomColorsInAppearance_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 21.8

### كيفية تغيير لون النص في التوقيع الرقمي؟

في الإصدار 21.8، خاصية ForegroundColor، تتيح تغيير لون النص في التوقيع الرقمي.

```csharp
private static void SignPdfWithForegroundColorInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set text color
            ForegroundColor = Aspose.Pdf.Color.Green
        };
        // Sign PDF file
        pdfSign.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfSign.Save(dataDir + "SignPdfWithForegroundInAppearance_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 21.7

### إنشاء PDF بناءً على XML و XLS مع المعلمات

لإضافة معلمات XSL، نحتاج إلى إنشاء [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) الخاصة بنا وتعيينها كخاصية في [XslFoLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/xslfoloadoptions). توضح الشيفرة التالية كيفية استخدام هذه الفئة مع الملفات النموذجية الموضحة أعلاه.

```csharp
private static void ConvertXslfoToPdfWithArgumentList()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");

    // Example of using XsltArgumentList
    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XslfoToPdfWithArgumentList_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 21.6

مع Aspose.PDF for .NET يمكنك إخفاء الصور باستخدام ImagePlacementAbsorber من الوثيقة:

```csharp
private static void HideImageInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        // Create ImagePlacementAbsorber instance
        var absorber = new Aspose.Pdf.ImagePlacementAbsorber();
        // Load the images of the first page
        document.Pages[1].Accept(absorber);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in absorber.ImagePlacements)
        {
            // Hide image
            imagePlacement.Hide();
        }

        // Save PDF document
        document.Save(dataDir + "HideImageInPdf_out.pdf");
    }
}
```

## ما الجديد في Aspose.PDF 21.5

### كيفية استخراج الاسم الكامل للخط من وصفه/موارده في PDF؟

يمكنك الحصول على خط كامل مع البادئة باستخدام خاصية BaseFont لفئة Font.

```csharp
private static void DisplayFontFullNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Get document fonts
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through the fonts
        foreach (var font in fonts)
        {
            // Show font names
            Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
        }
    }
}
```

## ما الجديد في Aspose.PDF 21.4

### إضافة واجهة برمجة التطبيقات لدمج الصور

يسمح Aspose.PDF 21.4 لك بدمج الصور. اتبع الشيفرة التالية:

```csharp
private static void MergeAsJpeg()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImages to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(inputImagesStreams,
                  Aspose.Pdf.Drawing.ImageFormat.Jpeg, Aspose.Pdf.Facades.ImageMergeMode.Vertical, 1, 1))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.jpg", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

يمكنك أيضًا دمج صورك بتنسيق Tiff:

```csharp
private static void MergeAsTiff()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImagesAsTiff to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(inputImagesStreams))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.tiff", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

## ما الجديد في Aspose.PDF 21.3

### الكشف العام عن خاصية لاكتشاف حماية المعلومات من Azure

مع الشيفرة التالية، يجب أن تكون قادرًا على الوصول إلى الحمولة المشفرة لملفات PDF الخاصة بك، المحمية بواسطة حماية المعلومات من Azure:

```csharp
private static void AzureInformationProtection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        if (document.EmbeddedFiles[1].AFRelationship == Aspose.Pdf.AFRelationship.EncryptedPayload)
        {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
                // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
                // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
                // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
        }
    }
}
```

## ما الجديد في Aspose.PDF 21.1

### إضافة دعم لاسترداد لون الخلفية لـ TextFragment

في هذا الإصدار من Aspose.PDF، أصبحت الوظيفة متاحة لاسترداد لون الخلفية. تحتاج إلى تحديد searchOptions.SearchForTextRelatedGraphics = true؛ في خيارات كائن TextFragmentAbsorber.

يرجى النظر في الشيفرة التالية:

```csharp
private static void DisplayPdfTextBackgroundColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTextBackgroundColor.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        var searchOptions = new Aspose.Pdf.Text.TextSearchOptions(false);
        // Setting this option into the 'true' is necessary 
        searchOptions.SearchForTextRelatedGraphics = true;
        textFragmentAbsorber.TextSearchOptions = searchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);
        
        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            Console.WriteLine("Text: '{0}'", textFragment.Text);
            Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
            Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
            Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
        }
    }
}
```

### بعد التحويل إلى HTML، يتم تضمين الخط بالكامل في الناتج

أيضًا، في Aspose.PDF 21.1، بعد تحويل PDF إلى HTML، أصبحت الخطوط المضمنة متاحة في مستند HTML الناتج. يمكن تحقيق ذلك مع خيار الحفظ الجديد البولياني HtmlSaveParameter.SaveFullFont.

إليك الشيفرة:

```csharp
private static void PdfToHtmlWithFullFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            LettersPositioningMethod = Aspose.Pdf.HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF,
            SaveTransparentTexts = true,
            // New option
            SaveFullFont = true
        };
        // Save HTML document
        document.Save(dataDir + "PdfToHtmlWithFullFont_out.html", options);
    }
}
```