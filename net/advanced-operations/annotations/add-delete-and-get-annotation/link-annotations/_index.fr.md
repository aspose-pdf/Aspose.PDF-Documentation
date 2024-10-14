---
title: Utilisation des annotations de lien dans les PDF
linktitle: Annotations de lien
type: docs
weight: 70
url: /net/link-annotations/
description: Aspose.PDF pour .NET vous permet d'ajouter, obtenir et supprimer des annotations de lien de votre document PDF.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Utilisation des annotations de lien pour les PDF",
    "alternativeHeadline": "Comment ajouter des annotations de lien dans les PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotation de texte",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter, obtenir et supprimer des annotations de texte de votre document PDF."
}
</script>

## Ajout d'une annotation de lien dans un fichier PDF existant

> Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Une [Annotation de Lien](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) représente un hyperlien, une destination ailleurs, et un document. Selon la norme PDF, l'annotation de lien peut être utilisée dans trois cas : ouvrir une vue de page, ouvrir un fichier et ouvrir une page web.

### Utilisation de l'Annotation de Lien pour ouvrir une vue de page

Plusieurs étapes supplémentaires ont été effectuées pour créer l'annotation. Nous avons utilisé 2 TextFragmentAbsorbers pour trouver des fragments à démontrer. Le premier est pour le texte de l'annotation de lien, et le second indique certains endroits dans le document.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
Pour créer l'annotation, nous avons suivi certaines étapes :

1. Créer `LinkAnnotation` et passer l'objet page et le rectangle du fragment de texte qui correspond à l'annotation.
1. Définir `Action` comme `GoToAction` et passer `XYZExplicitDestination` comme destination souhaitée. Nous avons créé `XYZExplicitDestination` basé sur la page, les coordonnées gauche et haut et le zoom.
1. Ajouter l'annotation à la collection d'annotations de la page.
1. Enregistrer le document

### Utilisation de l'annotation de lien avec destination nommée

Lors du traitement de divers documents, une situation survient lorsque vous tapez et ne savez pas où l'annotation va pointer.
Dans ce cas, vous pouvez utiliser une destination spéciale (nommée) et le code ressemblera à ceci :

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

À un autre endroit, vous pouvez créer une Destination Nomée.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### Utilisation de l'annotation de lien pour ouvrir un fichier

La même approche est utilisée lors de la création d'une annotation pour ouvrir un fichier, comme dans les exemples ci-dessus.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

La différence est que nous utiliserons `GoToRemoteAction` au lieu de `GoToAction`. Le constructeur de GoToRemoteAction reçoit deux paramètres : le nom du fichier et le numéro de page.
Vous pouvez également utiliser une autre forme et passer le nom du fichier et une destination quelconque. Évidemment, vous devez créer une telle destination avant de l'utiliser.

### Utilisation de l'annotation de lien pour ouvrir une page web

Pour ouvrir une page web, il suffit de définir `Action` avec l'objet `GoToURIAction`.
Vous pouvez passer un hyperlien comme paramètre du constructeur ou tout autre type d'URI. Par exemple, vous pouvez utiliser `callto` pour implémenter une action avec appel d'un numéro de téléphone.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Créer une annotation de lien et définir l'action pour appeler un numéro de téléphone
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## Ajout d'une annotation de lien décorée

Vous pouvez personnaliser l'annotation de lien en utilisant des bordures. Dans l'exemple ci-dessous, nous allons créer une bordure bleue en pointillés d'une largeur de 3pt.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Un autre exemple montre comment simuler le style du navigateur et utiliser l'underline pour les liens.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Obtenir les annotations de lien

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir LinkAnnotation à partir du document PDF.

```csharp
class ExampleLinkAnnotations
{
    // Le chemin vers le répertoire des documents.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // Charger le fichier PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Imprimer l'URL de chaque annotation de lien
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Imprimer le texte associé au lien hypertexte
            Console.WriteLine(extractedText);
        }
    }
}
```
### Supprimer les annotations de lien

Le code suivant montre comment supprimer une annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la 1ère page. Après cela, nous enregistrerons le document avec l'annotation supprimée.

```csharp
class ExampleLinkAnnotations
{
    // Le chemin vers le répertoire des documents.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Charger le fichier PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Trouver et supprimer toutes les annotations de lien sur la 1ère page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Enregistrer le document avec l'annotation supprimée
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
