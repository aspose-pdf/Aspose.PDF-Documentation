---
title: Working with Operators
linktitle: Working with Operators
type: docs
weight: 170
url: /fr/net/operators/
description: Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. Les classes d'opérateurs offrent de grandes fonctionnalités pour la manipulation de PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "How to use PDF operators",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, operators in pdf, use pdf operators",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. Les classes d'opérateurs offrent de grandes fonctionnalités pour la manipulation de PDF."
}
</script>

## Introduction aux opérateurs PDF et à leur utilisation

Un opérateur est un mot-clé PDF spécifiant une action qui doit être effectuée, comme peindre une forme graphique sur la page. Un mot-clé opérateur est distingué d'un objet nommé par l'absence d'un caractère de solidus initial (2Fh). Les opérateurs n'ont de sens que dans le flux de contenu.

Un flux de contenu est un objet flux PDF dont les données consistent en des instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans la [spécification PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Détails de l'implémentation

Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF.
Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF.

- L'opérateur **GSave** sauvegarde l'état graphique actuel du PDF.
- L'opérateur **ConcatenateMatrix** (concaténer matrice) est utilisé pour définir comment une image doit être placée sur la page PDF.
- L'opérateur **Do** dessine l'image sur la page.
- L'opérateur **GRestore** restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrez le document PDF d'entrée.
1. Obtenez la page spécifique où l'image doit être ajoutée.
1. Ajoutez l'image dans la collection des ressources de la page.
1. Utilisez les opérateurs pour placer l'image sur la page :
   - D'abord, utilisez l'opérateur GSave pour sauvegarder l'état graphique actuel.
   - Ensuite, utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.
   - Utilisez l'opérateur Do pour dessiner l'image sur la page.
1. Enfin, utilisez l'opérateur GRestore pour sauvegarder l'état graphique mis à jour.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant montre comment utiliser les opérateurs PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "PDFOperators.pdf");

// Définir les coordonnées
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtenir la page où l'image doit être ajoutée
Page page = pdfDocument.Pages[1];
// Charger l'image dans le flux
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Ajouter l'image à la collection Images des ressources de la page
page.Resources.Images.Add(imageStream);
// Utilisation de l'opérateur GSave : cet opérateur sauvegarde l'état graphique actuel
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Créer des objets Rectangle et Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Utilisation de l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment l'image doit être placée
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Utilisation de l'opérateur Do : cet opérateur dessine l'image
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Utilisation de l'opérateur GRestore : cet opérateur restaure l'état graphique
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```
## Dessiner un XForm sur une page en utilisant des opérateurs

Ce sujet démontre comment utiliser les opérateurs GSave/GRestore, l'opérateur ContatenateMatrix pour positionner un xForm et l'opérateur Do pour dessiner un xForm sur une page.

Le code ci-dessous enveloppe le contenu existant d'un fichier PDF avec la paire d'opérateurs GSave/GRestore. Cette approche aide à obtenir l'état graphique initial à la fin du contenu existant. Sans cette approche, des transformations indésirables pourraient subsister à la fin de la chaîne d'opérateurs existante.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // L'exemple démontre
    // l'utilisation des opérateurs GSave/GRestore
    // l'utilisation de l'opérateur ContatenateMatrix pour positionner xForm
    // l'utilisation de l'opérateur Do pour dessiner xForm sur la page

    // Envelopper le contenu existant avec la paire d'opérateurs GSave/GRestore
    //        ceci est pour obtenir l'état graphique initial à la fin du contenu existant
    //        sinon, il pourrait rester des transformations indésirables à la fin de la chaîne d'opérateurs existante
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Ajouter l'opérateur de sauvegarde de l'état graphique pour nettoyer correctement l'état graphique après les nouvelles commandes
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region créer xForm

    // Créer xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Définir la largeur et la hauteur de l'image
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Charger l'image dans le flux
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Ajouter l'image à la collection Images des ressources XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Utiliser l'opérateur Do : cet opérateur dessine l'image
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Placer le formulaire aux coordonnées x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Dessiner le formulaire avec l'opérateur Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Placer le formulaire aux coordonnées x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Dessiner le formulaire avec l'opérateur Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Restaurer l'état graphique avec GRestore après le GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## Supprimer des objets graphiques en utilisant les classes d'opérateurs

Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation de PDF. Lorsqu'un fichier PDF contient des graphiques qui ne peuvent pas être supprimés en utilisant la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), les classes d'opérateurs peuvent être utilisées à la place pour les supprimer.

Le code suivant montre comment supprimer les graphiques. Veuillez noter que si le fichier PDF contient des étiquettes textuelles pour les graphiques, elles pourraient persister dans le fichier PDF en utilisant cette approche. Par conséquent, recherchez les opérateurs graphiques pour une méthode alternative afin de supprimer de telles images.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Opérateurs de peinture de chemin utilisés
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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

