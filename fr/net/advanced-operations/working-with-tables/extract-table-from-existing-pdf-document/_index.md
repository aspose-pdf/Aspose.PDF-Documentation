---
title: Extraire un tableau d'un document PDF
linktitle: Extraire un tableau
type: docs
weight: 20
url: /fr/net/extract-table-from-existing-pdf-document/
description: Aspose.PDF pour .NET permet de réaliser diverses manipulations avec les tableaux contenus dans votre document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraire un tableau d'un document PDF",
    "alternativeHeadline": "Comment extraire un tableau d'un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, dotnet, extraire tableau",
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
    "url": "/net/extract-table-from-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-table-from-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET permet de réaliser diverses manipulations avec les tableaux contenus dans votre document PDF."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Extraire une table de PDF

```csharp
public static void Extract_Table()
{
    // Charger le document PDF source
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(@"c:\tmp\the_worlds_cities_in_2018_data_booklet 7.pdf");           
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {
                    TextFragment textfragment = new TextFragment();
                    TextFragmentCollection textFragmentCollection = cell.TextFragments;
                    foreach (TextFragment fragment in textFragmentCollection)
                    {
                        string txt = "";
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            txt += seg.Text;
                        }
                        Console.WriteLine(txt);
                    }
                }
            }
        }
    }
}
```
## Extraire la bordure du tableau sous forme d'image

Les bordures de page sont des opérations de dessin de chemin. Par conséquent, la logique de traitement de Pdf->Html se contente simplement d'exécuter des instructions de dessin et de placer l'arrière-plan derrière le texte. Ainsi, pour répéter la logique, vous devez traiter manuellement les opérateurs de contenu et dessiner les graphiques vous-même. Veuillez également noter que le fragment de code suivant peut ne pas fonctionner correctement pour divers fichiers PDF, mais si vous rencontrez un problème, n'hésitez pas à contacter. Ce code a été développé pour des fichiers PDF spécifiques. Le fragment de code suivant montre les étapes pour extraire la bordure du tableau sous forme d'image d'un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document(dataDir + "input.pdf");

Stack graphicsState = new Stack();
System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap((int)doc.Pages[1].PageInfo.Width, (int)doc.Pages[1].PageInfo.Height);
System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
// La valeur par défaut de la matrice ctm est 1,0,0,1,0,0
System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
// Le système de coordonnées de System.Drawing est basé en haut à gauche, tandis que le système de coordonnées pdf est basé en bas à gauche, donc nous devons appliquer la matrice d'inversion
System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)doc.Pages[1].PageInfo.Height);
System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
{
    gr.SmoothingMode = SmoothingMode.HighQuality;
    graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

    // Traiter toutes les commandes de contenu
    foreach (Operator op in doc.Pages[1].Contents)
    {
        Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
        Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
        Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
        Aspose.Pdf.Operators.MoveTo opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
        Aspose.Pdf.Operators.LineTo opLineTo = op as Aspose.Pdf.Operators.LineTo;
        Aspose.Pdf.Operators.Re opRe = op as Aspose.Pdf.Operators.Re;
        Aspose.Pdf.Operators.EndPath opEndPath = op as Aspose.Pdf.Operators.EndPath;
        Aspose.Pdf.Operators.Stroke opStroke = op as Aspose.Pdf.Operators.Stroke;
        Aspose.Pdf.Operators.Fill opFill = op as Aspose.Pdf.Operators.Fill;
        Aspose.Pdf.Operators.EOFill opEOFill = op as Aspose.Pdf.Operators.EOFill;
        Aspose.Pdf.Operators.SetRGBColor opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
        Aspose.Pdf.Operators.SetRGBColorStroke opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

        if (opSaveState != null)
        {
            // Sauvegarder l'état précédent et pousser l'état actuel en haut de la pile
            graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opRestoreState != null)
        {
            // Jeter l'état actuel et restaurer le précédent
            graphicsState.Pop();
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opCtm != null)
        {
            System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
                (float)opCtm.Matrix.A,
                (float)opCtm.Matrix.B,
                (float)opCtm.Matrix.C,
                (float)opCtm.Matrix.D,
                (float)opCtm.Matrix.E,
                (float)opCtm.Matrix.F);

            // Multiplier la matrice actuelle avec la matrice d'état
            ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opMoveTo != null)
        {
            lastPoint = new System.Drawing.PointF((float)opMoveTo.X, (float)opMoveTo.Y);
        }
        else if (opLineTo != null)
        {
            System.Drawing.PointF linePoint = new System.Drawing.PointF((float)opLineTo.X, (float)opLineTo.Y);
            graphicsPath.AddLine(lastPoint, linePoint);

            lastPoint = linePoint;
        }
        else if (opRe != null)
        {
            System.Drawing.RectangleF re = new System.Drawing.RectangleF((float)opRe.X, (float)opRe.Y, (float)opRe.Width, (float)opRe.Height);
            graphicsPath.AddRectangle(re);
        }
        else if (opEndPath != null)
        {
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opRGBFillColor != null)
        {
            fillColor = opRGBFillColor.getColor();
        }
        else if (opRGBStrokeColor != null)
        {
            strokeColor = opRGBStrokeColor.getColor();
        }
        else if (opStroke != null)
        {
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.DrawPath(new System.Drawing.Pen(strokeColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opFill != null)
        {
            graphicsPath.FillMode = FillMode.Winding;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opEOFill != null)
        {
            graphicsPath.FillMode = FillMode.Alternate;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
    }
}
dataDir = dataDir + "ExtractBorder_out.png";
bitmap.Save(dataDir, ImageFormat.Png);
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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

