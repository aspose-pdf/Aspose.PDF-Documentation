---
title: עבודה עם טפסי XFA
linktitle: טפסי XFA
type: docs
weight: 20
url: /net/xfa-forms/
description: ממשק Aspose.PDF עבור .NET מאפשר לך לעבוד עם שדות XFA ו-XFA Acroform במסמך PDF. הממשק Aspose.PDF.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם טפסי XFA",
    "alternativeHeadline": "מילוי, המרה וקבלת טפסי XFA ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, מילוי טופס xfa, קבלת טופס xfa, המרת טופס xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "ממשק Aspose.PDF עבור .NET מאפשר לך לעבוד עם שדות XFA ו-XFA Acroform במסמך PDF. הממשק Aspose.PDF.Facades."
}
</script>

{{% alert color="primary" %}}

טפסים דינמיים מבוססים על מפרט XML הידוע בשם XFA, "ארכיטקטורת טפסים ב-XML". הוא יכול גם להמיר טופס XFA דינמי ל-Acroform סטנדרטי. המידע על הטופס (ככל שנוגע ל-PDF) הוא מאוד מעורפל – הוא מציין שקיימים שדות, עם מאפיינים ואירועי JavaScript, אך לא מציין כל עיבוד. אובייקטים של טופס XFA נשרטטים בעת טעינת המסמך.

{{% /alert %}}

מחלקת Form מספקת את היכולת לעבוד עם AcroForm סטטי וניתן לקבל מופע של שדה מסוים באמצעות שיטת GetFieldFacade(..) של מחלקת Form. עם זאת, לא ניתן לגשת לשדות XFA באמצעות שיטת Form.GetFieldFacade(..). במקום זאת, השתמש ב- [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) כדי לקבל/להגדיר ערכי שדות ולנהל תבנית שדה XFA (להגדיר מאפייני שדה).

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## מילוי שדות XFA

הקטע קוד הבא מראה לך איך למלא שדות בטופס XFA.
הקטע הבא מראה לך איך למלא שדות בטופס XFA.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טען טופס XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// קבל שמות של שדות טופס XFA
string[] names = doc.Form.XFA.FieldNames;

// הגדר ערכים לשדות
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
```

## המרת XFA ל-Acroform

{{% alert color="primary" %}}

נסה באופן מקוון
תוכל לבדוק את איכות המרה של Aspose.PDF ולראות את התוצאות באופן מקוון בקישור הזה: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

טפסים דינמיים מבוססים על מפרט XML הידוע כ-XFA, ה"ארכיטקטורת טפסים XML".
טפסים דינמיים מבוססים על מפרט XML הידוע בשם XFA, "ארכיטקטורת טפסי XML".

כיום, PDF תומך בשתי שיטות שונות לשילוב נתונים וטפסי PDF:

- AcroForms (ידוע גם כטפסי Acrobat), הוצג וכלול במפרט פורמט PDF 1.2.
- טפסי ארכיטקטורת טפסי XML של Adobe (XFA), הוצגו במפרט פורמט PDF 1.5 כתכונה אופציונלית (מפרט XFA אינו כלול במפרט PDF, הוא רק מתייחס אליו.)

איננו יכולים לחלץ או לשנות דפים של טפסי XFA, מכיוון שתוכן הטופס נוצר בזמן ריצה (במהלך צפייה בטופס XFA) בתוך היישום המנסה להציג או לעבד את הטופס XFA. ל-Aspose.PDF יש תכונה שמאפשרת למפתחים להמיר טפסי XFA לטפסי AcroForms סטנדרטיים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טען טופס XFA דינמי
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// הגדר את סוג שדות הטופס כ-AcroForm סטנדרטי
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// שמור את ה-PDF המתקבל
document.Save(dataDir);
```
## קבל תכונות שדה XFA

כדי לגשת לתכונות שדה, תשתמש תחילה ב-Document.Form.XFA.Teamplate כדי לגשת לתבנית השדה. קטע הקוד הבא מציג את שלבי קבלת קואורדינטות X ו-Y של שדה טופס XFA.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טען טופס XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// הגדר ערכי שדה
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";

// קבל מיקום שדה
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// קבל מיקום שדה
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
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

