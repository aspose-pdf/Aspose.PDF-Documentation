---
title: تنسيق مستند PDF باستخدام C#
linktitle: تنسيق مستند PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/formatting-pdf-document/
description: إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF for .NET. استخدم مقتطف الشيفرة التالي لحل مهامك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "اكتشف الميزة الجديدة القوية لـ Aspose.PDF for .NET التي تتيح للمستخدمين إنشاء وتنسيق مستندات PDF بسلاسة. مع التحكم الشامل في خصائص المستند مثل إعدادات عرض النافذة، خيارات تضمين الخطوط، وعوامل التكبير القابلة للتخصيص، يمكن للمطورين تحسين تجربة المستخدم والحفاظ على سلامة المستند عبر منصات مختلفة. قم بتحسين مهام معالجة PDF الخاصة بك مع هذه الوظيفة القوية التي تحسن بشكل كبير من كفاءة تطبيقات .NET الخاصة بك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF for .NET. استخدم مقتطف الشيفرة التالي لحل مهامك."
}
</script>

## تنسيق مستند PDF

### الحصول على خصائص نافذة المستند وعرض الصفحة

تساعدك هذه الموضوعات على فهم كيفية الحصول على خصائص نافذة المستند، وتطبيق العرض، وكيفية عرض الصفحات. لتعيين هذه الخصائص:

افتح ملف PDF باستخدام [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class. الآن، يمكنك تعيين خصائص كائن Document، مثل

- CenterWindow – مركز نافذة المستند على الشاشة. الافتراضي: false.
- Direction – ترتيب القراءة. يحدد كيفية عرض الصفحات عند عرضها جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: false (يتم عرض العنوان).
- HideMenuBar – إخفاء أو عرض شريط قائمة نافذة المستند. الافتراضي: false (يتم عرض شريط القائمة).
- HideToolBar – إخفاء أو عرض شريط أدوات نافذة المستند. الافتراضي: false (يتم عرض شريط الأدوات).
- HideWindowUI – إخفاء أو عرض عناصر نافذة المستند مثل أشرطة التمرير. الافتراضي: false (يتم عرض عناصر واجهة المستخدم).
- NonFullScreenPageMode – كيفية عرض المستند عندما لا يتم عرضه في وضع ملء الشاشة.
- PageLayout – تخطيط الصفحة.
- PageMode – كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض المصغرات، ملء الشاشة، عرض لوحة المرفقات.

يعمل مقتطف الشيفرة التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يظهر مقتطف الشيفرة التالي كيفية الحصول على الخصائص باستخدام [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### تعيين خصائص نافذة المستند وعرض الصفحة

تشرح هذه الموضوعات كيفية تعيين خصائص نافذة المستند، وتطبيق العرض، وعرض الصفحة. لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.
1. قم بتعيين خصائص كائن Document.
1. احفظ ملف PDF المحدث باستخدام طريقة Save.

الخصائص المتاحة هي:

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

يتم استخدام كل منها ووصفها في الشيفرة أدناه. يظهر مقتطف الشيفرة التالي كيفية تعيين الخصائص باستخدام [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### تضمين الخطوط في ملف PDF موجود

تدعم قارئات PDF [مجموعة أساسية من 14 خطًا](https://en.wikipedia.org/wiki/PDF#Text) بحيث يمكن عرض المستندات بنفس الطريقة بغض النظر عن النظام الأساسي الذي يتم عرض المستند عليه. عندما يحتوي PDF على خط ليس من بين الخطوط الأربعة عشر الأساسية، يجب تضمين الخط في ملف PDF لتجنب استبدال الخط.

يدعم Aspose.PDF for .NET تضمين الخطوط في ملفات PDF الموجودة. يمكنك تضمين خط كامل أو مجموعة فرعية من الخط. لتضمين الخط، افتح ملف PDF باستخدام [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class. ثم استخدم [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) class لتضمين الخط في ملف PDF. لتضمين الخط الكامل، استخدم خاصية IsEmbeded لفئة Font؛ لاستخدام مجموعة فرعية من الخط، استخدم خاصية IsSubset.

{{% alert color="primary" %}}

تتضمن مجموعة فرعية من الخطوط فقط الأحرف المستخدمة وتكون مفيدة حيث يتم استخدام الخطوط لجمل قصيرة أو شعارات، على سبيل المثال حيث يتم استخدام خط الشركات لشعار، ولكن ليس لنص الجسم. يقلل استخدام مجموعة فرعية من حجم ملف PDF الناتج. ومع ذلك، إذا تم استخدام خط مخصص لنص الجسم، يجب تضمينه بالكامل.

{{% /alert %}}

يظهر مقتطف الشيفرة التالي كيفية تضمين خط في ملف PDF.

### تضمين الخطوط القياسية من النوع 1

تحتوي بعض مستندات PDF على خطوط من مجموعة خطوط Adobe الخاصة. تُسمى الخطوط من هذه المجموعة "خطوط قياسية من النوع 1". تتضمن هذه المجموعة 14 خطًا ويتطلب تضمين هذا النوع من الخطوط استخدام علامات خاصة أي [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). فيما يلي مقتطف الشيفرة الذي يمكن استخدامه للحصول على مستند مع جميع الخطوط المضمنة بما في ذلك خطوط قياسية من النوع 1:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة إلى استخدام أي خط بخلاف الخطوط الأربعة عشر الأساسية المدعومة من Adobe Reader، يجب عليك تضمين وصف الخط أثناء إنشاء ملف PDF. إذا لم يتم تضمين معلومات الخط، سيأخذ Adobe Reader ذلك من نظام التشغيل إذا كان مثبتًا على النظام، أو سيقوم بإنشاء خط بديل وفقًا لوصف الخط في PDF.

>يرجى ملاحظة أنه يجب تثبيت الخط المضمن على الجهاز المضيف أي في حالة الشيفرة التالية تم تثبيت خط "Univers Condensed" على النظام.

نستخدم خاصية IsEmbedded لفئة Font لتضمين معلومات الخط في ملف PDF. تعيين قيمة هذه الخاصية إلى "True" سيقوم بتضمين ملف الخط الكامل في PDF، مع العلم أنه سيزيد من حجم ملف PDF. فيما يلي مقتطف الشيفرة الذي يمكن استخدامه لتضمين معلومات الخط في PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### تعيين اسم الخط الافتراضي أثناء حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متاحة في المستند نفسه وعلى الجهاز، يقوم API باستبدال هذه الخطوط بالخط الافتراضي. عندما يكون الخط متاحًا (مثبت على الجهاز أو مضمن في المستند)، يجب أن يحتوي PDF الناتج على نفس الخط (يجب ألا يتم استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (ليس مسار ملفات الخط). لقد قمنا بتنفيذ ميزة لتعيين اسم الخط الافتراضي أثناء حفظ مستند كـ PDF. يمكن استخدام مقتطف الشيفرة التالي لتعيين الخط الافتراضي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### الحصول على جميع الخطوط من مستند PDF

في حالة رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة FontUtilities.GetAllFonts() المقدمة في [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class. يرجى مراجعة مقتطف الشيفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### الحصول على تحذيرات لاستبدال الخطوط

يوفر Aspose.PDF for .NET طرقًا للحصول على إشعارات حول استبدال الخطوط للتعامل مع حالات استبدال الخطوط. تظهر مقتطفات الشيفرة أدناه كيفية استخدام الوظائف المقابلة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

تظهر طريقة **OnFontSubstitution** كما هو مدرج أدناه.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### تحسين تضمين الخطوط باستخدام FontSubsetStrategy

يمكن تحقيق ميزة تضمين الخطوط كمجموعة فرعية باستخدام خاصية IsSubset، ولكن في بعض الأحيان تريد تقليل مجموعة الخطوط المضمنة بالكامل إلى فقط المجموعات الفرعية المستخدمة في المستند. تحتوي Aspose.Pdf.Document على خاصية FontUtilities التي تتضمن طريقة SubsetFonts(FontSubsetStrategy subsetStrategy). في طريقة SubsetFonts()، يساعد المعامل subsetStrategy في ضبط استراتيجية المجموعة الفرعية. تدعم FontSubsetStrategy نوعين من استبدال الخطوط.

- SubsetAllFonts - ستقوم هذه بتضمين جميع الخطوط المستخدمة في المستند.
- SubsetEmbeddedFontsOnly - ستقوم هذه بتضمين الخطوط التي تم تضمينها بالكامل في المستند فقط.

يظهر مقتطف الشيفرة التالي كيفية تعيين FontSubsetStrategy:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### الحصول على تعيين عامل التكبير لملف PDF

في بعض الأحيان، تريد تحديد ما هو عامل التكبير الحالي لمستند PDF. مع Aspose.Pdf، يمكنك معرفة القيمة الحالية وكذلك تعيين واحدة.

تسمح خاصية Destination لفئة [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) بالحصول على قيمة التكبير المرتبطة بملف PDF. وبالمثل، يمكن استخدامها لتعيين عامل تكبير الملف.

#### تعيين عامل التكبير

يظهر مقتطف الشيفرة التالي كيفية تعيين عامل التكبير لملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### الحصول على عامل التكبير

يظهر مقتطف الشيفرة التالي كيفية الحصول على عامل التكبير لملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### تعيين خصائص إعدادات طباعة الحوار

يسمح Aspose.PDF بتعيين خصائص إعدادات طباعة الحوار لمستند PDF. يسمح لك بتغيير خاصية DuplexMode لمستند PDF والتي يتم تعيينها على simplex بشكل افتراضي. يمكن تحقيق ذلك باستخدام طريقتين مختلفتين كما هو موضح أدناه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### تعيين خصائص إعدادات طباعة الحوار باستخدام محرر محتوى PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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