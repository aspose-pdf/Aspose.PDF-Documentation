---
title: איך להדפיס קובץ PDF ב-.NET Core
linktitle: הדפסת PDF ב-.NET Core
type: docs
weight: 40
url: /net/print-dotnetcore/
keywords: "print pdf .net core"
description: דף זה מסביר איך להמיר מסמך PDF ל-XPS ב-.NET Core ולהוסיף אותו כמשימה לתור המדפסת המקומית.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "איך להדפיס קובץ PDF ב-.NET Core",
    "alternativeHeadline": "הדפסת קובץ PDF ב-.NET Core",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכים ב-PDF",
    "keywords": "pdf, c#, pdf ב-.NET Core",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2022-02-04",
    "description": "דף זה מסביר איך להמיר מסמך PDF ל-XPS ולהוסיף אותו כמשימה לתור המדפסת המקומית."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **הדפסת מסמך PDF ב-.NET Core**

ספריית Aspose.PDF מאפשרת לנו להמיר קבצי PDF ל-XPS. פונקציה זו יכולה להיות שימושית לארגון הדפסת מסמכים. בואו נבחן דוגמה לשימוש במדפסת ברירת המחדל:

```csharp
class Program
{
    static void Main()
    {
        // יצירת התהליך המשני והעברת שיטת ההדפסה עבור
        // פרמטר המשלח של נציג ThreadStart של הבנאי.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // הגדרת התהליך שישתמש ב-PrintQueue.AddJob לתהליך חד-ניטי.
        printingThread.SetApartmentState(ApartmentState.STA);

        // התחלת תהליך ההדפסה. השיטה שהועברה לבנאי
        // של התהליך תבוצע.
        printingThread.Start();
    }//סיום Main

    private static void PrintPDF(string pdfFileName)
    {
        // יצירת שרת הדפסה ותור הדפסה.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // הדפסת קובץ ה-Xps תוך ספק אימות XPS והתראות התקדמות.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0} לא ניתן להוסיף לתור ההדפסה.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\tזהו לא קובץ XPS תקף. השתמש בכלי התאמת isXPS כדי לאבחן אותו.");
            }
            Console.WriteLine("\tהמשך עם קובץ XPS הבא.\n");
        }
    }
}//סיום כיתת Program
```
בדוגמה זו, אנו ממירים מסמך PDF ל-XPS ומוסיפים אותו כמשימה לתור של המדפסת המקומית.

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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
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

