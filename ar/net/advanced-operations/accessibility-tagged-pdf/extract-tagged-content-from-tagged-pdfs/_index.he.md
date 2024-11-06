---
title: חלץ תוכן עם תגיות ממסמך PDF
linktitle: חלץ תוכן עם תגיות
type: docs
weight: 20
url: ar/net/extract-tagged-content-from-tagged-pdfs/
description: מאמר זה מסביר כיצד לחלץ תוכן עם תגיות ממסמך PDF באמצעות Aspose.PDF for .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חלץ תוכן עם תגיות ממסמך PDF",
    "alternativeHeadline": "איך לתייג תמונה ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "תג, pdf, חילוץ",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכי Aspose.PDF",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר כיצד לחלץ תוכן עם תגיות ממסמך PDF באמצעות Aspose.PDF for .NET"
}
</script>
במאמר זה תלמדו כיצד לחלץ תוכן מתויג ממסמך PDF באמצעות C#.

הקטע הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## קבלת תוכן PDF מתויג

על מנת לקבל תוכן של מסמך PDF עם טקסט מתויג, Aspose.PDF מציעה את התכונה [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) של הכיתה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

הקטע קוד הבא מראה כיצד לקבל תוכן של מסמך PDF עם טקסט מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך Pdf
Document document = new Document();

// קבלת תוכן לעבודה עם TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// עבודה עם תוכן PDF מתויג
//

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// שמירת מסמך PDF מתויג
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## קבלת מבנה שורש

כדי לקבל את מבנה השורש של מסמך PDF מתויג, Aspose.PDF מציע את התכונה [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) של ממשק [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) ו-[StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). הקטע קוד הבא מראה איך לקבל את מבנה השורש של מסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך PDF
Document document = new Document();

// קבלת תוכן לעבודה עם TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// התכונות StructTreeRootElement ו-RootElement משמשות לגישה ל
// אובייקט StructTreeRoot של מסמך pdf ולאלמנט מבנה שורש (אלמנט מבנה המסמך).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## גישה לאלמנטים צאצא

כדי לגשת לאלמנטים צאצא של מסמך PDF מתויג, Aspose.PDF מציעה את הכיתה [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist). קטע הקוד הבא מראה כיצד לגשת לאלמנטים צאצא של מסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתיחת מסמך PDF
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// קבלת תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// גישה לאלמנט(ים) שורש
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // קבלת מאפיינים
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// גישה לאלמנטים צאצא של האלמנט הראשון באלמנט שורש
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // הגדרת מאפיינים
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// שמירת מסמך PDF מתויג
document.Save(dataDir + "AccessChildElements.pdf");
```
## תיוג תמונות במסמך PDF קיים

כדי לתייג תמונות במסמך PDF קיים, Aspose.PDF מציעה את שיטת [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) של מחלקת [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). ניתן להוסיף טקסט חלופי לדמויות באמצעות תכונת [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) של מחלקת [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement).

הדוגמה הבאה מראה כיצד לתייג תמונות במסמך PDF קיים:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// פתח מסמך
Document document = new Document(inFile);

// מקבל תוכן מתויג ואלמנט מבנה שורש
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// הגדר כותרת למסמך PDF מתויג
taggedContent.SetTitle("מסמך עם תמונות");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // הגדר טקסט חלופי לדמות
    figureElement.AlternativeText = "טקסט חלופי לדמות (טכניקה 2)";


    // צור והגדר את תכונת BBox
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// הזז אלמנט Span לתוך פסקה (מצא span ופסקה שגויים ב-TD הראשון)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// הזז אלמנט Span לתוך פסקה
spanElement.ChangeParentElement(paragraph);


// שמור מסמך
document.Save(outFile);



// בדיקת תאימות PDF/UA למסמך החדש
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("תאימות PDF/UA: {0}", isPdfUaCompliance));
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

