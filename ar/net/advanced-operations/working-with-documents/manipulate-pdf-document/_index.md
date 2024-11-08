---
title: التعامل مع مستند PDF في C#
linktitle: التعامل مع مستند PDF
type: docs
weight: 20
url: /ar/net/manipulate-pdf-document/
description: يحتوي هذا المقال على معلومات حول كيفية التحقق من صحة مستند PDF لمعيار PDF A، وكيفية العمل مع جدول المحتويات، وكيفية تعيين تاريخ انتهاء صلاحية PDF، وما إلى ذلك.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "التعامل مع مستند PDF",
    "alternativeHeadline": "كيفية التعامل مع ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, dotnet, manipulate pdf file",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "يحتوي هذا المقال على معلومات حول كيفية التحقق من صحة مستند PDF لمعيار PDF A، وكيفية العمل مع جدول المحتويات، وكيفية تعيين تاريخ انتهاء صلاحية PDF، وما إلى ذلك."
}
</script>
## **التعامل مع مستند PDF في C#**

## التحقق من صحة مستند PDF لمعيار PDF A (A 1A و A 1B)

للتحقق من صحة مستند PDF للتوافق مع PDF/A-1a أو PDF/A-1b، استخدم طريقة التحقق Validate في فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). تتيح لك هذه الطريقة تحديد اسم الملف الذي يجب حفظ النتيجة فيه ونوع التحقق المطلوب من تعداد [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat): PDF_A_1A أو PDF_A_1B.

{{% alert color="primary" %}}

تنسيق XML الناتج هو تنسيق مخصص من Aspose. يحتوي XML على مجموعة من العلامات باسم Problem؛ كل علامة تحتوي على تفاصيل مشكلة معينة. تمثل سمة ObjectID في علامة Problem معرف الكائن المتعلق بهذه المشكلة. تمثل سمة Clause القاعدة المقابلة في مواصفات PDF.

{{% /alert %}}

يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يوضح الجزء التالي من الكود كيفية التحقق من صحة مستند PDF لـ PDF/A-1A.
الجزء التالي من الشفرة يوضح لك كيفية التحقق من صحة ملف PDF لمعيار PDF/A-1A.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// التحقق من صحة PDF لمعيار PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

الجزء التالي من الشفرة يوضح لك كيفية التحقق من صحة ملف PDF لمعيار PDF/A-1B.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// التحقق من صحة PDF لمعيار PDF/A-1b
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

يمكن استخدام Aspose.PDF لـ .NET لتحديد ما إذا كان المستند المحمّل صالحًا كملف PDF وكذلك [إذا كان مشفرًا أم لا](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). لتوسيع قدرات فئة المستند، تمت إضافة خاصية تُسمى *IsPdfaCompliant* لتحديد ما إذا كان الملف المدخل مطابقًا لمعيار PDF/A وخاصية تُسمى *PdfaFormat* لتحديد تنسيق PDF/A.

{{% /alert %}}

## العمل مع جدول المحتويات

### إضافة جدول المحتويات إلى PDF موجود

تتيح واجهة برمجة التطبيقات Aspose.PDF إمكانية إضافة جدول المحتويات إما عند إنشاء PDF، أو إلى ملف موجود. تسمح فئة ListSection في الفضاء الاسمي Aspose.Pdf.Generator بإنشاء جدول المحتويات عند إنشاء PDF من البداية. لإضافة العناوين، والتي تعتبر عناصر في جدول المحتويات، استخدم فئة Aspose.Pdf.Generator.Heading.

لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم فئة Heading في الفضاء الاسمي Aspose.Pdf.
لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم فئة Heading في فضاء الأسماء Aspose.Pdf.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// تحميل ملف PDF موجود
Document doc = new Document(dataDir + "AddTOC.pdf");

// الوصول إلى الصفحة الأولى من ملف PDF
Page tocPage = doc.Pages.Insert(1);

// إنشاء كائن لتمثيل معلومات جدول المحتويات
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("جدول المحتويات");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// تعيين العنوان لجدول المحتويات
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// إنشاء كائنات string التي ستستخدم كعناصر في جدول المحتويات
string[] titles = new string[4];
titles[0] = "الصفحة الأولى";
titles[1] = "الصفحة الثانية";
titles[2] = "الصفحة الثالثة";
titles[3] = "الصفحة الرابعة";
for (int i = 0; i < 2; i++)
{
    // إنشاء كائن Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // تحديد الصفحة المقصودة لكائن العنوان
    heading2.DestinationPage = doc.Pages[i + 2];

    // الصفحة المقصودة
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // الإحداثي المقصود
    segment2.Text = titles[i];

    // إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// حفظ المستند المحدث
doc.Save(dataDir);
```
### تعيين أنواع مختلفة لـ TabLeaderType لمستويات TOC المختلفة

يسمح Aspose.PDF أيضًا بتعيين أنواع مختلفة لـ TabLeaderType لمستويات TOC المختلفة. تحتاج إلى تعيين خاصية LineDash لـ FormatArray بالقيمة المناسبة من تعداد TabLeaderType كما يلي.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//تعيين LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("جدول المحتويات");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
tocPage.TocInfo = tocInfo;
//تحديد تنسيق القوائم ذات الأربع مستويات بضبط الهوامش اليسرى
//و
//إعدادات تنسيق النص لكل مستوى

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//إنشاء قسم في مستند Pdf
Page page = doc.Pages.Add();

//إضافة أربع عناوين في القسم
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "عنوان نموذجي" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //إضافة العنوان إلى جدول المحتويات.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// حفظ ملف Pdf

doc.Save(outFile);
```
### إخفاء أرقام الصفحات في جدول المحتويات

في حالة عدم رغبتك في عرض أرقام الصفحات، بالإضافة إلى العناوين في جدول المحتويات، يمكنك استخدام خاصية [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) للفئة [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) على أنها false. يرجى مراجعة الشفرة التالية لإخفاء أرقام الصفحات في جدول المحتويات:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("جدول المحتويات");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//أضف قسم القائمة إلى مجموعة أقسام المستند PDF
tocPage.TocInfo = tocInfo;
//حدد تنسيق الأربع مستويات للقائمة بضبط الهوامش اليسرى و
//إعدادات تنسيق النص لكل مستوى

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//أضف أربعة عناوين في القسم
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "هذا عنوان المستوى " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### تخصيص أرقام الصفحات أثناء إضافة فهرس المحتويات

من الشائع تخصيص ترقيم الصفحات في فهرس المحتويات عند إضافة فهرس المحتويات في مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بعض البادئات قبل رقم الصفحة مثل P1، P2، P3 وهكذا. في مثل هذه الحالة، يوفر Aspose.PDF لـ .NET خاصية PageNumbersPrefix لفئة TocInfo والتي يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في مثال الكود التالي.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// تحميل ملف PDF موجود
Document doc = new Document(inFile);
// الوصول إلى أول صفحة من ملف PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// إنشاء كائن لتمثيل معلومات فهرس المحتويات
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("فهرس المحتويات");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// تعيين العنوان لفهرس المحتويات
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // إنشاء كائن العنوان
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // تحديد الصفحة المقصودة للكائن العنوان
    heading2.DestinationPage = doc.Pages[i + 1];
    // الصفحة المقصودة
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // الإحداثي المقصود
    segment2.Text = "الصفحة " + i.ToString();
    // إضافة العنوان إلى الصفحة التي تحتوي على فهرس المحتويات
    tocPage.Paragraphs.Add(heading2);
}

// حفظ المستند بعد التحديث
doc.Save(outFile);
```
## كيفية تعيين تاريخ انتهاء صلاحية PDF

نحن نطبق امتيازات الوصول على ملفات PDF بحيث يمكن لمجموعة معينة من المستخدمين الوصول إلى ميزات/عناصر معينة في مستندات PDF. من أجل تقييد الوصول إلى ملف PDF، عادة ما نطبق التشفير وقد يكون لدينا متطلب لتعيين انتهاء صلاحية ملف PDF، بحيث يحصل المستخدم الذي يقوم بالوصول/الاطلاع على المستند على إشعار صالح بخصوص انتهاء صلاحية ملف PDF.

لتحقيق المتطلب المذكور أعلاه، يمكننا استخدام كائن *JavascriptAction*. الرجاء الاطلاع على الشفرة التالية.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// توثيق كائن Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// إضافة صفحة إلى مجموعة صفحات ملف PDF
doc.Pages.Add();
// إضافة جزء نصي إلى مجموعة فقرات كائن الصفحة
doc.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// إنشاء كائن JavaScript لتعيين تاريخ انتهاء صلاحية PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('The file is expired. You need a new one.');");
// تعيين JavaScript كفعل فتح PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// حفظ مستند PDF
doc.Save(dataDir);
```
## تحديد تقدم إنشاء ملف PDF

طلب أحد العملاء إضافة ميزة تسمح للمطورين بتحديد تقدم إنشاء ملف PDF. إليكم الرد على هذا الطلب.

يسمح لك الحقل [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) من فئة [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) بتحديد كيفية سير إنشاء PDF. يحتوي المعالج على الأنواع التالية:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

الأكواد أدناه تُظهر كيفية استخدام CustomerProgressHandler.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - تقدم التحويل : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - تم تحليل الصفحة المصدر {1} من {2}.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - تم إنشاء تخطيط الصفحة النتيجة {1} من {2}.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - تم تصدير الصفحة النتيجة {1} من {2}.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## تسطيح ملف PDF القابل للتعبئة في C#

غالبًا ما تتضمن مستندات PDF نماذج بعناصر تفاعلية قابلة للتعبئة مثل أزرار الاختيار وخانات الاختيار وصناديق النصوص والقوائم، إلخ. لجعله غير قابل للتحرير لأغراض تطبيقية متنوعة، نحتاج إلى تسطيح ملف PDF.
يوفر Aspose.PDF الوظيفة لتسطيح PDF في C# ببضع أسطر من الكود فقط:

```csharp

// تحميل نموذج PDF المصدر
Document doc = new Document(dataDir + "input.pdf");

// تسطيح ملف PDF القابل للتعبئة 
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// حفظ المستند بعد التحديث
doc.Save(dataDir);
```

