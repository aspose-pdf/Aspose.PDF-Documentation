---
title: Extraire un tableau d'un document PDF
linktitle: Extraire un tableau
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/extract-table-from-existing-pdf-document/
description: Aspose.PDF for .NET permet d'effectuer diverses manipulations avec les tableaux contenus dans votre document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Table from PDF Document",
    "alternativeHeadline": "Extract Tables Easily from PDF Files with .NET",
    "abstract": "Aspose.PDF for .NET introduit la capacité d'extraire des tableaux des documents PDF, rationalisant la manipulation des données et améliorant la productivité des développeurs. Cette fonctionnalité permet aux utilisateurs d'accéder et de gérer efficacement les données tabulaires au sein des PDF, en faisant un outil essentiel pour les applications nécessitant l'extraction et le traitement des données.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "837",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET permet d'effectuer diverses manipulations avec les tableaux contenus dans votre document PDF."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Extraire un tableau d'un PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_Table()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "the_worlds_cities_in_2018_data_booklet 7.pdf"))
    {          
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        var textfragment = new Aspose.Pdf.Text.TextFragment();
                        TextFragmentCollection textFragmentCollection = cell.TextFragments;
                        foreach (var fragment in textFragmentCollection)
                        {
                            string txt = "";
                            foreach (var seg in fragment.Segments)
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
}
```

## Extraire la bordure du tableau en tant qu'image

Les bordures de page sont des opérations de dessin de chemin. Par conséquent, la logique de traitement Pdf->Html effectue simplement des instructions de dessin et place l'arrière-plan derrière le texte. Donc, pour répéter la logique, vous devez traiter manuellement les opérateurs de contenu et dessiner vous-même les graphiques. Veuillez également noter que le code suivant peut ne pas fonctionner avec précision pour divers fichiers PDF, mais si vous rencontrez un problème, n'hésitez pas à nous contacter. Ce code a été développé pour des fichiers PDF spécifiques. Le code suivant montre les étapes pour extraire la bordure du tableau en tant qu'image d'un document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        Stack graphicsState = new Stack();
        using (var bitmap = new System.Drawing.Bitmap((int)document.Pages[1].PageInfo.Width, (int)document.Pages[1].PageInfo.Height))
        {
            System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
            // Default ctm matrix value is 1,0,0,1,0,0
            System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
            // System.Drawing coordinate system is top left based, while pdf coordinate system is low left based, so we have to apply the inversion matrix
            System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)document.Pages[1].PageInfo.Height);
            System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
            System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
            System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

            using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
            {
                gr.SmoothingMode = SmoothingMode.HighQuality;
                graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

                // Process all the contents commands
                foreach (var op in document.Pages[1].Contents)
                {
                    var opSaveState = op as Aspose.Pdf.Operators.GSave;
                    var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
                    var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
                    var opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
                    var opLineTo = op as Aspose.Pdf.Operators.LineTo;
                    var opRe = op as Aspose.Pdf.Operators.Re;
                    var opEndPath = op as Aspose.Pdf.Operators.EndPath;
                    var opStroke = op as Aspose.Pdf.Operators.Stroke;
                    var opFill = op as Aspose.Pdf.Operators.Fill;
                    var opEOFill = op as Aspose.Pdf.Operators.EOFill;
                    var opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
                    var opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

                    if (opSaveState != null)
                    {
                        // Save previous state and push current state to the top of the stack
                        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
                        lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    }
                    else if (opRestoreState != null)
                    {
                        // Throw away current state and restore previous one
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

                        // Multiply current matrix with the state matrix
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

            bitmap.Save(dataDir + "ExtractTableBorder_out.png", ImageFormat.Png);
        }
    }
}
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