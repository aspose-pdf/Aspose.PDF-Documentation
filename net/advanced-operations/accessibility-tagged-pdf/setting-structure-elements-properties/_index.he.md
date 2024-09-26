---
title: הגדרת תכונות אלמנטים מבניים
linktitle: הגדרת תכונות אלמנטים מבניים
type: docs
weight: 30
url: /net/setting-structure-elements-properties/
description: תוכל להגדיר תכונות של אלמנטים מבניים שונים במסמך PDF עם Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הגדרת תכונות אלמנטים מבניים",
    "alternativeHeadline": "כיצד להגדיר את תכונות האלמנטים המבניים",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הגדרת מבנה טקסט, הגדרת שפה, הגדרת כותרת, הגדרת אלמנט מבני של הערה",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכים של Aspose.PDF",
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
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
    "description": "תוכל להגדיר תכונות של אלמנטים מבניים שונים במסמך PDF עם Aspose.PDF עבור .NET."
}
</script>
כדי להגדיר תכונות של אלמנטים מובנים במסמך PDF מתויג, Aspose.PDF מציעה את השיטות [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) ו-[CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) של ממשק [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

הדוגמה הבאה מראה כיצד להגדיר תכונות של אלמנטים מובנים במסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// צור מסמך PDF
Document document = new Document();

// קבל תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// הגדר כותרת ושפה למסמך
taggedContent.SetTitle("מסמך PDF מתויג");
taggedContent.SetLanguage("en-US");

// צור אלמנטים מובנים
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("הכותרת");

h1.Title = "כותרת";
h1.Language = "en-US";
h1.AlternativeText = "טקסט חלופי";
h1.ExpansionText = "טקסט הרחבה";
h1.ActualText = "טקסט בפועל";

// שמור את מסמך ה-PDF המתויג
document.Save(dataDir + "StructureElementsProperties.pdf");
```
changefreq: "monthly"
type: docs
## הגדרת אלמנטים של מבנה טקסט

על מנת להגדר אלמנטים של מבנה טקסט במסמך PDF מתויג, Aspose.PDF מציעה את הכיתה [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). הדוגמה הבאה מראה כיצד להגדיר אלמנטים של מבנה טקסט במסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך PDF
Document document = new Document();

// קבלת תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// קבלת אלמנטים של מבנה השורש
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// הגדרת טקסט לאלמנט מבנה טקסט
p.SetText("Paragraph.");
rootElement.AppendChild(p);


// שמירת מסמך PDF מתויג
document.Save(dataDir + "TextStructureElement.pdf");
```
## הגדרת אלמנטים של מבנה בלוק טקסט

כדי להגדיר אלמנטים של מבנה בלוק טקסט של מסמך PDF מתויג, Aspose.PDF מציעה את המחלקות [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) ו-[ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). ניתן להוסיף אובייקטים מסוג אלו כילדים של אובייקט [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
הדוגמה הבאה מראה כיצד להגדיר אלמנטים של מבנה בלוק טקסט של מסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך PDF
Document document = new Document();

// קבלת תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// קבלת אלמנט המבנה הראשי
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. כותרת רמה 1");
h2.SetText("H2. כותרת רמה 2");
h3.SetText("H3. כותרת רמה 3");
h4.SetText("H4. כותרת רמה 4");
h5.SetText("H5. כותרת רמה 5");
h6.SetText("H6. כותרת רמה 6");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// שמירת מסמך PDF מתויג
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## הגדרת אלמנטים מובנים בשורה

כדי להגדיר אלמנטים מובנים בשורה של מסמך PDF מתויג, Aspose.PDF מציע את המחלקות [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) ו-[ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). ניתן להוסיף אובייקטים ממחלקות אלו כילד לאובייקט [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). קטע הקוד הבא מראה כיצד להגדיר אלמנטים מובנים בשורה של מסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// צור מסמך PDF
Document document = new Document();

// קבל תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// הגדר כותרת ושפה למסמך
taggedContent.SetTitle("מסמך PDF מתויג");
taggedContent.SetLanguage("en-US");

// קבל את אלמנט המבנה הראשי
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
spanH12.SetText("כותרת רמה 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("כותרת רמה 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("כותרת רמה 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("כותרת רמה 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("כותרת רמה 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("כותרת רמה 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("פ. ");
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

// שמור את מסמך ה-PDF המתויג
document.Save(dataDir + "InlineStructureElements.pdf");
```
## הגדרת שם תג מותאם אישית

כדי להגדיר שם תג מותאם אישית של אלמנטים במסמך PDF מתויג, Aspose.PDF מציעה את השיטה [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) של מחלקת StructureElement לאלמנטים. קטע הקוד הבא מראה כיצד להגדיר שם תג מותאם אישית:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// צור מסמך PDF
Document document = new Document();

// קבל תוכן לעבודה עם TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// הגדר כותרת ושפה למסמך
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// צור אלמנטים של מבנה לוגי
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

// שמור מסמך PDF מתויג
document.Save(dataDir + "CustomTag.pdf");
```
## הוספת אלמנט מבנה לתוך אלמנטים

**תכונה זו נתמכת על ידי גרסה 19.4 או גדולה יותר.**

כדי להגדיר אלמנטי מבנה במסמך PDF מתויג, Aspose.PDF מציעה את השיטה [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) של ממשק [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). קטע הקוד הבא מראה כיצד להגדיר אלמנטי מבנה בפסקה עם טקסט של מסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// יצירת מסמך וקבלת תוכן PDF מתויג
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// הגדרת כותרת ושפת טבע למסמך
taggedContent.SetTitle("דוגמא לאלמנטים מקושרים");
taggedContent.SetLanguage("en-US");

// קבלת אלמנט מבנה שורש (אלמנט מבנה של מסמך)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "קישור ל-Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "קישור ל-Google";


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
link3.AlternateDescriptions = "קישור ל-Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("הקישור הרב שורות: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "קישור ל-Google (רב שורות)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "סמל Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "קישור ל-Google";


// שמירת מסמך PDF מתויג
document.Save(outFile);

// בדיקת תאימות PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("תאימות PDF/UA: {0}", isPdfUaCompliance));
```
## הגדרת אלמנט מבנה קישור

**תכונה זו נתמכת בגרסה 19.4 או גדולה יותר.**

‏Aspose.PDF for .NET API מאפשרת גם להוסיף אלמנטי מבנה קישור. קטע הקוד הבא מראה איך להוסיף אלמנט מבנה קישור למסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// יצירת מסמך וקבלת תוכן PDF מתויג
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// הגדרת כותרת ושפת טבע למסמך
taggedContent.SetTitle("דוגמת אלמנטי טקסט");
taggedContent.SetLanguage("en-US");

// קבלת אלמנט המבנה השורש (אלמנט מבנה המסמך)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" ו-Span_12.");
p1.SetText("פסקה עם ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" ו-");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" ו-Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 ו-");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// שמירת מסמך PDF מתויג
document.Save(outFile);

// בדיקת תאימות PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("תאימות PDF/UA: {0}", isPdfUaCompliance));
```
## הגדרת מבנה הערה

‏Aspose.PDF for .NET API מאפשר גם להוסיף [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) במסמך PDF מתויג. קטע הקוד הבא מראה איך להוסיף אלמנט הערה במסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// יצירת מסמך PDF
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("דוגמה לאלמנטי הערה");
taggedContent.SetLanguage("en-US");

// הוספת אלמנט פסקה
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// הוספת NoteElement
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("הערה עם מזהה אוטומטי. ");

// הוספת NoteElement
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("הערה עם מזהה = 'note_002'. ");
note2.SetId("note_002");

// הוספת NoteElement
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("הערה עם מזהה = 'note_003'. ");
note3.SetId("note_003");

// חייב לזרוק יוצאת דופן - Aspose.Pdf.Tagged.TaggedException : אלמנט מבנה עם מזהה='note_002' כבר קיים
//note3.SetId("note_002");

// המסמך המתקבל אינו תואם לPDF/UA אם נעשה שימוש בClearId() עבור אלמנט מבנה הערה
//note3.ClearId();


// שמירת מסמך PDF מתויג
document.Save(outFile);

// בדיקת תאימות PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("תאימות PDF/UA: {0}", isPdfUaCompliance));
```
## הגדרת שפה וכותרת

**תכונה זו נתמכת בגרסה 19.6 ומעלה.**

Aspose.PDF עבור .NET API מאפשר גם להגדיר שפה וכותרת למסמך בהתאם למפרט PDF/UA. ניתן להגדיר שפה גם למסמך כולו וגם לאלמנטים מבניים נפרדים בו. קטע הקוד הבא מראה איך להגדיר שפה וכותרת במסמך PDF מתוייג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// קבלת TaggedContent
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה
taggedContent.SetTitle("Example Tagged Document");
taggedContent.SetLanguage("en-US");

// כותרת (en-US, נגזר מהמסמך)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("Phrase on different languages");
taggedContent.RootElement.AppendChild(h1);

// פסקה (אנגלית)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Hello, World!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// פסקה (גרמנית)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// פסקה (צרפתית)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// פסקה (ספרדית)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// שמירת מסמך PDF מתוייג
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF עבור .NET",
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
                "contactType": "מכירות",
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית עיבוד PDF עבור .NET",
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
```

