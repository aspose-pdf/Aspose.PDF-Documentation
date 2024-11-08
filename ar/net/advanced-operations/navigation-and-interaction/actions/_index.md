---
title: العمل مع الأفعال في ملف PDF
linktitle: الأفعال
type: docs
weight: 20
url: /ar/net/actions/
description: هذا القسم يشرح كيفية إضافة أفعال إلى المستند وحقول النموذج برمجياً باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع الأفعال في ملف PDF",
    "alternativeHeadline": "كيفية إضافة الأفعال في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أندري أندروخوفسكي",
        "givenName": "أندري",
        "familyName": "أندروخوفسكي",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, actions in pdf",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "dateModified": "2022-02-04",
    "description": "هذا القسم يشرح كيفية إضافة أفعال إلى المستند وحقول النموذج برمجياً باستخدام C#."
}
</script>
يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة رابط تشعبي في ملف PDF

من الممكن إضافة روابط تشعبية إلى ملفات PDF، إما للسماح للقراء بالانتقال إلى جزء آخر من الـ PDF، أو إلى محتوى خارجي.

لإضافة روابط ويب تشعبية إلى مستندات PDF:

1. إنشاء كائن الفصل [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. الحصول على فصل [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) الذي تريد إضافة الرابط إليه.
1. إنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) باستخدام الفصل Page وكائنات [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). يُستخدم كائن المستطيل لتحديد الموقع على الصفحة الذي يجب إضافة الرابط فيه.
1. تعيين خاصية الفعل إلى كائن [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) الذي يحدد موقع الـ URI البعيد. 
1. 
1.
1. لإضافة نص حر:
   
   - قم بإنشاء كائن [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). يقبل أيضًا كائنات الصفحة والمستطيل كوسيطات، لذا من الممكن تقديم نفس القيم المحددة لبناء جملة مُنشئ LinkAnnotation.
   - باستخدام خاصية Contents لكائن [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)، حدد النص الذي يجب أن يظهر في ملف PDF الناتج.
   - اختياريًا، قم بضبط عرض الحد لكل من كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) وFreeTextAnnotation إلى 0 بحيث لا يظهران في مستند PDF.
   - بمجرد تعريف كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) و [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)، أضف هذه الروابط إلى مجموعة Annotations لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- بمجرد تعريف كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) و [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)، قم بإضافة هذه الروابط إلى مجموعة التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- أخيرًا، احفظ ملف PDF المُحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) الخاصة بكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

يوضح مقتطف الكود التالي كيفية إضافة ارتباط تشعبي إلى ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// فتح المستند
Document document = new Document(dataDir + "AddHyperlink.pdf");
// إنشاء رابط
Page page = document.Pages[1];
// إنشاء كائن تعليق توضيحي للرابط
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// إنشاء كائن حدود لتعليق LinkAnnotation
Border border = new Border(link);
// تحديد قيمة عرض الحدود كـ 0
border.Width = 0;
// تعيين الحدود لتعليق LinkAnnotation
link.Border = border;
// تحديد نوع الرابط كعنوان URI بعيد
link.Action = new GoToURIAction("www.aspose.com");
// إضافة تعليق توضيحي للرابط إلى مجموعة التعليقات التوضيحية للصفحة الأولى من ملف PDF
page.Annotations.Add(link);

// إنشاء تعليق توضيحي للنص الحر
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// النص المراد إضافته كنص حر
textAnnotation.Contents = "Link to Aspose website";
// تعيين الحدود لتعليق النص الحر
textAnnotation.Border = border;
// إضافة تعليق النص الحر إلى مجموعة التعليقات التوضيحية للصفحة الأولى من المستند
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// حفظ المستند المُحدث
document.Save(dataDir);
```
## إنشاء رابط تشعبي للصفحات في نفس ملف PDF

Aspose.PDF لـ .NET يوفر ميزة رائعة لإنشاء ملفات PDF بالإضافة إلى تعديلها. كما يقدم الميزة لإضافة روابط إلى صفحات PDF ويمكن أن يوجه الرابط إلى صفحات في ملف PDF آخر، عنوان URL للويب، رابط لتشغيل تطبيق أو حتى رابط للصفحات في نفس ملف PDF. من أجل إضافة الروابط المحلية (روابط للصفحات في نفس ملف PDF)، تم إضافة فئة تسمى [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) إلى فضاء الاسم Aspose.PDF ولهذه الفئة خاصية تسمى TargetPageNumber، والتي يتم استخدامها لتحديد صفحة الهدف/الوجهة للرابط التشعبي.

من أجل إضافة الرابط المحلي، نحتاج إلى إنشاء TextFragment بحيث يمكن ربط الرابط بـ TextFragment. تحتوي فئة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) على خاصية تسمى Hyperlink والتي تستخدم لربط مثيل LocalHyperlink. يوضح الشفرة التالية الخطوات لتحقيق هذا الشرط.

```csharp
// إنشاء مستند PDF جديد
Document pdfDocument = new Document();

// إضافة صفحة إلى مستند PDF
Page page1 = pdfDocument.Pages.Add();
Page page2 = pdfDocument.Pages.Add();

// إنشاء TextFragment
TextFragment textFragment = new TextFragment("انتقل إلى الصفحة الثانية");
textFragment.Position = new Position(100, 600);

// إنشاء LocalHyperlink
LocalHyperlink localHyperlink = new LocalHyperlink();
localHyperlink.TargetPageNumber = 2;

// ربط الرابط المحلي بـ TextFragment
textFragment.Hyperlink = localHyperlink;

// إضافة TextFragment إلى الصفحة الأولى
page1.Paragraphs.Add(textFragment);

// حفظ المستند
pdfDocument.Save("output.pdf");
```
```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// إنشاء نموذج للمستند
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات ملف PDF
Page page = doc.Pages.Add();
// إنشاء نموذج لجزء نصي
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("اختبار رقم الصفحة الرابط إلى الصفحة 7");
// إنشاء نموذج لرابط محلي
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// تحديد الصفحة المستهدفة لنموذج الرابط
link.TargetPageNumber = 7;
// تعيين الرابط الخاص بجزء النص
text.Hyperlink = link;
// إضافة النص إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(text);
// إنشاء نموذج جديد لجزء نصي
text = new TextFragment("اختبار رقم الصفحة الرابط إلى الصفحة 1");
// يجب إضافة جزء النص على صفحة جديدة
text.IsInNewPage = true;
// إنشاء نموذج آخر لرابط محلي
link = new LocalHyperlink();
// تحديد الصفحة المستهدفة للرابط الثاني
link.TargetPageNumber = 1;
// تعيين الرابط لجزء النص الثاني
text.Hyperlink = link;
// إضافة النص إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// حفظ المستند بعد التحديث
doc.Save(dataDir);
```
## الحصول على وجهة الرابط التشعبي (URL) في ملف PDF

الروابط ممثلة كتعليقات في ملف PDF ويمكن إضافتها أو تحديثها أو حذفها. يدعم Aspose.PDF لـ .NET أيضًا الحصول على وجهة (URL) الرابط التشعبي في ملف PDF.

للحصول على URL للرابط:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. الحصول على [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) الذي تريد استخراج الروابط منه.
1. استخدم فئة [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) لاستخراج كل كائنات [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) من الصفحة المحددة.
1. قم بتمرير كائن [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) إلى طريقة Accept الخاصة بكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. أخيرًا، استخرج إجراء LinkAnnotation كـ GoToURIAction.

الشفرة التالية توضح كيفية الحصول على وجهات الروابط الفائقة (URL) من ملف PDF.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// تحميل ملف PDF
Document document = new Document(dataDir + "input.pdf");

// تصفح جميع صفحات PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // الحصول على تعليقات الروابط من صفحة معينة
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // إنشاء قائمة تحتوي على جميع الروابط
    IList<Annotation> list = selector.Selected;
    // تكرار كل عنصر داخل القائمة
    foreach (LinkAnnotation a in list)
    {
        // طباعة عنوان URL الوجهة
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## الحصول على نص الرابط التشعبي

الرابط التشعبي يتكون من جزأين: النص الذي يظهر في المستند، وعنوان URL الوجهة. في بعض الحالات، النص هو ما نحتاجه بدلاً من العنوان.

النص والتعليقات/الأفعال في ملف PDF يتم تمثيلها بكيانات مختلفة. النص على صفحة هو مجرد مجموعة من الكلمات والأحرف، بينما تجلب التعليقات بعض التفاعلية مثل التي تكون متأصلة في الرابط التشعبي.

لإيجاد محتوى العنوان، تحتاج للعمل مع التعليق والنص. كائن [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) لا يحتوي بحد ذاته على النص ولكن يقع تحت النص في الصفحة. لذا للحصول على النص، يعطي Annotation حدود العنوان، بينما يعطي كائن النص محتويات العنوان. يرجى مشاهدة الشفرة التالية.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // المسار إلى دليل المستندات.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // تحميل ملف PDF
                Document document = new Document(dataDir + "input.pdf");
                // تكرار كل صفحة من PDF
                foreach (Page page in document.Pages)
                {
                    // عرض التعليق التوضيحي للرابط
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // طباعة عنوان URL لكل تعليق توضيحي للرابط
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // طباعة النص المرتبط بالرابط التشعبي
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## إزالة إجراء فتح المستند من ملف PDF

[كيفية تحديد صفحة PDF عند عرض المستند](#how-to-specify-pdf-page-when-viewing-document) شرح كيفية توجيه المستند ليفتح على صفحة مختلفة عن الأولى. عند دمج عدة مستندات، وواحدة أو أكثر بها إجراء GoTo، ربما ترغب في إزالتها. على سبيل المثال، إذا كنت تدمج مستندين والثاني به إجراء GoTo يأخذك إلى الصفحة الثانية، سيفتح المستند الناتج على الصفحة الثانية من الوثيقة الثانية بدلاً من الصفحة الأولى من المستند المدمج. لتجنب هذا السلوك، قم بإزالة أمر إجراء الفتح.

لإزالة إجراء فتح:

1. قم بتعيين خاصية [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) على null.
1. احفظ PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن Document.

يوضح الكود التالي كيفية إزالة إجراء فتح المستند من ملف PDF.
يوضح الشيفرة التالية كيفية إزالة إجراء فتح المستند من ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// فتح المستند
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// إزالة إجراء فتح المستند
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// حفظ المستند المحدث
document.Save(dataDir);
```

## كيفية تحديد صفحة PDF عند عرض المستند {#how-to-specify-pdf-page-when-viewing-document}

عند عرض ملفات PDF في مشاهد PDF مثل Adobe Reader، عادةً ما تفتح الملفات في الصفحة الأولى. ومع ذلك، من الممكن تعيين الملف ليفتح على صفحة مختلفة.

تسمح لك الفئة [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) بتحديد صفحة في ملف PDF تريد فتحها.
فئة [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) تسمح لك بتحديد صفحة في ملف PDF التي تريد فتحها.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// تحميل ملف PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// الحصول على نموذج الصفحة الثانية من المستند
Page page2 = doc.Pages[2];
// إنشاء المتغير لضبط عامل التكبير للصفحة المستهدفة
double zoom = 1;
// إنشاء نموذج GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// الذهاب إلى الصفحة 2
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// تعيين فتح الوثيقة بالفعل
doc.OpenAction = action;
// حفظ الوثيقة بعد التحديث
doc.Save(dataDir + "goto2page_out.pdf");
```

