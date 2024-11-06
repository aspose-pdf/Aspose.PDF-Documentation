---
title: استخدام التعليقات التوضيحية للنص في ملف PDF
linktitle: التعليقات التوضيحية للنص
type: docs
weight: 10
url: ar/net/text-annotation/
description: يتيح لك Aspose.PDF لـ .NET إضافة، والحصول على، وحذف التعليقات التوضيحية للنص من مستند PDF الخاص بك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخدام التعليقات التوضيحية للنص في ملف PDF",
    "alternativeHeadline": "كيفية إضافة التعليقات التوضيحية للنص في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, التعليقات التوضيحية للنص",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "يتيح لك Aspose.PDF لـ .NET إضافة، والحصول على، وحذف التعليقات التوضيحية للنص من مستند PDF الخاص بك."
}
</script>
## كيفية إضافة تعليق نصي إلى ملف PDF موجود

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

التعليق النصي هو تعليق مرتبط بموقع محدد في مستند PDF. عند إغلاق التعليق، يظهر كأيقونة؛ عند فتحه، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم الذي يختاره القارئ.

التعليقات محتواة بواسطة مجموعة [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) لصفحة معينة. تحتوي هذه المجموعة على التعليقات لتلك الصفحة فقط؛ كل صفحة لها مجموعة Annotations الخاصة بها.

لإضافة تعليق إلى صفحة معينة، أضفه إلى مجموعة Annotations الخاصة بتلك الصفحة باستخدام طريقة [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. أولاً، قم بإنشاء تعليق تريد إضافته إلى ملف PDF.
1. ثم افتح ملف PDF الذي تريد التعديل عليه.
1.

الشفرة التالية توضح لك كيفية إضافة تعليق توضيحي في صفحة PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// إنشاء التعليق التوضيحي
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "عنوان التعليق التوضيحي";
textAnnotation.Subject = "موضوع العينة";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "محتويات العينة للتعليق التوضيحي";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// إضافة التعليق التوضيحي في مجموعة التعليقات التوضيحية للصفحة
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// حفظ الملف الناتج
pdfDocument.Save(dataDir);
```
## كيفية إضافة تعليق توضيحي منبثق

يعرض التعليق التوضيحي المنبثق النص في نافذة منبثقة للإدخال والتحرير. لا يجب أن يظهر بمفرده بل يرتبط بتعليق توضيحي للعلامات، وهو التعليق التوضيحي الأم، ويجب استخدامه لتحرير نص الأم.

لا يجب أن يكون له تيار ظهور أو أفعال مرتبطة خاصة به ويجب تحديده بواسطة إدخال Popup في قاموس التعليق التوضيحي الأم.

يوضح الكود التالي كيفية إضافة [تعليق توضيحي منبثق](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) في صفحة PDF باستخدام مثال على إضافة [تعليق توضيحي للخط](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) للأم.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // مسار دليل المستندات.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // تحميل ملف PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // إنشاء تعليق توضيحي للخط
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // إضافة التعليق التوضيحي إلى الصفحة
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## كيفية إضافة (أو إنشاء) تعليق نصي حر جديد

يعرض التعليق النصي الحر النص مباشرةً على الصفحة. تسمح طريقة [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) بإنشاء هذا النوع من التعليقات. في الجزء التالي، نضيف تعليقاً نصياً حراً فوق أول ظهور للسلسلة النصية.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### تعيين خاصية الدعوة للتعليق النصي الحر
### تعيين خاصية Callout لـ FreeTextAnnotation

لتكوين أكثر مرونة للتعليق التوضيحي في مستند PDF، يوفر Aspose.PDF لـ.NET خاصية [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) لفئة [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) التي تسمح بتحديد مصفوفة من نقاط خط الإشارة. يوضح الجزء التالي من الكود كيفية استخدام هذه الوظيفة:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### تعيين خاصية Callout لملف XFDF

إذا كنت تستخدم الاستيراد من ملف XFDF، يرجى استخدام اسم خط الإشارة بدلاً من استخدام Callout فقط. يوضح الجزء التالي من الكود كيفية استخدام هذه الوظيفة:

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

الطريقة التالية تستخدم لإنشاء Xfdf:

```csharp
/// <summary>
/// إنشاء XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">هذا مثال</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### اجعل التعليق التوضيحي للنص الحر غير مرئي

في بعض الأحيان، قد يكون من الضروري إنشاء علامة مائية غير مرئية في الوثيقة عند عرضها ولكن يجب أن تكون مرئية عند طباعة الوثيقة. استخدم علامات التعليق التوضيحي لهذا الغرض. يوضح الجزء التالي من الكود كيفية ذلك.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح الوثيقة
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// حفظ الملف الناتج
doc.Save(dataDir);
```
### تنسيق FreeTextAnnotation

هذا الجزء ينظر في كيفية تنسيق النص في تعليق نصي حر.

التعليقات موجودة في مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). عند إضافة [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) إلى مستند PDF، يمكنك تحديد معلومات التنسيق مثل الخط، الحجم، اللون وغيرها باستخدام فئة [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). من الممكن أيضًا تحديد معلومات التنسيق باستخدام خاصية TextStyle. علاوة على ذلك، يمكنك تحديث تنسيق أي FreeTextAnnotation موجود بالفعل في مستند PDF.

تدعم فئة [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) العمل مع مدخل النمط الافتراضي.
الفئة [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) تدعم العمل مع إدخال النمط الافتراضي.

- خاصية FontName تحصل أو تضبط اسم الخط (نص).
- خاصية FontSize تحصل وتضبط حجم النص الافتراضي (مضاعف).
- خاصية System.Drawing.Color تحصل وتضبط لون النص (لون).
- خاصية TextAlignment تحصل وتضبط محاذاة نص الشارة (محاذاة).

الشفرة التالية تظهر كيفية إضافة شارة نص حر مع تنسيق نص محدد.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

عندما تغير محتويات أو نمط نص شارة نص حر، يتم إعادة توليد مظهر الشارة ليعكس التغييرات.

{{% /alert %}}

### شطب الكلمات باستخدام StrikeOutAnnotation

Aspose.PDF لـ .NET يتيح لك إضافة، حذف وتحديث الشارات في مستندات PDF.
Aspose.PDF لـ .NET يتيح لك إضافة، حذف وتحديث التعليقات التوضيحية في مستندات PDF.

لشطب نص معين:

1. ابحث عن TextFragment في ملف PDF.
1. احصل على إحداثيات كائن TextFragment.
1. استخدم الإحداثيات لإنشاء كائن StrikeOutAnnotation.

يوضح الجزء التالي من الكود كيفية البحث عن TextFragment معين وإضافة StrikeOutAnnotation لذلك الكائن.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

هذه الميزة مدعومة بالإصدار 19.6 أو أعلى.

{{% /alert %}}

## حذف جميع التعليقات التوضيحية من صفحة ملف PDF

مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) تحتوي على جميع التعليقات التوضيحية لتلك الصفحة بالذات.
يحتوي مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) على جميع التعليقات التوضيحية لتلك الصفحة المحددة.

يوضح مقتطف الكود التالي كيفية حذف جميع التعليقات التوضيحية من صفحة معينة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// حذف التعليق التوضيحي المحدد
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

## حذف تعليق توضيحي معين من ملف PDF

{{% alert color="primary" %}}

يمكنك التحقق من جودة Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا الرابط:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF يتيح لك إزالة تعليق توضيحي معين من ملف PDF. يشرح هذا الموضوع كيفية القيام بذلك.

لحذف تعليق توضيحي معين من PDF، قم بالاتصال بطريقة الحذف في [مجموعة AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)، والتي تنتمي إلى كائن [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page). تتطلب طريقة الحذف مؤشر التعليق التوضيحي الذي تريد حذفه. ثم، احفظ ملف PDF المُحدث. يوضح الجزء التالي من الكود كيفية حذف تعليق توضيحي معين.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// حذف تعليق توضيحي معين
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// حفظ المستند المُحدث
pdfDocument.Save(dataDir);
```
## الحصول على جميع التعليقات التوضيحية من صفحة في مستند PDF

يتيح لك Aspose.PDF الحصول على التعليقات التوضيحية من مستند بأكمله، أو من صفحة معينة. للحصول على جميع التعليقات التوضيحية من صفحة في مستند PDF، قم بالتكرار عبر مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لموارد الصفحة المطلوبة. يوضح الجزء التالي من الشفرة كيفية الحصول على جميع التعليقات التوضيحية لصفحة.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار لدليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// التكرار عبر جميع التعليقات التوضيحية
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // الحصول على خصائص التعليق التوضيحي
    Console.WriteLine("Title : {0} ", annotation.Title);
    Console.WriteLine("Subject : {0} ", annotation.Subject);
    Console.WriteLine("Contents : {0} ", annotation.Contents);
}
```
يرجى ملاحظة أنه للحصول على جميع التعليقات التوضيحية من ملف PDF بأكمله، يجب عليك التكرار عبر مجموعة فئة PageCollection للمستند قبل التنقل عبر مجموعة فئة AnnotationCollection. يمكنك الحصول على كل تعليق توضيحي في المجموعة في نوع أساسي من التعليقات التوضيحية يسمى فئة MarkupAnnotation ثم عرض خصائصها.

## الحصول على تعليق توضيحي معين من ملف PDF

التعليقات التوضيحية مرتبطة بصفحات فردية ومخزنة في مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
التعليقات التوضيحية مرتبطة بصفحات فردية ومخزنة في مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) الخاصة بكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// الحصول على تعليق توضيحي محدد
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// الحصول على خصائص التعليق التوضيحي
Console.WriteLine("العنوان : {0} ", textAnnotation.Title);
Console.WriteLine("الموضوع : {0} ", textAnnotation.Subject);
Console.WriteLine("المحتويات : {0} ", textAnnotation.Contents);
```

## الحصول على مورد التعليق التوضيحي

يتيح لك Aspose.PDF الحصول على مورد التعليق التوضيحي من مستند كامل، أو من صفحة معينة.
Aspose.PDF يتيح لك الحصول على مورد التعليق التوضيحي من مستند بأكمله، أو من صفحة معينة.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document doc = new Document(dataDir + "AddAnnotation.pdf");
//إنشاء التعليق التوضيحي
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// حفظ المستند
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// فتح المستند
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

//الحصول على إجراء التعليق التوضيحي
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

//الحصول على العرض من إجراء العرض
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

//مقطع الوسائط
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
//بيانات الوسائط متاحة في FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

