---
title: Ajouter un objet Rectangle au fichier PDF
linktitle: Ajouter Rectangle
type: docs
weight: 50
url: fr/net/add-rectangle/
description: Cet article explique comment créer un objet Rectangle dans votre PDF en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un objet Rectangle au fichier PDF",
    "alternativeHeadline": "Comment créer un objet Rectangle dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, rectangle dans pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment créer un objet Rectangle dans votre PDF en utilisant Aspose.PDF pour .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un objet Rectangle

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) où vous offrez également la fonctionnalité de remplir l'objet rectangle avec une certaine couleur, contrôler l'ordre Z, ajouter un remplissage de couleur dégradé, etc.

D'abord, examinons la possibilité de créer un objet Rectangle.

Suivez les étapes ci-dessous :

1. Créer un nouveau [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF

1. Ajouter une [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à la collection de pages du fichier PDF

1. Ajouter un [Fragment de texte](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) à la collection de paragraphes de l'instance de page

1. Créer une instance de [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. Créez une instance de Rectangle

1. Ajoutez un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) à la collection de formes de l'objet Graph

1. Ajoutez l'objet graphique à la collection de paragraphes de l'instance de page

1. Ajoutez un [fragment de texte](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) à la collection de paragraphes de l'instance de page

1. Et enregistrez votre fichier PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Créer un objet graphique avec les dimensions spécifiées pour l'objet Rectangle
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Peut-on changer la position de l'instance graphique
                IsChangePosition = false,
                // Définir la position de coordonnée gauche pour l'instance Graph
                Left = x,
                // Définir la position de coordonnée haute pour l'objet Graph
                Top = y
            };
            // Ajouter un rectangle à l'intérieur du "graph"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Définir la couleur de remplissage du rectangle
            rect.GraphInfo.FillColor = color;
            // Couleur de l'objet graphique
            rect.GraphInfo.Color = color;
            // Ajouter le rectangle à la collection de formes de l'instance graphique
            graph.Shapes.Add(rect);
            // Définir l'index Z pour l'objet rectangle
            graph.ZIndex = zindex;
            // Ajouter le graph à la collection de paragraphes de l'objet page
            page.Paragraphs.Add(graph);
        }
```
![Créer un rectangle](create_rectangle.png)

## Créer un objet rectangle rempli

Aspose.PDF pour .NET offre également la fonctionnalité de remplir un objet rectangle avec une certaine couleur.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) qui est rempli de couleur.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Créer une instance de Document
            var doc = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = doc.Pages.Add();
            // Créer une instance de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Ajouter l'objet graphique à la collection de paragraphes de l'instance de page
            page.Paragraphs.Add(graph);

            // Créer une instance de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);

            // Spécifier la couleur de remplissage pour l'objet Graph
            rect.GraphInfo.FillColor = Color.Red;

            // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
            graph.Shapes.Add(rect);

            // Sauvegarder le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
Regardez le résultat d'un rectangle rempli d'une couleur unie :

![Rectangle rempli](fill_rectangle.png)

## Ajouter un dessin avec remplissage dégradé

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter des objets graphiques aux documents PDF et il est parfois nécessaire de remplir les objets graphiques avec une couleur dégradée. Pour remplir les objets graphiques avec une couleur dégradée, nous devons définir setPatterColorSpace avec un objet gradientAxialShading comme suit.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) qui est rempli avec une couleur dégradée.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Créer une instance de Document
            var doc = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = doc.Pages.Add();
            // Créer une instance de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Ajouter un objet graphique à la collection de paragraphes de l'instance de page
            page.Paragraphs.Add(graph);
            // Créer une instance de Rectangle
            var rect = new Rectangle(0, 0, 300, 300);
            // Spécifier la couleur de remplissage pour l'objet Graph
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
            graph.Shapes.Add(rect);

            // Sauvegarder le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle dégradé](gradient.png)

## Créer un rectangle avec un canal de couleur Alpha

Aspose.PDF pour .NET permet de remplir un objet rectangle avec une couleur spécifique. Un objet rectangle peut également avoir un canal de couleur Alpha pour donner un aspect transparent. Le fragment de code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) avec un canal de couleur Alpha.

Les pixels de l'image peuvent stocker des informations sur leur opacité en plus de la valeur de couleur. Cela permet de créer des images avec des zones transparentes ou semi-transparentes.

Au lieu de rendre une couleur transparente, chaque pixel stocke des informations sur son opacité. Ces données d'opacité sont appelées canal alpha et sont généralement stockées après les canaux de couleur du pixel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Créer une instance de Document
            var doc = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = doc.Pages.Add();
            // Créer une instance de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Ajouter l'objet graphique à la collection de paragraphes de l'instance de page
            page.Paragraphs.Add(graph);
            // Créer une instance de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);
            // Spécifier la couleur de remplissage pour l'objet Graph
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
            graph.Shapes.Add(rect);

            // Créer un second objet rectangle
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Ajouter l'instance de graphique à la collection de paragraphes de l'objet page
            page.Paragraphs.Add(graph);

            // Enregistrer le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## Contrôler l'ordre Z du rectangle

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple, graphique, ligne, rectangle, etc.) aux documents PDF. Lors de l'ajout de plusieurs instances du même objet dans un fichier PDF, nous pouvons contrôler leur rendu en spécifiant l'ordre Z. L'ordre Z est également utilisé lorsque nous devons rendre des objets les uns sur les autres.

Le fragment de code suivant montre les étapes pour rendre les objets [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) les uns sur les autres.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instancier l'objet de la classe Document
            Document doc1 = new Document();
            /// Ajouter une page à la collection de pages du fichier PDF
            Page page1 = doc1.Pages.Add();
            // Définir la taille de la page PDF
            page1.SetPageSize(375, 300);
            // Définir la marge gauche de l'objet page à 0
            page1.PageInfo.Margin.Left = 0;
            // Définir la marge supérieure de l'objet page à 0
            page1.PageInfo.Margin.Top = 0;
            // Créer un nouveau rectangle avec la couleur Rouge, l'ordre Z à 0 et certaines dimensions
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Créer un nouveau rectangle avec la couleur Bleue, l'ordre Z à 0 et certaines dimensions
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Créer un nouveau rectangle avec la couleur Verte, l'ordre Z à 0 et certaines dimensions
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Enregistrer le fichier PDF résultant
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Contrôle de l'ordre Z](control.png)

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


