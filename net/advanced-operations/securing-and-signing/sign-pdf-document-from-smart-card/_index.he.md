---
title: כיצד להוסיף חתימת כרטיס חכם ל-PDF
linktitle: חתימה ב-PDF עם כרטיס חכם
type: docs
weight: 40
url: /net/sign-pdf-document-from-smart-card/
description: Aspose.PDF עבור .NET מאפשר לך לחתום על מסמכי PDF מכרטיס חכם באמצעות שדה חתימה.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "כיצד להוסיף חתימת כרטיס חכם ל-PDF",
    "alternativeHeadline": "עבודה עם חתימת כרטיס חכם ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, חתימת כרטיס חכם",
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
    "url": "/net/sign-pdf-document-from-smart-card/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sign-pdf-document-from-smart-card/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך לחתום על מסמכי PDF מכרטיס חכם באמצעות שדה חתימה."
}
</script>
Aspose.PDF עבור .NET מציעה את היכולת להוסיף חתימות דיגיטליות ממיקום מאגר מפתחות. ניתן להחיל את החתימה על ידי קבלת התעודה שמספק מאגר התעודות, כרטיס חכם או [כרטיס PIV](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card) המחובר למערכת בזמן ריצה.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

להלן קטעי הקוד לחתימה על מסמך PDF מכרטיס חכם:

## חתום עם כרטיס חכם באמצעות שדה חתימה

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

File.Copy(dataDir + "blank.pdf", dataDir + "externalSignature1.pdf", true);
using (FileStream fs = new FileStream(dataDir + "externalSignature1.pdf", FileMode.Open, FileAccess.ReadWrite))
{
    using (Document doc = new Document(fs))
    {
        SignatureField field1 = new SignatureField(doc.Pages[1], new Rectangle(100, 400, 10, 10));

        // חתום עם בחירת תעודה בחנות התעודות של חלונות
        System.Security.Cryptography.X509Certificates.X509Store store = new System.Security.Cryptography.X509Certificates.X509Store(System.Security.Cryptography.X509Certificates.StoreLocation.CurrentUser);
        store.Open(System.Security.Cryptography.X509Certificates.OpenFlags.ReadOnly);
        // בחירה ידנית של התעודה בחנות
        System.Security.Cryptography.X509Certificates.X509Certificate2Collection sel = System.Security.Cryptography.X509Certificates.X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, System.Security.Cryptography.X509Certificates.X509SelectionFlag.SingleSelection);

        Aspose.Pdf.Forms.ExternalSignature externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0])
        {
            Authority = "Me",
            Reason = "Reason",
            ContactInfo = "Contact"
        };

        field1.PartialName = "sig1";
        doc.Form.Add(field1, 1);
        field1.Sign(externalSignature);
        doc.Save();
    }
}

using (PdfFileSignature pdfSign = new PdfFileSignature(new Document(dataDir + "externalSignature1.pdf")))
{
    IList<string> sigNames = pdfSign.GetSignNames();
    for (int index = 0; index <= sigNames.Count - 1; index++)
    {
        if (!pdfSign.VerifySigned(sigNames[index]) || !pdfSign.VerifySignature(sigNames[index]))
        {
            throw new ApplicationException("Not verified");
        }
    }
}
```
## חתימה עם כרטיס חכם באמצעות חתימת קובץ PDF

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

Document doc = new Document(dataDir + "blank.pdf");

using (Facades.PdfFileSignature pdfSign = new Facades.PdfFileSignature())
{
    pdfSign.BindPdf(doc);

    // חתימה עם בחירת תעודה בחנות תעודות של חלונות
    System.Security.Cryptography.X509Certificates.X509Store store = new System.Security.Cryptography.X509Certificates.X509Store(System.Security.Cryptography.X509Certificates.StoreLocation.CurrentUser);
    store.Open(System.Security.Cryptography.X509Certificates.OpenFlags.ReadOnly);
    // בחירה ידנית של התעודה בחנות
    System.Security.Cryptography.X509Certificates.X509Certificate2Collection sel = System.Security.Cryptography.X509Certificates.X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, System.Security.Cryptography.X509Certificates.X509SelectionFlag.SingleSelection);

    Aspose.Pdf.Forms.ExternalSignature externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0]);
    pdfSign.SignatureAppearance = dataDir + "demo.png";
    pdfSign.Sign(1, "Reason", "Contact", "Location", true, new System.Drawing.Rectangle(100, 100, 200, 200), externalSignature);
    pdfSign.Save(dataDir + "externalSignature2.pdf");
}

using (Facades.PdfFileSignature pdfSign = new Facades.PdfFileSignature(new Document(dataDir + "externalSignature2.pdf")))
{
    IList<string> sigNames = pdfSign.GetSignNames();
    for (int index = 0; index <= sigNames.Count - 1; index++)
    {
        if (!pdfSign.VerifySigned(sigNames[index]) || !pdfSign.VerifySignature(sigNames[index]))
        {
            throw new ApplicationException("לא אומת");
        }
    }
}
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

