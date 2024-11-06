---
title: Travailler avec les formulaires XFA
linktitle: Formulaires XFA
type: docs
weight: 20
url: fr/net/xfa-forms/
description: Aspose.PDF pour l'API .NET vous permet de travailler avec les champs XFA et XFA Acroform dans un document PDF. Les Aspose.PDF.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les formulaires XFA",
    "alternativeHeadline": "Remplir, Convertir et Obtenir les formulaires XFA dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, c#, remplir formulaire xfa, obtenir formulaire xfa, convertir formulaire xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour l'API .NET vous permet de travailler avec les champs XFA et XFA Acroform dans un document PDF. Les Aspose.PDF.Facades."
}
</script>
{{% alert color="primary" %}}

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'"Architecture des formulaires XML". Il peut également convertir un formulaire XFA dynamique en Acroform standard. Les informations concernant le formulaire (en ce qui concerne le PDF) sont très vagues – elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucune représentation. Les objets du formulaire XFA sont dessinés au moment du chargement du document.

{{% /alert %}}

La classe Form fournit la capacité de traiter avec l'AcroForm statique et vous pouvez obtenir une instance de champ particulière en utilisant la méthode GetFieldFacade(..) de la classe Form. Cependant, les champs XFA ne peuvent pas être accessibles via la méthode Form.GetFieldFacade(..). Utilisez plutôt [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) pour obtenir/définir les valeurs des champs et manipuler le modèle de champ XFA (définir les propriétés des champs).

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Remplir les champs XFA

Le code suivant vous montre comment remplir les champs dans un formulaire XFA.
Le code suivant montre comment remplir les champs dans un formulaire XFA.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Obtenir les noms des champs du formulaire XFA
string[] names = doc.Form.XFA.FieldNames;

// Définir les valeurs des champs
doc.Form.XFA[names[0]] = "Champ 0";
doc.Form.XFA[names[1]] = "Champ 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```

## Convertir XFA en Acroform

{{% alert color="primary" %}}

Essayez en ligne
Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien : [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'"Architecture de formulaires XML".
Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l’« Architecture de formulaires XML ».

Actuellement, PDF prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF :

- AcroForms (également connus sous le nom de formulaires Acrobat), introduits et inclus dans la spécification du format PDF 1.2.
- Les formulaires Adobe XML Forms Architecture (XFA), introduits dans la spécification du format PDF 1.5 comme une fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est uniquement référencée.)

Nous ne pouvons ni extraire ni manipuler les pages des formulaires XFA, car le contenu du formulaire est généré à l'exécution (lors de la visualisation du formulaire XFA) au sein de l'application tentant d'afficher ou de rendre le formulaire XFA. Aspose.PDF dispose d'une fonctionnalité qui permet aux développeurs de convertir les formulaires XFA en AcroForms standards.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire XFA dynamique
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Définir le type des champs de formulaire comme AcroForm standard
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Sauvegarder le PDF résultant
document.Save(dataDir);
```

## Obtenir les propriétés des champs XFA

Pour accéder aux propriétés des champs, utilisez d'abord Document.Form.XFA.Teamplate pour accéder au modèle de champ. Le fragment de code suivant montre les étapes pour obtenir les coordonnées X et Y d'un champ de formulaire XFA.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Définir les valeurs des champs
doc.Form.XFA[names[0]] = "Champ 0";
doc.Form.XFA[names[1]] = "Champ 1";

// Obtenir la position du champ
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Obtenir la position du champ
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Sauvegarder le document mis à jour
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

