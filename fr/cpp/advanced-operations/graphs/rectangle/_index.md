---
title: Ajouter un objet Rectangle au fichier PDF
linktitle: Ajouter Rectangle
type: docs
weight: 50
url: fr/cpp/add-rectangle/
description: Cet article explique comment créer un objet Rectangle dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Rectangle

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) où vous proposez également la fonction de remplir l'objet rectangle avec une certaine couleur, contrôler l'ordre Z, ajouter un remplissage de couleur en dégradé, etc.

Tout d'abord, examinons la possibilité de créer un objet Rectangle.

Suivez les étapes ci-dessous :

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Ajoutez une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) à la collection de pages du fichier PDF

1. Ajouter [Fragment de texte](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à la collection de paragraphes de l'instance de page

1. Créer une instance de [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. Définir la bordure pour l'[objet de dessin](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. Créer une instance de Rectangle

1. Ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) à la collection de formes de l'objet Graph

1. Ajouter l'objet de graph à la collection de paragraphes de l'instance de page

1. Ajouter [Fragment de texte](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à la collection de paragraphes de l'instance de page

1. Et sauvegarder votre fichier PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Créer un objet de graph avec des dimensions identiques à celles spécifiées pour l'objet Rectangle
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Pouvons-nous changer la position de l'instance de graph
                IsChangePosition = false,
                // Définir la position de coordonnée gauche pour l'instance Graph
                Left = x,
                // Définir la position de coordonnée supérieure pour l'objet Graph
                Top = y
            };
            // Ajouter un rectangle à l'intérieur du "graph"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Définir la couleur de remplissage du rectangle
            rect.GraphInfo.FillColor = color;
            // Couleur de l'objet graph
            rect.GraphInfo.Color = color;
            // Ajouter le rectangle à la collection de formes de l'instance de graph
            graph.Shapes.Add(rect);
            // Définir l'indice Z pour l'objet rectangle
            graph.ZIndex = zindex;
            // Ajouter le graph à la collection de paragraphes de l'objet page
            page.Paragraphs.Add(graph);
        }
```
![Créer Rectangle](create_rectangle.png)

## Créer un Objet Rectangle Rempli

Aspose.PDF pour C++ offre également la fonctionnalité de remplir un objet rectangle avec une certaine couleur.

Le fragment de code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) qui est rempli de couleur.

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

            // Ajouter un objet graphique à la collection de paragraphes de l'instance de page
            page.Paragraphs.Add(graph);

            // Créer une instance de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);

            // Spécifier la couleur de remplissage pour l'objet Graph
            rect.GraphInfo.FillColor = Color.Red;

            // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
            graph.Shapes.Add(rect);

            // Enregistrer le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Regardez le résultat d'un rectangle rempli de couleur unie :

![Rectangle Rempli](fill_rectangle.png)

## Ajouter un dessin avec un remplissage en dégradé

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajout d'objets graphiques aux documents PDF et il est parfois nécessaire de remplir les objets graphiques avec une couleur en dégradé. Pour remplir des objets graphiques avec une couleur en dégradé, nous devons définir setPatterColorSpace avec l'objet gradientAxialShading comme suit.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) qui est rempli avec une couleur en dégradé.

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

            // Enregistrer le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## Créer un rectangle avec un canal de couleur Alpha

Aspose.PDF pour C+++ prend en charge le remplissage d'un objet rectangle avec une certaine couleur. Un objet rectangle peut également avoir un canal de couleur Alpha pour donner un aspect transparent. L'extrait de code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) avec un canal de couleur Alpha.

Les pixels de l'image peuvent stocker des informations sur leur opacité ainsi que sur la valeur de la couleur. Cela permet de créer des images avec des zones transparentes ou semi-transparentes.

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
            // Ajouter un objet graphique à la collection de paragraphes de l'instance de page
            page.Paragraphs.Add(graph);
            // Créer une instance de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);
            // Spécifier la couleur de remplissage pour l'objet Graph
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
            graph.Shapes.Add(rect);

            // Créer un deuxième objet rectangle
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Ajouter une instance de graphique à la collection de paragraphes de l'objet de page
            page.Paragraphs.Add(graph);

            // Enregistrer le fichier PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Contrôler l'ordre Z du rectangle

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajout d'objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Lors de l'ajout de plus d'une instance du même objet dans un fichier PDF, nous pouvons contrôler leur rendu en spécifiant l'ordre Z. L'ordre Z est également utilisé lorsque nous devons rendre des objets les uns sur les autres.

Le code suivant montre les étapes pour rendre les objets [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) les uns sur les autres.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instancier un objet de classe Document
            Document doc1 = new Document();
            /// Ajouter une page à la collection de pages du fichier PDF
            Page page1 = doc1.Pages.Add();
            // Définir la taille de la page PDF
            page1.SetPageSize(375, 300);
            // Définir la marge gauche de l'objet page à 0
            page1.PageInfo.Margin.Left = 0;
            // Définir la marge supérieure de l'objet page à 0
            page1.PageInfo.Margin.Top = 0;
            // Créer un nouveau rectangle avec la couleur rouge, ordre Z à 0 et des dimensions spécifiques
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Créer un nouveau rectangle avec la couleur bleue, ordre Z à 0 et des dimensions spécifiques
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Créer un nouveau rectangle avec la couleur verte, ordre Z à 0 et des dimensions spécifiques
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Enregistrer le fichier PDF résultant
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![Contrôler l'ordre Z](control.png)