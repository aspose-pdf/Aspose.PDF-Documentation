---
title: Impression PDF sur une imprimante XPS
linktitle: Impression PDF sur une imprimante XPS (Facades)
type: docs
weight: 20
url: /fr/net/printing-pdf-to-an-xps-printer-facades/
description: Cette page montre comment imprimer un PDF sur une imprimante XPS en utilisant la classe PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impression PDF sur une imprimante XPS",
    "alternativeHeadline": "Comment imprimer un PDF sur une imprimante XPS",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, pdf vers une imprimante XPS",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette page montre comment imprimer un PDF sur une imprimante XPS en utilisant la classe PdfViewer."
}
</script>
## **Imprimer un PDF sur une imprimante XPS en C#**

Vous pouvez imprimer un fichier PDF sur une imprimante XPS, ou sur une autre imprimante logicielle, en utilisant la classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Pour ce faire, créez un objet de la classe PdfViewer et ouvrez le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Vous pouvez définir différents paramètres d'impression à l'aide des classes PrinterSettings et PageSettings. Vous devez également définir la propriété PrinterName sur l'imprimante XPS ou autre imprimante logicielle que vous avez installée.

Enfin, utilisez la méthode [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) pour imprimer le PDF sur l'imprimante XPS ou autre imprimante logicielle. Le fragment de code suivant vous montre comment imprimer le fichier PDF sur une imprimante XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // Créer l'objet PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Ouvrir le fichier PDF d'entrée
    viewer.BindPdf(_dataDir + "input.pdf");

    // Définir les attributs pour l'impression
    viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
    viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée
    viewer.PrintPageDialog = false;   // Ne pas produire de dialogue de numéro de page lors de l'impression

    // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Définir le nom de l'imprimante XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // Ou définir l'imprimante PDF
    // Ps.PrinterName = "Adobe PDF";

    // Définir la taille de la page (si nécessaire)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Définir les marges de la page (si nécessaire)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Fermer le fichier PDF après l'impression
    viewer.Close();
}
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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

