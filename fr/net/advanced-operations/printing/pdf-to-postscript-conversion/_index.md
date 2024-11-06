---
title: Conversion de PDF en PostScript
linktitle: Conversion de PDF en PostScript
type: docs
weight: 30
url: fr/net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: Nous avons une solution pour la conversion de PDF en PostScript. Utilisez pour cette tâche l'impression et la classe PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Conversion de PDF en PostScript",
    "alternativeHeadline": "Convertir PDF en PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, pdf to postscript",
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
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "Nous avons une solution pour la conversion de PDF en PostScript. Utilisez pour cette tâche l'impression et la classe PdfViewer."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **PDF en Postscript en C#**

La classe PdfViewer fournit la capacité d'imprimer des documents PDF et avec l'aide de cette classe, nous pouvons également convertir des fichiers PDF au format PostScript. Pour convertir un fichier PDF en PostScript, installez d'abord n'importe quelle imprimante PS et imprimez simplement le fichier à l'aide de PdfViewer. Vous pouvez suivre les instructions spécifiées par l'Université d'Hawaii sur la façon d'installer une imprimante PS. Le fragment de code suivant vous montre comment imprimer et convertir un PDF en format PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // Le chemin vers le répertoire des documents.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Définir les paramètres de l'imprimante et les paramètres de page
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Définir l'imprimante PS, on peut trouver ce pilote dans la liste des pilotes d'imprimante préinstallés sur Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Définir le nom du fichier de sortie et l'attribut PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Désactiver la boîte de dialogue de la page d'impression
    viewer.PrintPageDialog = false;
    // Passer l'objet des paramètres d'imprimante à la méthode
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## Vérification du statut du travail d'impression

Un fichier PDF peut être imprimé sur une imprimante physique ainsi que sur l'imprimante de documents Microsoft XPS, sans afficher de dialogue d'impression, en utilisant la classe PdfViewer. Lors de l'impression de grands fichiers PDF, le processus peut prendre beaucoup de temps, donc l'utilisateur pourrait ne pas être certain que le processus d'impression soit terminé ou ait rencontré un problème. Pour déterminer le statut d'un travail d'impression, utilisez la propriété PrintStatus. Le fragment de code suivant vous montre comment imprimer le fichier PDF sur un fichier XPS et obtenir le statut d'impression.

```csharp
public static void CheckingPrintJobStatus()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // Le chemin vers le répertoire des documents.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instancier l'objet PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Lier le fichier PDF source
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Masquer le dialogue d'impression
    viewer.PrintPageDialog = false;

    // Créer un objet Paramètres d'imprimante
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Spécifier le nom de l'imprimante
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Nom du résultat imprimé
    ps.PrintFileName = "ResultantPrintout.xps";

    // Imprimer la sortie sur fichier
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Spécifier la taille de page de l'impression
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimer le document avec les paramètres spécifiés ci-dessus
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Vérifier le statut de l'impression
    if (viewer.PrintStatus != null)
    {
        // Une exception a été lancée
        if (viewer.PrintStatus is Exception ex)
        {
            // Obtenir le message de l'exception
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // Aucune erreur détectée. Le travail d'impression est terminé avec succès
        Console.WriteLine("impression terminée sans aucun problème..");
    }
}
```
## Obtenir/Définir le nom du propriétaire de l'impression

Récemment, nous avons reçu une exigence pour obtenir/définir le nom du propriétaire de l'impression (l'utilisateur réel qui a appuyé sur le bouton d'impression sur la page web). Cette information est requise lors de l'impression du fichier PDF. Pour répondre à cette exigence, vous pouvez utiliser la propriété nommée PrinterJobName :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Lier le fichier PDF source
viewer.BindPdf(dataDir + "input.pdf");
// Spécifier le nom de la tâche d'impression
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // L'implémentation dépend du type d'application en cours d'exécution (ASP.NET, Windows forms, etc.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## Utilisation de l'usurpation d'identité

Une autre approche pour obtenir le nom du propriétaire d'une impression est d'utiliser l'usurpation d'identité (exécution des routines d'impression dans le contexte d'un autre utilisateur) ou l'utilisateur peut changer directement le nom du propriétaire en utilisant la routine SetJob.

Veuillez noter qu'il n'est pas possible de définir la valeur du propriétaire en utilisant l'API d'impression Aspose.PDF pour des raisons de sécurité. La propriété PrinterJobName peut être utilisée pour définir la valeur de la colonne du nom du document dans l'application d'impression spooler. Le fragment de code partagé ci-dessus montre simplement comment l'utilisateur peut intégrer le nom de l'utilisateur dans la colonne du nom du document (par exemple en utilisant la syntaxe UserName\documentName). Mais le réglage des colonnes Propriétaire peut être mis en œuvre de la manière suivante directement par l'utilisateur :

1) Usurpation d'identité. Comme la valeur de la colonne propriétaire contient la valeur de l'utilisateur qui exécute le code d'impression, il existe un moyen d'invoquer l'API d'impression Aspose.PDF dans le contexte d'un autre utilisateur. Par exemple, veuillez regarder la solution décrite ici. En utilisant cette classe, l'utilisateur peut atteindre un objectif :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// Ne produit pas le dialogue de numéro de page lors de l'impression
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName est une valeur de la colonne Propriétaire dans l'application spooler
    viewer.Close();
}
```
2) Utilisation de l'API Spooler et de la routine SetJob

Le snippet de code suivant montre comment imprimer certaines pages d'un fichier PDF en mode Simplex et certaines pages en mode Duplex.

```csharp
struct ParamètresDeTravailD'impression
{
    public int Jusqu'àLaPage { get; set; }
    public int DepuisLaPage { get; set; }
    public string FichierDeSortie { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int indexDeTravailD'impression = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<ParamètresDeTravailD'impression> travauxD'impression = new List<ParamètresDeTravailD'impression>();

ParamètresDeTravailD'impression travailD'impression1 = new ParamètresDeTravailD'impression();
travailD'impression1.DepuisLaPage = 1;
travailD'impression1.Jusqu'àLaPage = 3;
travailD'impression1.FichierDeSortie = output + "35925_1_3.xps";
travailD'impression1.Mode = Duplex.Default;

travauxD'impression.Add(travailD'impression1);

ParamètresDeTravailD'impression travailD'impression2 = new ParamètresDeTravailD'impression();
travailD'impression2.DepuisLaPage = 4;
travailD'impression2.Jusqu'àLaPage = 6;
travailD'impression2.FichierDeSortie = output + "35925_4_6.xps";
travailD'impression2.Mode = Duplex.Simplex;

travauxD'impression.Add(travailD'impression2);

ParamètresDeTravailD'impression travailD'impression3 = new ParamètresDeTravailD'impression();
travailD'impression3.DepuisLaPage = 7;
travailD'impression3.Jusqu'àLaPage = 7;
travailD'impression3.FichierDeSortie = output + "35925_7.xps";
travailD'impression3.Mode = Duplex.Default;

travauxD'impression.Add(travailD'impression3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(travauxD'impression[indexDeTravailD'impression].FichierDeSortie);
ps.PrintToFile = true;
ps.DepuisLaPage = travauxD'impression[indexDeTravailD'impression].DepuisLaPage;
ps.Jusqu'àLaPage = travauxD'impression[indexDeTravailD'impression].Jusqu'àLaPage;
ps.Duplex = travauxD'impression[indexDeTravailD'impression].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++indexDeTravailD'impression < travauxD'impression.Count)
    {
        ps.PrintFileName = Path.GetFullPath(travauxD'impression[indexDeTravailD'impression].FichierDeSortie);
        ps.DepuisLaPage = travauxD'impression[indexDeTravailD'impression].DepuisLaPage;
        ps.Jusqu'àLaPage = travauxD'impression[indexDeTravailD'impression].Jusqu'àLaPage;
        ps.Duplex = travauxD'impression[indexDeTravailD'impression].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
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
Sure, just provide the document you want translated into French, and I'll help you with that while preserving the original markdown formatting.
