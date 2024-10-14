---
title: חלץ מידע על תמונה וחתימה
linktitle: חלץ מידע על תמונה וחתימה
type: docs
weight: 30
url: /net/extract-image-and-signature-information/
description: תוכל לחלץ תמונות משדה החתימה ולחלץ מידע על חתימה באמצעות המחלקה SignatureField עם C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חלץ מידע על תמונה וחתימה",
    "alternativeHeadline": "כיצד לחלץ תמונה וחתימה מ-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, חלץ חתימה",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2022-02-04",
    "description": "תוכל לחלץ תמונות משדה החתימה ולחלץ מידע על חתימה באמצעות המחלקה SignatureField עם C#."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## חילוץ תמונה משדה חתימה

Aspose.PDF עבור .NET תומכת בתכונה לחתום דיגיטלית על קבצי PDF באמצעות מחלקת [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) ובעת חתימת המסמך, ניתן גם להגדיר תמונה עבור SignatureAppearance. כעת, ה-API גם מספקת את היכולת לחלץ מידע על החתימה כמו גם את התמונה הקשורה לשדה החתימה.

על מנת לחלץ מידע על החתימה, הצגנו את שיטת [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) למחלקת SignatureField. אנא עיין בקטע הקוד הבא שמדגים את השלבים לחילוץ תמונה מאובייקט SignatureField:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir+ @"ExtractingImage.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            string outFile = dataDir+ @"output_out.jpg";
            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    using (System.Drawing.Image image = Bitmap.FromStream(imageStream))
                    {
                        image.Save(outFile, System.Drawing.Imaging.ImageFormat.Jpeg);
                    }
                }
            }
        }
    }
}
```
### החלפת תמונת חתימה

לפעמים יכול להיות לך דרישה להחליף רק את תמונת שדה חתימה שכבר קיים בתוך קובץ PDF. כדי לעמוד בדרישה זו, ראשית עלינו לחפש שדות טפסים בתוך קובץ ה-PDF, לזהות שדות חתימה, לקבל את הממדים (ממדים מלבניים) של שדה החתימה ולאחר מכן לחתום תמונה מעל אותם ממדים.

## חילוץ מידע חתימה

Aspose.PDF עבור .NET תומך בתכונה לחתימה דיגיטלית על קבצי PDF באמצעות מחלקת SignatureField. כרגע אנו יכולים גם לקבוע את תקפות התעודה אך איננו יכולים לחלץ את כל התעודה. המידע שניתן לחלץ הוא מפתח ציבורי, טביעת אצבע, מנפיק וכו'.

לשם חילוץ מידע חתימה, הוספנו את השיטה [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) למחלקת [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield).
כדי לחלץ מידע על חתימה, הוספנו את השיטה [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) למחלקה [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield).

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir + "ExtractSignatureInfo.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream != null)
            {
                using (cerStream)
                {
                    byte[] bytes = new byte[cerStream.Length];
                    using (FileStream fs = new FileStream(dataDir + @"input.cer", FileMode.CreateNew))
                    {
                        cerStream.Read(bytes, 0, bytes.Length);
                        fs.Write(bytes, 0, bytes.Length);
                    }
                }
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF ל-.NET",
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
```

