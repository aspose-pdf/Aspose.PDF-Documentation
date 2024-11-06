---
title: Extract AcroForm - Extraire les données de formulaire d'un PDF en C#
linktitle: Extract AcroForm
type: docs
weight: 30
url: fr/net/extract-form/
keywords: extract form data from pdf c#
description: Extraire un formulaire de votre document PDF avec la bibliothèque Aspose.PDF pour .NET. Obtenez la valeur d'un champ individuel du fichier PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "Comment extraire AcroForm d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, extract acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Extraire un formulaire de votre document PDF avec la bibliothèque Aspose.PDF pour .NET. Obtenez la valeur d'un champ individuel du fichier PDF."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Extraire des données d'un formulaire

### Obtenir les valeurs de tous les champs du document PDF

Pour obtenir les valeurs de tous les champs d'un document PDF, vous devez naviguer à travers tous les champs du formulaire puis obtenir la valeur en utilisant la propriété Value. Obtenez chaque champ de la collection Form, dans le type de champ de base appelé Field et accédez à sa propriété Value.

Les extraits de code C# suivants montrent comment obtenir les valeurs de tous les champs d'un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Obtenir les valeurs de tous les champs
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Nom du champ : {0} ", formField.PartialName);
    Console.WriteLine("Valeur : {0} ", formField.Value);
}
```
### Obtenir la valeur d'un champ individuel d'un document PDF

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire de la collection Form de l'objet Document. Cet exemple en C# sélectionne un [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) et récupère sa valeur en utilisant la propriété Value.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Obtenir un champ
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Obtenir la valeur du champ
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

Pour obtenir l'URL du bouton de soumission, utilisez les lignes de code suivantes.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Obtenir les champs de formulaire d'une région spécifique d'un fichier PDF

Parfois, vous pouvez savoir où dans un document se trouve un champ de formulaire, mais vous ne connaissez pas son nom. Par exemple, si tout ce que vous avez est un schéma d'un formulaire imprimé. Avec Aspose.PDF pour .NET, ce n'est pas un problème. Vous pouvez découvrir quels champs se trouvent dans une région donnée d'un fichier PDF. Pour obtenir les champs de formulaire d'une région spécifique d'un fichier PDF :

1. Ouvrez le fichier PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Obtenez le formulaire de la collection de formulaires du document.
3. Spécifiez la région rectangulaire et passez-la à la méthode GetFieldsInRect de l'objet Form. Une collection de champs est renvoyée.
4. Utilisez cela pour manipuler les champs.

Le fragment de code C# suivant montre comment obtenir les champs de formulaire dans une région rectangulaire spécifique d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le fichier pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Créer un objet rectangle pour obtenir les champs dans cette zone
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Obtenir le formulaire PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// Obtenir les champs dans la zone rectangulaire
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Afficher les noms et valeurs des champs
foreach (Field field in fields)
{
    // Afficher les propriétés de placement des images pour tous les placements
    Console.Out.WriteLine("Nom du champ : " + field.FullName + "-" + "Valeur du champ : " + field.Value);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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

