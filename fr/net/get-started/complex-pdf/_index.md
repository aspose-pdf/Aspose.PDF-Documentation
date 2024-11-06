---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 60
url: fr/net/complex-pdf-example/
description: Aspose.PDF pour NET vous permet de créer des documents plus complexes qui contiennent des images, des fragments de texte et des tables dans un seul document.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'exemple [Bonjour, Monde](/pdf/net/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant C# et Aspose.PDF. Dans cet article, nous examinerons la création d'un document plus complexe avec C# et Aspose.PDF pour .NET. À titre d'exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers.
Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe) et un tableau. Pour construire un tel document, nous utiliserons une approche basée sur DOM. Vous pouvez en lire plus dans la section [Fondamentaux de l'API DOM](/pdf/net/basics-of-dom-api/).

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1.
1. Ajoutez une [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à l'objet document. Désormais, notre document contiendra une page.
1. Ajoutez une [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) à la Page.
1. Créez un [Fragment de Texte](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajoutez l'en-tête aux [Paragraphes](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Créez un [Fragment de Texte](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajoutez (la description) aux Paragraphes de la page.
1. Créez une table, ajoutez les propriétés de la table.
1. Ajoutez (la table) aux [Paragraphes](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Enregistrez un document "Complex.pdf".

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // Initialiser l'objet document
            Document document = new Document();
            // Ajouter une page
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // Ajouter une image
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Ajouter un en-tête
            var header = new TextFragment("Nouveaux itinéraires de ferry à l'automne 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Ajouter une description
            var descriptionText = "Les visiteurs doivent acheter leurs billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à demi-capacité et selon un horaire réduit. Attendez-vous à des files d'attente.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Ajouter un tableau
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("Départ de la ville");
            headerRow.Cells.Add("Départ de l'île");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

