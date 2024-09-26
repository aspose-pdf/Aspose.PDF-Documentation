---
title: פרסום נתוני AcroForm
linktitle: פרסום AcroForm
type: docs
weight: 50
url: /net/posting-acroform-data/
description: ניתן לייבא ולייצא נתוני טופס לקובץ XML עם מרחב השמות Aspose.Pdf.Facades ב-Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "פרסום נתוני AcroForm",
    "alternativeHeadline": "יבוא ויצוא נתוני טופס לקובץ XML",
    "author": {
        "@type": "Person",
        "name": "אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, פרסום נתוני acroform",
    "wordcount": "302",
    "proficiencyLevel": "מתחיל",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "ניתן לייבא ולייצא נתוני טופס לקובץ XML עם מרחב השמות Aspose.Pdf.Facades ב-Aspose.PDF עבור .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm הוא סוג חשוב של מסמך PDF. אתה יכול לא רק ליצור ולערוך AcroForm באמצעות [מרחב השמות Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), אלא גם לייבא ולייצא נתוני טופס לקובץ XML וממנו. מרחב השמות Aspose.Pdf.Facades ב-Aspose.PDF עבור .NET מאפשר לך ליישם תכונה נוספת של AcroForm, המסייעת לך לשלוח נתוני AcroForm לדף אינטרנט חיצוני. דף האינטרנט הזה אז קורא את משתני ה-POST ומשתמש בנתונים אלו לעיבוד נוסף. תכונה זו שימושית במקרים שבהם אתה לא רק רוצה לשמור את הנתונים בקובץ PDF, אלא גם לשלוח אותם לשרת שלך ולאחר מכן לשמור אותם במסד נתונים וכו'.

{{% /alert %}}

## פרטי היישום

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

במאמר זה, ניסינו ליצור AcroForm באמצעות [מרחב השמות Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).
במאמר זה ניסינו ליצור AcroForm באמצעות [Aspose.Pdf.Facades namepsace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).

```csharp
// צור מופע של מחלקת FormEditor וקשר קבצי PDF קלט ופלט
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// צור שדות AcroForm - יצרתי רק שני שדות לפשטות
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// הוסף כפתור שליחה וקבע את כתובת ה-URL היעד
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// שמור את קובץ ה-PDF המוצא
editor.Save();
```

{{% alert color="primary" %}}

הקטע קוד הבא מראה איך לקבל את הערכים שנשלחו בדף האינטרנט היעד.
הקטע הבא מראה איך לקבל את הערכים שנשלחו בדף היעד.

{{% /alert %}}

```csharp
// מציג את הערכים שנשלחו בדף האינטרנט של היעד
Response.Write("שלום " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
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

