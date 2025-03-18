---
title: Rechercher et Obtenir du Texte des Pages d'un PDF
linktitle: Rechercher et Obtenir du Texte
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/search-and-get-text-from-pdf/
description: Découvrez comment rechercher et récupérer du texte à partir d'un fichier PDF en .NET en utilisant Aspose.PDF pour l'analyse et l'extraction de texte.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Search and Get Text from Pages of PDF",
    "alternativeHeadline": "Search and Extract Text from PDF Pages",
    "abstract": "Aspose.PDF for .NET permet aux utilisateurs de rechercher et d'extraire efficacement du texte de toutes les pages d'un document PDF. Cette fonctionnalité utilise la classe TextFragmentAbsorber pour localiser des phrases ou segments de texte spécifiés, avec un support avancé pour les expressions régulières, permettant une récupération et une manipulation précises du texte. Idéal pour les développeurs, cette fonctionnalité améliore les capacités de gestion des documents PDF en simplifiant les processus d'extraction de texte.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2762",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Cet article explique comment utiliser divers outils pour rechercher et obtenir un texte de Aspose.PDF for .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Rechercher et Obtenir du Texte de Toutes les Pages d'un Document PDF

La classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) vous permet de trouver du texte correspondant à une phrase particulière, sur toutes les pages d'un document PDF. Pour rechercher du texte dans l'ensemble du document, vous devez appeler la méthode Accept de la collection Pages. La méthode [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) prend un objet TextFragmentAbsorber comme paramètre, qui retourne une collection d'objets TextFragment. Vous pouvez parcourir tous les fragments et obtenir leurs propriétés comme Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

Le code suivant vous montre comment rechercher du texte sur toutes les pages.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

Si vous devez rechercher du texte à l'intérieur d'une page PDF particulière, veuillez spécifier le numéro de page de la collection de pages de l'instance Document et appeler la méthode Accept sur cette page (comme indiqué dans la ligne de code ci-dessous).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

### Rechercher à travers une liste de phrases dans un TextFragmentAbsorber

La bibliothèque C# ne peut passer qu'une seule phrase au TextFragmentAbsorber, mais depuis la version 24.2 d'Aspose.PDF, elle a implémenté un nouvel algorithme pour rechercher la liste d'algorithmes de recherche.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

Le code suivant recherche des motifs spécifiques tels que des numéros de document, des mots-clés et des numéros de fichier dans un document PDF en utilisant des expressions régulières. Il charge le PDF, applique la recherche et récupère les résultats correspondants pour un traitement ultérieur.

## Rechercher et Obtenir des Segments de Texte de Toutes les Pages d'un Document PDF

Pour rechercher des segments de texte sur toutes les pages, vous devez d'abord obtenir les objets TextFragment du document. TextFragmentAbsorber vous permet de trouver du texte correspondant à une phrase particulière, sur toutes les pages d'un document PDF. Pour rechercher du texte dans l'ensemble du document, vous devez appeler la méthode Accept de la collection Pages. La méthode Accept prend un objet TextFragmentAbsorber comme paramètre, qui retourne une collection d'objets TextFragment. Une fois la TextFragmentCollection récupérée du document, vous devez parcourir cette collection et obtenir la TextSegmentCollection de chaque objet TextFragment. Après cela, vous pouvez obtenir toutes les propriétés de l'objet TextSegment individuel. Le code suivant vous montre comment rechercher des segments de texte sur toutes les pages.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextPage.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Figure");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            foreach (var textSegment in textFragment.Segments)
            {
                Console.WriteLine("Text : {0} ", textSegment.Text);
                Console.WriteLine("Position : {0} ", textSegment.Position);
                Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
                Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
                Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
                Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
                Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
                Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
                Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
                Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
            }
        }
    }
}
```

Pour rechercher et obtenir des TextSegments d'une page particulière d'un PDF, vous devez spécifier l'index de la page particulière lors de l'appel de la méthode Accept(..). Veuillez consulter les lignes de code suivantes.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

## Rechercher et Obtenir du Texte de toutes les pages en utilisant des Expressions Régulières

TextFragmentAbsorber vous aide à rechercher et à récupérer du texte, de toutes les pages, basé sur une expression régulière. Tout d'abord, vous devez passer une expression régulière au constructeur de TextFragmentAbsorber comme phrase. Après cela, vous devez définir la propriété TextSearchOptions de l'objet TextFragmentAbsorber. Cette propriété nécessite un objet TextSearchOptions et vous devez passer true comme paramètre à son constructeur lors de la création de nouveaux objets. Comme vous souhaitez récupérer le texte correspondant de toutes les pages, vous devez appeler la méthode Accept de la collection Pages. TextFragmentAbsorber retourne une TextFragmentCollection contenant tous les fragments correspondant aux critères spécifiés par l'expression régulière. Le code suivant vous montre comment rechercher et obtenir du texte de toutes les pages basé sur une expression régulière.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        textFragmentAbsorber.TextSearchOptions = textSearchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFragmentAbsorberCtor()
{
    Aspose.Pdf.Text.TextFragmentAbsorber textFragmentAbsorber;
    // In order to search exact match of a word, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"\bWord\b", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search a string in either upper case or lowercase, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("(?i)Line", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

    // Find match of search string and get anything after the string till line break
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?i)the ((.)*)");

    // Please use following regular expression to find text following to the regex match
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?<=word).*");

    // In order to search Hyperlink/URL's inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
}
```

## Rechercher du Texte basé sur Regex et Ajouter un Hyperlien

Si vous souhaitez ajouter un hyperlien sur une phrase de texte basée sur une expression régulière, trouvez d'abord toutes les phrases correspondant à cette expression régulière particulière en utilisant TextFragmentAbsorber et ajoutez un hyperlien sur ces phrases.

Pour trouver une phrase et ajouter un hyperlien dessus :

1. Passez l'expression régulière comme paramètre au constructeur de TextFragmentAbsorber.
2. Créez un objet TextSearchOptions qui spécifie si l'expression régulière est utilisée ou non.
3. Obtenez les phrases correspondantes dans TextFragments.
4. Parcourez les correspondances pour obtenir leurs dimensions rectangulaires, changez la couleur de premier plan en bleu (optionnel - pour donner l'apparence d'un hyperlien) et créez un lien en utilisant la méthode CreateWebLink(..) de la classe PdfContentEditor.
5. Enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.
Le code suivant vous montre comment rechercher du texte à l'intérieur d'un fichier PDF en utilisant une expression régulière et en ajoutant des hyperliens sur les correspondances.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create absorber object to find all instances of the input search phrase
    var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}");

    // Enable regular expression search
    absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

    // Create the editor
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");

        // Accept the absorber for the page
        editor.Document.Pages[1].Accept(absorber);

        int[] dashArray = { };
        String[] LEArray = { };
        System.Drawing.Color blue = System.Drawing.Color.Blue;

        // Loop through the fragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
                (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
                (int)Math.Round(textFragment.Rectangle.Height + 1));
            Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
            editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
            editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
                (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
        }

        // Save PDF document
        editor.Save(dataDir + "SearchTextAndAddHyperlink_out.pdf");
    }
}
```

## Rechercher et dessiner un rectangle autour de chaque TextFragment

Aspose.PDF for .NET prend en charge la fonctionnalité de recherche et d'obtention des coordonnées de chaque caractère ou fragment de texte. Donc, pour être certain des coordonnées renvoyées pour chaque caractère, nous pouvons envisager de mettre en surbrillance (ajouter un rectangle) autour de chaque caractère.

Dans le cas d'un paragraphe de texte, vous pouvez envisager d'utiliser une expression régulière pour déterminer la rupture de paragraphe et dessiner un rectangle autour de celui-ci. Veuillez consulter le code suivant. Le code suivant obtient les coordonnées de chaque caractère et crée un rectangle autour de chaque caractère.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        foreach (var textFragment in textAbsorber.TextFragments)
        {
            DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
        }   
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```

## Mettre en Évidence chaque caractère dans un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de rechercher du texte dans un document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF for .NET prend en charge la fonctionnalité de recherche et d'obtention des coordonnées de chaque caractère ou fragment de texte. Ainsi, pour être certain des coordonnées retournées pour chaque caractère, nous pouvons envisager de mettre en surbrillance (ajouter un rectangle) autour de chaque caractère. Le code suivant obtient les coordonnées de chaque caractère et crée un rectangle autour de chaque caractère.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndHighlight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    int resolution = 150;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        using (MemoryStream stream = new MemoryStream())
        {
            var conv = new Aspose.Pdf.Facades.PdfConverter(document);
            conv.Resolution = new Aspose.Pdf.Devices.Resolution(resolution, resolution);
            conv.GetNextImage(stream, System.Drawing.Imaging.ImageFormat.Png);

            using (var bmp = System.Drawing.Bitmap.FromStream(stream))
            {

                using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
                {
                    float scale = resolution / 72f;
                    gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

                    for (int i = 0; i < document.Pages.Count; i++)
                    {
                        var page = document.Pages[1];
                        // Create TextAbsorber object to find all words
                        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");
                        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
                        page.Accept(textFragmentAbsorber);
                        // Get the extracted text fragments
                        var textFragmentCollection = textFragmentAbsorber.TextFragments;
                        // Loop through the fragments
                        foreach (var textFragment in textFragmentCollection)
                        {
                            if (i == 0)
                            {
                                gr.DrawRectangle(
                                    System.Drawing.Pens.Yellow,
                                    (float)textFragment.Position.XIndent,
                                    (float)textFragment.Position.YIndent,
                                    (float)textFragment.Rectangle.Width,
                                    (float)textFragment.Rectangle.Height);

                                for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                                {
                                    var segment = textFragment.Segments[segNum];

                                    for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                                    {
                                        var characterInfo = segment.Characters[charNum];

                                        Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                                        Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                            "   TextFragment URY = " + textFragment.Rectangle.URY);

                                        gr.DrawRectangle(
                                            System.Drawing.Pens.Black,
                                            (float)characterInfo.Rectangle.LLX,
                                            (float)characterInfo.Rectangle.LLY,
                                            (float)characterInfo.Rectangle.Width,
                                            (float)characterInfo.Rectangle.Height);
                                    }

                                    gr.DrawRectangle(
                                        System.Drawing.Pens.Green,
                                        (float)segment.Rectangle.LLX,
                                        (float)segment.Rectangle.LLY,
                                        (float)segment.Rectangle.Width,
                                        (float)segment.Rectangle.Height);
                                }
                            }
                        }
                    }
                }
                
                // Save result
                bmp.Save(dataDir + "HighlightCharacterInPDF_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
    }
}
```

## Ajouter et Rechercher du Texte Caché

Parfois, nous voulons ajouter du texte caché dans un document PDF, puis rechercher du texte caché et utiliser sa position pour un traitement ultérieur. Pour votre commodité, Aspose.PDF for .NET fournit ces capacités. Vous pouvez ajouter du texte caché lors de la génération du document. De plus, vous pouvez trouver du texte caché en utilisant TextFragmentAbsorber. Pour ajouter du texte caché, définissez TextState.Invisible sur 'true' pour le texte ajouté. TextFragmentAbsorber trouve tout le texte qui correspond au motif (si spécifié). C'est le comportement par défaut qui ne peut pas être changé. Pour vérifier si le texte trouvé est réellement invisible, la propriété TextState.Invisible peut être utilisée. Le code ci-dessous montre comment utiliser cette fonctionnalité.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndSearchText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var frag1 = new Aspose.Pdf.Text.TextFragment("This is common text.");
        var frag2 = new Aspose.Pdf.Text.TextFragment("This is invisible text.");

        //Set text property - invisible
        frag2.TextState.Invisible = true;

        page.Paragraphs.Add(frag1);
        page.Paragraphs.Add(frag2);
        // Save PDF document
        document.Save(dataDir + "CreateAndSearchText_out.pdf");
    }

    // Search text in the document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateAndSearchText_out.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        foreach (var fragment in absorber.TextFragments)
        {
            //Do something with fragments
            Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
            fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
        }
    }
}
```

## Recherche de Texte Avec Regex .NET

Aspose.PDF for .NET fournit la capacité de rechercher des documents en utilisant l'option Regex standard de .NET. Le TextFragmentAbsorber peut être utilisé à cette fin comme montré dans l'exemple de code ci-dessous.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create Regex object to find all words
    var regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf"))
    {

        // Get a particular page
        var page = document.Pages[1];

        // Create TextAbsorber object to find all instances of the input regex
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regex);
        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

        // Accept the absorber for the page
        page.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine(textFragment.Text);
        }
    }
}
```

## Recherche de texte en gras

Aspose.PDF for .NET permet aux utilisateurs de rechercher des documents en utilisant les propriétés de style de police. Le TextFragmentAbsorber peut être utilisé à cet effet, comme montré dans l'exemple de code ci-dessous.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf"))
    {
        // Create TextFragmentAbsorber object to extract text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // Accept the absorber for all document
        textFragmentAbsorber.Visit(document);

        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            // Get the text properties of the text fragment
            var textState = textFragment.TextState;
            // Check if text is bold
            if (textState.FontStyle == FontStyles.Bold)
            {
                // Print the text from the text fragment
                Console.WriteLine("Text :- " + textFragment.Text);
            }
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