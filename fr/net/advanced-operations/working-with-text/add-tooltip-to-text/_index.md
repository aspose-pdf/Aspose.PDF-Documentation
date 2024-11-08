```
---
title: PDF Tooltip using C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: /fr/net/pdf-tooltip/
description: Apprenez à ajouter une infobulle au fragment de texte dans un PDF en utilisant C# et Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using C#",
    "alternativeHeadline": "Add PDF Tooltip to the Text",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, add pdf tooltip",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "Apprenez à ajouter une infobulle au fragment de texte dans un PDF en utilisant C# et Aspose.PDF"
}
</script>
```
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter une infobulle au texte recherché en ajoutant un bouton invisible

Il est souvent nécessaire d'ajouter des détails pour une phrase ou un mot spécifique sous forme d'infobulle dans le document PDF afin qu'elle apparaisse lorsque l'utilisateur passe le curseur de la souris sur le texte. Aspose.PDF pour .NET offre cette fonctionnalité de créer des infobulles en ajoutant un bouton invisible sur le texte recherché. Le fragment de code suivant vous montrera comment atteindre cette fonctionnalité :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Créer un document exemple avec texte
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Déplacez le curseur de la souris ici pour afficher une infobulle"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Déplacez le curseur de la souris ici pour afficher une infobulle très longue"));
doc.Save(outputFile);

// Ouvrir le document avec texte
Document document = new Document(outputFile);
// Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Déplacez le curseur de la souris ici pour afficher une infobulle");
// Accepter l'absorbeur pour les pages du document
document.Pages.Accept(absorber);
// Obtenir les fragments de texte extraits
TextFragmentCollection textFragments = absorber.TextFragments;

// Boucle à travers les fragments
foreach (TextFragment fragment in textFragments)
{
    // Créer un bouton invisible à la position du fragment de texte
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // La valeur AlternateName sera affichée comme infobulle par une application de visualisation
    field.AlternateName = "Infobulle pour le texte.";
    // Ajouter le champ bouton au document
    document.Form.Add(field);
}

// Ensuite sera un exemple d'infobulle très longue
absorber = new TextFragmentAbsorber("Déplacez le curseur de la souris ici pour afficher une infobulle très longue");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Définir un texte très long
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// Sauvegarder le document
document.Save(outputFile);
```
{{% alert color="primary" %}}

Concernant la longueur de l'infobulle, le texte de l'infobulle est contenu dans le document PDF sous forme de chaîne PDF, en dehors du flux de contenu. Il n'y a pas de restriction effective sur de telles chaînes dans les fichiers PDF (voir Annexe C de la référence PDF). Cependant, un lecteur conforme (par exemple, Adobe Acrobat) fonctionnant sur un processeur particulier et dans un environnement d'exploitation particulier a une telle limite. Veuillez vous référer à la documentation de votre application de lecteur PDF.

{{% /alert %}}

## Créer un Bloc de Texte Caché et l'Afficher au Survol de la Souris

Dans Aspose.PDF, une fonctionnalité pour masquer des actions est implémentée par laquelle il est possible de montrer/masquer un champ de texte (ou tout autre type d'annotation) lors de l'entrée/sortie de la souris sur un bouton invisible. À cette fin, la classe Aspose.Pdf.Annotations.HideAction est utilisée pour assigner l'action de masquer/afficher au bloc de texte. Veuillez utiliser le fragment de code suivant pour Afficher/Masquer un Bloc de Texte à l'Entrée/Sortie de la Souris.

Veuillez également prendre en compte que les actions PDF dans les documents fonctionnent bien dans les lecteurs conformes (par exemple,
Veuillez également prendre en compte que les actions PDF dans les documents fonctionnent correctement dans les lecteurs conformes (par exemple,

- Toutes les implémentations de l'action de masquage dans les documents PDF fonctionnent correctement dans Internet Explorer v.11.0.
- Toutes les implémentations de l'action de masquage fonctionnent également dans Opera v.12.14, mais nous constatons un certain retard de réponse lors de la première ouverture du document.
- Seule l'implémentation utilisant le constructeur HideAction acceptant le nom du champ fonctionne si Google Chrome v.61.0 parcourt le document ; Veuillez utiliser les constructeurs correspondants si la navigation dans Google Chrome est significative :

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Créer un document exemple avec du texte
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Déplacez le curseur de la souris ici pour afficher le texte flottant"));
doc.Save(outputFile);

// Ouvrir le document avec le texte
Document document = new Document(outputFile);
// Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Déplacez le curseur de la souris ici pour afficher le texte flottant");
// Accepter l'absorbeur pour les pages du document
document.Pages.Accept(absorber);
// Obtenir le premier fragment de texte extrait
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Créer un champ de texte caché pour le texte flottant dans le rectangle spécifié de la page
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Définir le texte à afficher comme valeur de champ
floatingField.Value = "Ceci est le \"champ de texte flottant\".";
// Nous recommandons de rendre le champ 'en lecture seule' pour ce scénario
floatingField.ReadOnly = true;
// Définir le drapeau 'caché' pour rendre le champ invisible à l'ouverture du document
floatingField.Flags |= AnnotationFlags.Hidden;

// Définir un nom de champ unique n'est pas nécessaire mais autorisé
floatingField.PartialName = "FloatingField_1";

// Définir les caractéristiques de l'apparence du champ n'est pas nécessaire mais le rend meilleur
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Ajouter le champ de texte au document
document.Form.Add(floatingField);

// Créer un bouton invisible sur la position du fragment de texte
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Créer une nouvelle action de masquage pour le champ spécifié (annotation) et le drapeau d'invisibilité.
// (Vous pouvez également référer le champ flottant par le nom si vous l'avez spécifié ci-dessus.)
// Ajouter des actions à l'entrée/sortie de la souris sur le champ de bouton invisible
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Ajouter le champ de bouton au document
document.Form.Add(buttonField);

// Sauvegarder le document
document.Save(outputFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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

