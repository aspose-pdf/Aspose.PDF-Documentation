---
title: Impression de PDF dans .NET Framework
linktitle: Impression de PDF dans .NET Framework
type: docs
weight: 10
url: /fr/net/printing-pdf-in-net-framework/
description: Vous pouvez imprimer des fichiers PDF sur l'imprimante par défaut en utilisant les paramètres d'imprimante et de page avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
 
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impression de PDF dans .NET Framework",
    "alternativeHeadline": "Comment imprimer PDF dans .NET Framework",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, c#, pdf dans .NET Framework",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez imprimer des fichiers PDF sur l'imprimante par défaut en utilisant les paramètres d'imprimante et de page avec C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## **Imprimer un fichier PDF en C# - Imprimer un fichier PDF sur l'imprimante par défaut en utilisant les paramètres d'imprimante et de page**

Cet article décrit comment imprimer un fichier PDF sur l'imprimante par défaut en utilisant les paramètres d'imprimante et de page en C#.

La classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) vous permet d'imprimer un fichier PDF sur l'imprimante par défaut. Vous devez créer un objet PdfViewer et ouvrir le PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Pour spécifier différents paramètres d'impression, utilisez les classes `PageSettings` et `PrinterSettings`. Enfin, appelez la méthode [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) pour imprimer le PDF sur l'imprimante par défaut. Le code suivant montre comment imprimer un PDF sur l'imprimante par défaut avec les paramètres d'imprimante et de page.

```csharp
public static void SimplePrint()
{
    // Créer un objet PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Ouvrir le fichier PDF d'entrée
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Définir les attributs pour l'impression
    viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
    viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée
    viewer.PrintPageDialog = false;   // Ne pas produire de dialogue de numéro de page lors de l'impression

    // Créer des objets pour les paramètres d'imprimante et de page et PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Définir le nom de l'imprimante
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Définir PageSize (si nécessaire)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Définir les marges de la page (si nécessaire)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimer le document en utilisant les paramètres d'imprimante et de page
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Fermer le fichier PDF après l'impression
    viewer.Close();
}
```
Pour afficher une boîte de dialogue d'impression, essayez d'utiliser le fragment de code suivant :

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // Le code d'impression du document va ici
    // Imprimer le document en utilisant les paramètres d'imprimante et de page
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```
## Choosing paper source by PDF page size
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the 'Document.PickTrayByPdfSize' property.

```cs
using (Document document = new Document())
{
    Page page = document.Pages.Add();
    page.Paragraphs.Add(new TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;
    document.Save("result.pdf");
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

