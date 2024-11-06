---
title: تعيين خصائص عناصر الهيكل
linktitle: تعيين خصائص عناصر الهيكل
type: docs
weight: 30
url: ar/net/setting-structure-elements-properties/
description: يمكنك تعيين خصائص عناصر الهيكل المختلفة في مستند PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعيين خصائص عناصر الهيكل",
    "alternativeHeadline": "كيفية تعيين خصائص العناصر الهيكلية",
    "author": {
        "@type": "Person",
        "name":"أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, تعيين هيكل النص, تعيين اللغة, تعيين العنوان, تعيين عنصر هيكل الملاحظة",
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
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك تعيين خصائص عناصر الهيكل المختلفة في مستند PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
لتعيين خصائص عناصر الهيكل في مستند PDF الموسوم، يقدم Aspose.PDF الطرق [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) و [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) لواجهة [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

يظهر الجزء التالي من الكود كيفية تعيين خصائص عناصر الهيكل لمستند PDF موسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("مستند PDF موسوم");
taggedContent.SetLanguage("en-US");

// إنشاء عناصر الهيكل
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("العنوان");

h1.Title = "العنوان";
h1.Language = "en-US";
h1.AlternativeText = "نص بديل";
h1.ExpansionText = "نص التوسعة";
h1.ActualText = "النص الفعلي";

// حفظ مستند PDF الموسوم
document.Save(dataDir + "StructureElementsProperties.pdf");
```
changefreq: "monthly"
type: docs
## تحديد عناصر هيكلية للنص

لتحديد عناصر هيكلية للنص في مستند PDF موسوم، يقدم Aspose.PDF فئة [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). يظهر شفرة البرمجة التالية كيفية تحديد عناصر هيكلية للنص في مستند PDF موسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على محتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("مستند PDF موسوم");
taggedContent.SetLanguage("en-US");

// الحصول على عناصر الهيكل الجذرية
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// تعيين النص إلى عنصر هيكل النص
p.SetText("فقرة.");
rootElement.AppendChild(p);


// حفظ مستند PDF الموسوم
document.Save(dataDir + "TextStructureElement.pdf");
```
## تحديد عناصر هيكل كتلة النص

لتعيين عناصر هيكل كتلة النص في مستند PDF الموسوم، يوفر Aspose.PDF فئات [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) و [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement) . يمكنك إلحاق أشياء من هذه الفئات كطفل لكائن [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
يظهر الشفرة التالية كيفية تعيين عناصر هيكل كتلة النص في مستند PDF الموسوم:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// الطريق إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("مستند PDF الموسوم");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر الهيكل الجذري
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. رأس من المستوى 1");
h2.SetText("H2. رأس من المستوى 2");
h3.SetText("H3. رأس من المستوى 3");
h4.SetText("H4. رأس من المستوى 4");
h5.SetText("H5. رأس من المستوى 5");
h6.SetText("H6. رأس من المستوى 6");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. لوريم إيبسوم دولور سيت أميت، كونسكتيتور أديبيسكينغ إيليت. أنيان نيك لكتوس أك سيم فوسيبوس إمبيرديت. سيد أوت إيرات أك ماغنا أولامكوربر هندريريت. كراس بيلينتيسكو ليبيرو سيمبر، غرافيدا ماغنا سيد، لوكتوس ليو. فوسي لكتوس أوديو، لاوريت نيك أولامكوربر أوت، موليستي إيو إيليت. إنتردوم إت ماليسوادا فاميس أك أنتي إيبسوم بريميس إن فوسيبوس. أليكوام لاسينيا سيت أميت إيليت أك كونسكتيتور. دونيك كورسوس كونديمنتوم ليغولا، فيتاي فولوتبات سيم تريستيكي إيجيت. نولا إن كونسكتيتور ماسا. فيستيبولوم فيتاي لوبورتيس أنتي. نولا أولامكوربر بيلينتيسكو جوستو رونكوس أكومسان. ماوريس أورناري إيو أوديو نون لاسينيا. أليكوام ماسا ليو، رونكوس أك إياسيوليس إيجيت، تيمبوس إيت ماغنا. سيد نون كونسكتيتور إيليت. سيد فولوتبات، كوام سيد لاسينيا لوكتوس، إيبسوم نيبه فرينجيلا بوروس، فيتاي بوسويري ريسوس أوديو إيد ماسا. كراس سيد فينيناتيس لاكوس.");
rootElement.AppendChild(p);

// حفظ مستند PDF الموسوم
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## تعيين عناصر البنية المضمنة

لتعيين عناصر البنية المضمنة لمستند PDF الموسوم، تقدم Aspose.PDF فئات [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) و[ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). يمكنك إلحاق كائنات من هذه الفئات كطفل لكائن [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). يوضح الجزء التالي من الشفرة كيفية تعيين عناصر البنية المضمنة لمستند PDF الموسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر البنية الجذر
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("عنوان المستوى 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("عنوان المستوى 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("عنوان المستوى 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("عنوان المستوى 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("عنوان المستوى 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("عنوان المستوى 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// حفظ مستند PDF الموسوم
document.Save(dataDir + "InlineStructureElements.pdf");
```
## تعيين اسم علامة مخصصة

لتعيين اسم علامة مخصص لعناصر مستند PDF الموسوم، يقدم Aspose.PDF طريقة [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) لفئة StructureElement للعناصر. يوضح مقتطف الكود التالي كيفية تعيين اسم علامة مخصص:

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// إنشاء عناصر البنية المنطقية
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// حفظ مستند Pdf الموسوم
document.Save(dataDir + "CustomTag.pdf");
```
## إضافة عنصر هيكلي إلى العناصر

**هذه الميزة مدعومة بواسطة الإصدار 19.4 أو أعلى.**

لتعيين عناصر الهيكل في مستند PDF موسوم، يقدم Aspose.PDF طريقة [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) لواجهة [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). يوضح الجزء التالي من الكود كيفية تعيين عناصر الهيكل في فقرة مع نص في مستند PDF موسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// إنشاء مستند والحصول على محتوى PDF الموسوم
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// تعيين العنوان واللغة الطبيعية للمستند
taggedContent.SetTitle("مثال عناصر الرابط");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر الهيكل الجذر (عنصر هيكل المستند)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "رابط إلى Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "رابط إلى Google";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "رابط إلى Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("الرابط متعدد الأسطر: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "رابط إلى Google (متعدد الأسطر)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "أيقونة Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "رابط إلى Google";


// حفظ مستند PDF الموسوم
document.Save(outFile);

// التحقق من توافق PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("التوافق مع PDF/UA: {0}", isPdfUaCompliance));
```
## تحديد عنصر هيكل الرابط

**هذه الميزة مدعومة بواسطة الإصدار 19.4 أو أعلى.**

واجهة برمجة التطبيقات Aspose.PDF لـ .NET تتيح لك أيضًا إضافة عناصر هيكل الرابط. يوضح الكود التالي كيفية إضافة عنصر هيكل الرابط إلى مستند PDF الموسوم:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// إنشاء مستند والحصول على محتوى PDF الموسوم
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// تحديد العنوان واللغة الطبيعية للمستند
taggedContent.SetTitle("مثال عناصر النص");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر الهيكل الجذري (عنصر هيكل المستند)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" و Span_12.");
p1.SetText("فقرة مع ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" و ");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" و Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411، ");
span41.SetText("Span_41، ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 و ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// حفظ مستند PDF الموسوم
document.Save(outFile);

// التحقق من الامتثال لـ PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("الامتثال لـ PDF/UA: {0}", isPdfUaCompliance));
```
## تعيين عنصر هيكل ملاحظة

يسمح Aspose.PDF لـ .NET API أيضًا بإضافة [عنصر ملاحظة](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) في مستند PDF الموسوم. يوضح جزء الكود التالي كيفية إضافة عنصر ملاحظة في مستند PDF الموسوم:

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// إنشاء مستند Pdf
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("عينة من عناصر الملاحظة");
taggedContent.SetLanguage("en-US");

// إضافة عنصر فقرة
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// إضافة عنصر ملاحظة
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("ملاحظة بمعرف توليد تلقائي. ");

// إضافة عنصر ملاحظة
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("ملاحظة بمعرف = 'note_002'. ");
note2.SetId("note_002");

// إضافة عنصر ملاحظة
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("ملاحظة بمعرف = 'note_003'. ");
note3.SetId("note_003");

// يجب أن يطرح استثناء - Aspose.Pdf.Tagged.TaggedException : عنصر الهيكل بمعرف='note_002' موجود بالفعل
//note3.SetId("note_002");

// الوثيقة الناتجة لا تتوافق مع PDF/UA إذا تم استخدام ClearId() لعنصر هيكل الملاحظة
//note3.ClearId();


// حفظ مستند PDF الموسوم
document.Save(outFile);

// التحقق من التوافق مع PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("التوافق مع PDF/UA: {0}", isPdfUaCompliance));
```
## تعيين اللغة والعنوان

**هذه الميزة مدعومة بواسطة الإصدار 19.6 أو أعلى.**

يتيح لك واجهة برمجة تطبيقات Aspose.PDF لـ .NET أيضًا تعيين اللغة والعنوان للمستند وفقًا لمواصفات PDF/UA. يمكن تعيين اللغة للمستند بأكمله أو لعناصره الهيكلية المنفصلة. يوضح الجزء التالي من الكود كيفية تعيين اللغة والعنوان في مستند PDF الموسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// احصل على TaggedContent
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة
taggedContent.SetTitle("مستند موسوم كمثال");
taggedContent.SetLanguage("en-US");

// العنوان (en-US، موروث من المستند)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("عبارة بلغات مختلفة");
taggedContent.RootElement.AppendChild(h1);

// فقرة (إنجليزي)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("مرحباً بالعالم!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// فقرة (ألماني)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// فقرة (فرنسي)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// فقرة (إسباني)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// حفظ مستند PDF الموسوم
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينوكس",
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

