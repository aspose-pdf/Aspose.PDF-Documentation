---
title: Ajouter des annotations de figures en utilisant C#
linktitle: Annotations de figures
type: docs
weight: 30
url: fr/net/figures-annotation/
description: Cet article décrit comment ajouter, obtenir et supprimer des annotations de figures de votre document PDF avec Aspose.PDF pour .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des annotations de figures en utilisant C#",
    "alternativeHeadline": "Comment ajouter des annotations de figures dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotations de figures, annotation polygonale, annotation de ligne, annotation carrée, annotation circulaire",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article décrit comment ajouter, obtenir et supprimer des annotations de figures de votre document PDF avec Aspose.PDF pour .NET"
}
</script>
L'application de gestion de documents PDF offre divers outils pour annoter des documents. Du point de vue de la structure interne du PDF, ces outils sont des annotations. Nous prenons en charge les types d'outils de dessin suivants.

* Annotation Ligne - outil pour dessiner des lignes et des flèches
* Annotation Carré - pour dessiner des carrés et des rectangles
* Annotation Cercle - pour les ovales et les cercles
* Annotation TexteLibre - pour les commentaires de type légende
* Annotation Polygone - pour les polygones et les nuages
* Annotation Polyligne - pour les lignes connectées

## Ajout de Formes et de Figures sur la Page

L'approche pour ajouter l'annotation est typique pour chacune d'entre elles.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Charger le fichier PDF ou en créer un nouveau par [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créer la nouvelle annotation et définir les paramètres (nouveau Rectangle, nouveau Point, titre, couleur, largeur, etc).
1.
1. Associer l'annotation popup à l'originale.
1. Ajouter l'annotation à la page

## Ajout de lignes ou de flèches

L'objectif de l'annotation de ligne est d'afficher une ligne droite ou une flèche sur la page.
Pour créer une ligne, nous avons besoin d'un nouvel objet LineAnnotation.
Le constructeur de la classe LineAnnotation prend quatre paramètres :

* la page où l'annotation sera ajoutée,
* le rectangle qui définit la limite de l'annotation,
* et les deux points qui définissent le début et la fin de la ligne.

Nous devons également initialiser certaines propriétés :

* `Title` - généralement, c'est le nom de l'utilisateur qui a fait ce commentaire
* `Subject` - peut être n'importe quelle chaîne, mais dans les cas courants c'est un nom d'annotation

Pour styliser notre ligne, nous devons définir la couleur, la largeur, le style de début et le style de fin.
Pour styliser notre ligne, nous devons définir la couleur, la largeur, le style de départ et le style de fin.

Le fragment de code suivant montre comment ajouter une annotation de ligne à un fichier PDF :

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// Créer une annotation de ligne
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Ajouter l'annotation à la page
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## Ajout de carré ou de cercle

Les annotations [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) et [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) afficheront un rectangle ou une ellipse sur la page.
Les annotations [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) et [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) afficheront un rectangle ou une ellipse sur la page.

### Ajout d'une annotation Circle

Pour dessiner une nouvelle annotation de cercle ou d'ellipse, nous devons créer un nouvel objet CircleAnnotation. Le constructeur de la classe `CircleAnnotation` prend deux paramètres :

* la page où l'annotation sera ajoutée,
* et le rectangle qui définit la limite de l'annotation

Nous pouvons également définir certaines propriétés de l'objet `CircleAnnotation`, telles que le titre, la couleur, la couleur intérieure, l'opacité. Ces propriétés contrôlent l'apparence et le comportement de l'annotation dans le visualiseur PDF. Ici et plus loin dans le Square, la couleur `InteriorColor` est la couleur de remplissage et `Color` est la couleur de la bordure.

### Ajout d'une annotation Square

Dessiner un rectangle est identique à dessiner un cercle.
Dessiner un rectangle est identique à dessiner un cercle.

```csharp
var dataDir = "<chemin-vers-fichier>";
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Créer l'annotation Cercle
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Cercle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Créer l'annotation Carré
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Ajouter l'annotation à la page
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
Comme exemple, nous verrons le résultat suivant de l'ajout d'annotations Carré et Cercle à un document PDF :

![Démonstration d'annotation Cercle et Carré](circle_demo.png)

## Ajout d'annotations Polygone et Polyligne

L'outil Poly- vous permet de créer des formes et des contours avec un nombre arbitraire de côtés sur le document.

**Annotations Polygone** représentent des polygones sur une page. Ils peuvent avoir un nombre quelconque de sommets reliés par des lignes droites.
**Annotations Polyligne** sont également similaires aux polygones, la seule différence est que les sommets de début et de fin ne sont pas implicitement connectés.

### Ajout d'une annotation Polygone

PolygonAnnotation est responsable des annotations polygonales. Le constructeur de la classe PolygonAnnotation prend trois paramètres :

* la page où l'annotation sera ajoutée,
* le rectangle qui définit la limite de l'annotation,
* et un tableau de points qui définissent les sommets du polygone.

`Color` et `InteriorColor` sont utilisés respectivement pour les couleurs de la bordure et du remplissage.

### Ajout d'une annotation Polyligne
### Ajout d'une annotation Polyline

PolygonAnnotation est responsable des annotations de polygones. Le constructeur de la classe PolygonAnnotation prend trois paramètres :

* la page où l'annotation sera ajoutée,
* le rectangle qui définit la limite de l'annotation,
* et un tableau de points qui définissent les sommets du polygone.

Au lieu de `PolygonAnnotation`, nous ne pouvons pas remplir cette forme, donc nous n'avons pas besoin d'utiliser `InteriorColor`.

Le code suivant montre comment ajouter des annotations de polygon et de polyline à un fichier PDF :

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Créer une annotation de polygone
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Créer une annotation de polyligne
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Ajouter l'annotation à la page
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## Obtention de Figures

Toutes les annotations sont stockées dans la collection `Annotations`. Toute annotation peut indiquer son type via la propriété `AnnotationType`. Par conséquent, nous pouvons faire une requête LINQ pour filtrer les annotations souhaitées.

### Obtention des Annotations Linéaires

L'exemple ci-dessous explique comment obtenir toutes les Annotations Linéaires de la première page du document PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Obtention des Annotations Circulaires

L'exemple ci-dessous explique comment obtenir toutes les Annotations Polyligne de la première page du document PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### Obtenir les annotations carrées

L'exemple ci-dessous explique comment obtenir toutes les annotations carrées de la première page du document PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Obtenir les annotations polyligne

L'exemple ci-dessous explique comment obtenir toutes les annotations polyligne de la première page du document PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Obtenir les annotations polygone
L'exemple ci-dessous explique comment obtenir toutes les annotations de polygone de la première page du document PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Suppression de figures

La méthode pour supprimer une annotation d'un PDF est assez simple :

* Sélectionnez les annotations à supprimer (créez une collection)
* Itérez sur la collection en utilisant une boucle foreach, et supprimez chaque annotation de la collection des annotations en utilisant la méthode Delete.

### Suppression d'une annotation de ligne

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### Supprimer les annotations de cercle et de carré

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### Supprimer les annotations de polygone et de polyligne

Le code suivant montre comment supprimer les annotations de polygone et de polyligne d'un fichier PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## Comment ajouter une annotation à l'encre dans un fichier PDF

Une annotation à l'encre représente un gribouillage à main levée composé d'un ou plusieurs chemins disjoints. Lorsqu'elle est ouverte, elle doit afficher une fenêtre pop-up contenant le texte de la note associée.

L'[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) représente un gribouillage à main levée composé d'un ou plusieurs points disjoints. Veuillez essayer d'utiliser le fragment de code suivant pour ajouter une InkAnnotation dans un document PDF.

```csharp
// Charger le fichier PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Sauvegarder le fichier de sortie
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### Définir la largeur de ligne de InkAnnotation

La largeur de [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) peut être modifiée en utilisant les objets LineInfo et Border.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Titre";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Sauvegarder le fichier de sortie
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
### Supprimer l'annotation circulaire

Le code suivant montre comment supprimer une annotation circulaire d'un fichier PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // Charger le fichier PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
