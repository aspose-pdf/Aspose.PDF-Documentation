---
title: العمل مع الإجراءات في PDF
linktitle: الإجراءات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/actions/
description: يشرح هذا القسم كيفية إضافة إجراءات إلى المستند وحقول النموذج برمجيًا باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين إضافة إجراءات برمجية إلى ملفات PDF، مما يعزز التفاعل داخل المستندات. يمكن للمستخدمين تنفيذ الروابط للتنقل داخل المستند أو إلى عناوين URL خارجية، بالإضافة إلى التلاعب بإجراءات فتح المستند للتحكم في كيفية عرض ملفات PDF عند فتحها. تعمل هذه الوظيفة القوية على تبسيط إنشاء المستندات والتفاعل لتطبيقات C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "2007",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2024-11-25",
    "description": "يشرح هذا القسم كيفية إضافة إجراءات إلى المستند وحقول النموذج برمجيًا باستخدام C#."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## إضافة رابط في ملف PDF

من الممكن إضافة روابط إلى ملفات PDF، إما للسماح للقراء بالتنقل إلى جزء آخر من PDF، أو إلى محتوى خارجي.

لإضافة روابط ويب إلى مستندات PDF:

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. الحصول على فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) التي تريد إضافة الرابط إليها.
1. إنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) باستخدام كائنات Page و [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) . يتم استخدام كائن المستطيل لتحديد الموقع على الصفحة حيث يجب إضافة الرابط.
1. تعيين خاصية Action إلى كائن [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) الذي يحدد موقع URI البعيد.
1. لعرض نص الرابط، أضف سلسلة نصية في موقع مشابه لمكان وجود كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) .
1. لإضافة نص حر:

- قم بإنشاء كائن [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) . يقبل أيضًا كائنات Page و Rectangle كوسائط، لذا من الممكن توفير نفس القيم كما هو محدد ضد مُنشئ LinkAnnotation.
- باستخدام خاصية Contents لكائن [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) ، حدد السلسلة التي يجب عرضها في ملف PDF الناتج.
- اختياريًا، قم بتعيين عرض الحدود لكل من كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) و FreeTextAnnotation إلى 0 حتى لا تظهر في مستند PDF.
- بمجرد تعريف كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) و [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) ، أضف هذه الروابط إلى مجموعة التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) .
- أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .

تظهر مقتطفات الشيفرة التالية كيفية إضافة رابط إلى ملف PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إنشاء رابط إلى الصفحات في نفس ملف PDF

تقدم Aspose.PDF for .NET ميزة رائعة لإنشاء PDF وكذلك التلاعب به. كما أنها تقدم ميزة إضافة روابط إلى صفحات PDF ويمكن أن يوجه الرابط إما إلى صفحات في ملف PDF آخر، أو عنوان URL على الويب، أو رابط لتشغيل تطبيق، أو حتى رابط إلى صفحات في نفس ملف PDF. لإضافة روابط محلية (روابط إلى صفحات في نفس ملف PDF)، تمت إضافة فئة تسمى [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) إلى مساحة أسماء Aspose.PDF وهذه الفئة تحتوي على خاصية تسمى TargetPageNumber، والتي تستخدم لتحديد الصفحة المستهدفة/الوجهة للرابط.

لإضافة الرابط المحلي، نحتاج إلى إنشاء TextFragment بحيث يمكن ربط الرابط بـ TextFragment. تحتوي فئة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) على خاصية تسمى Hyperlink والتي تستخدم لربط مثيل LocalHyperlink. تظهر مقتطفات الشيفرة التالية الخطوات اللازمة لتحقيق هذا المتطلب.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## الحصول على وجهة رابط PDF (URL)

تمثل الروابط كتعليقات توضيحية في ملف PDF ويمكن إضافتها أو تحديثها أو حذفها. تدعم Aspose.PDF for .NET أيضًا الحصول على الوجهة (URL) للرابط في ملف PDF.

للحصول على عنوان URL للرابط:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. الحصول على [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) التي تريد استخراج الروابط منها.
1. استخدم فئة [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) لاستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) من الصفحة المحددة.
1. تمرير كائن [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) إلى طريقة Accept لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) .
1. الحصول على جميع التعليقات التوضيحية المحددة في كائن IList باستخدام خاصية Selected لكائن [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) .
1. أخيرًا، استخراج إجراء LinkAnnotation كـ GoToURIAction.

تظهر مقتطفات الشيفرة التالية كيفية الحصول على وجهات الروابط (URL) من ملف PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## الحصول على نص الرابط

لدى الرابط جزئين: النص الذي يظهر في المستند، وURL الوجهة. في بعض الحالات، يكون النص بدلاً من URL هو ما نحتاجه.

يمثل النص والتعليقات التوضيحية/الإجراءات في ملف PDF كيانات مختلفة. النص على الصفحة هو مجرد مجموعة من الكلمات والأحرف، بينما تجلب التعليقات التوضيحية بعض التفاعل مثل ذلك الموجود في الرابط.

للعثور على محتوى URL، تحتاج إلى العمل مع كل من التعليق والنص. لا يحتوي كائن [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) على النص بنفسه ولكنه يقع تحت النص على الصفحة. لذا للحصول على النص، يعطي التعليق حدود URL، بينما يعطي كائن النص محتويات URL. يرجى الاطلاع على مقتطفات الشيفرة التالية.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## إزالة إجراء فتح المستند من ملف PDF

[كيفية تحديد صفحة PDF عند عرض المستند](#how-to-specify-pdf-page-when-viewing-document) يشرح كيفية إخبار المستند بفتح صفحة مختلفة عن الصفحة الأولى. عند دمج عدة مستندات، وإذا كان واحد أو أكثر منها يحتوي على إجراء GoTo محدد، فمن المحتمل أنك تريد إزالتها. على سبيل المثال، إذا كنت تجمع بين مستندين وكان الثاني يحتوي على إجراء GoTo يأخذك إلى الصفحة الثانية، فسيتم فتح المستند الناتج على الصفحة الثانية من المستند الثاني بدلاً من الصفحة الأولى من المستند المدمج. لتجنب هذا السلوك، قم بإزالة أمر إجراء الفتح.

لإزالة إجراء الفتح:

1. تعيين خاصية [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) إلى null.
1. احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن Document .

تظهر مقتطفات الشيفرة التالية كيفية إزالة إجراء فتح المستند من ملف PDF.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## كيفية تحديد صفحة PDF عند عرض المستند {#how-to-specify-pdf-page-when-viewing-document}

عند عرض ملفات PDF في عارض PDF مثل Adobe Reader، عادةً ما تفتح الملفات على الصفحة الأولى. ومع ذلك، من الممكن تعيين الملف ليفتح على صفحة مختلفة.

تسمح لك فئة [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) بتحديد صفحة في ملف PDF تريد فتحها. عند تمرير قيمة كائن GoToAction إلى خاصية OpenAction لفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ، يفتح المستند في الصفحة المحددة ضد كائن XYZExplicitDestination. تظهر مقتطفات الشيفرة التالية كيفية تحديد صفحة كإجراء فتح المستند.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
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