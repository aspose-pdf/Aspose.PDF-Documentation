---
title: Extraire du texte d'un PDF C#
linktitle: Extraire du texte d'un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/extract-text-from-all-pdf/
description: Cet article décrit différentes manières d'extraire du texte de documents PDF en utilisant Aspose.PDF en C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "Découvrez la nouvelle fonctionnalité puissante dans Aspose.PDF for .NET qui permet aux développeurs d'extraire facilement du texte de documents PDF. Cette fonctionnalité prend en charge l'extraction de toutes les pages ou de régions spécifiques, s'adapte aux mises en page multi-colonnes et permet même de récupérer le texte surligné en quelques lignes de code. Améliorez vos capacités de traitement de documents et rationalisez l'extraction de contenu avec cet outil polyvalent.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Extraire du texte de toutes les pages d'un document PDF

L'extraction de texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF for .NET permet d'extraire du texte de toutes les pages d'un document PDF. Vous devez créer un objet de la classe **TextAbsorber**. Après cela, ouvrez le PDF en utilisant la classe **Document** et appelez la méthode **Accept** de la collection **Pages**. La classe **TextAbsorber** absorbe le texte du document et le renvoie dans la propriété **Text**. Le code suivant vous montre comment extraire du texte de toutes les pages d'un document PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Appelez la méthode **Accept** sur une page particulière de l'objet Document. L'index est le numéro de page particulier à partir duquel le texte doit être extrait.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extraire du texte des pages en utilisant le dispositif de texte

Vous pouvez utiliser la classe **TextDevice** pour extraire du texte d'un fichier PDF. **TextDevice** utilise **TextAbsorber** dans son implémentation, donc, en fait, ils font la même chose mais **TextDevice** est juste implémenté pour unifier l'approche "Device" pour extraire quoi que ce soit de l'image de la page, du dispositif de page, etc. **TextAbsorber** peut extraire du texte de la page, de l'ensemble du PDF ou de XForm, ce **TextAbsorber** est plus universel.

### Extraire du texte de toutes les pages

Les étapes suivantes et le code montrent comment extraire du texte d'un PDF en utilisant le dispositif de texte.

1. Créez un objet de la classe Document avec le fichier PDF d'entrée spécifié.
1. Créez un objet de la classe TextDevice.
1. Utilisez l'objet de la classe TextExtractOptions pour spécifier les options d'extraction.
1. Utilisez la méthode Process de la classe TextDevice pour convertir le contenu en texte.
1. Enregistrez le texte dans le fichier de sortie.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## Extraire du texte d'une région particulière de la page

La classe **TextAbsorber** fournit la capacité d'extraire du texte d'une page particulière ou de toutes les pages d'un document PDF. Cette classe renvoie le texte extrait dans la propriété **Text**. Cependant, si nous avons besoin d'extraire du texte d'une région particulière de la page, nous pouvons utiliser la propriété **Rectangle** de **TextSearchOptions**. La propriété Rectangle prend un objet Rectangle comme valeur et en utilisant cette propriété, nous pouvons spécifier la région de la page à partir de laquelle nous devons extraire le texte.

La méthode **Accept** d'une page est appelée pour extraire le texte. Créez des objets des classes **Document** et **TextAbsorber**. Appelez la méthode **Accept** sur la page individuelle, en tant qu'index **Page**, de l'objet **Document**. L'**Index** est le numéro de page particulier à partir duquel le texte doit être extrait. Vous pouvez obtenir le texte à partir de la propriété **Text** de la classe **TextAbsorber**. Le code suivant vous montre comment extraire du texte d'une page individuelle.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extraire du texte en fonction des colonnes

Un fichier PDF peut comprendre des éléments tels que du texte, des images, des annotations, des pièces jointes, des graphiques, etc., et Aspose.PDF for .NET offre la fonctionnalité d'ajouter ainsi que de manipuler tous ces éléments. Cette API est remarquable lorsqu'il s'agit d'ajouter et d'extraire du texte d'un document PDF et nous pouvons rencontrer un scénario où un document PDF est composé de plus d'une colonne (document multi-colonnes) et nous devons extraire le contenu de la page tout en respectant la même mise en page, alors Aspose.PDF for .NET est le bon choix pour accomplir cette exigence. Une approche consiste à réduire la taille de la police des contenus à l'intérieur du document PDF et ensuite effectuer l'extraction de texte. Le code suivant montre les étapes pour réduire la taille du texte et ensuite essayer d'extraire du texte d'un document PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### Deuxième approche - Utilisation de ScaleFactor

Dans cette nouvelle version, nous avons également introduit plusieurs améliorations dans **TextAbsorber** et dans le mécanisme de formatage de texte interne. Ainsi, maintenant lors de l'extraction de texte en utilisant le mode 'Pur', vous pouvez spécifier l'option ScaleFactor et cela peut être une autre approche pour extraire du texte d'un document PDF multi-colonnes en plus de l'approche mentionnée ci-dessus. Ce facteur d'échelle peut être défini pour ajuster la grille qui est utilisée pour le mécanisme de formatage de texte interne lors de l'extraction de texte. Spécifier les valeurs de ScaleFactor entre 1 et 0.1 (y compris 0.1) a le même effet que la réduction de la police.

Spécifier les valeurs de ScaleFactor entre 0.1 et -0.1 est traité comme une valeur nulle, mais cela fait que l'algorithme calcule automatiquement le facteur d'échelle nécessaire lors de l'extraction de texte. Le calcul est basé sur la largeur moyenne des glyphes de la police la plus populaire sur la page, mais nous ne pouvons pas garantir qu'aucune chaîne de colonne extraite n'atteigne le début de la colonne suivante. Veuillez noter que si la valeur de ScaleFactor n'est pas spécifiée, la valeur par défaut de 1.0 sera utilisée. Cela signifie qu'aucun redimensionnement ne sera effectué. Si la valeur de ScaleFactor spécifiée est supérieure à 10 ou inférieure à -0.1, la valeur par défaut de 1.0 sera utilisée.

Nous proposons l'utilisation de l'auto-redimensionnement (ScaleFactor = 0) lors du traitement d'un grand nombre de fichiers PDF pour l'extraction de contenu texte. Ou définissez manuellement une réduction redondante de la largeur de la grille (environ ScaleFactor = 0.5). Cependant, vous ne devez pas déterminer si le redimensionnement est nécessaire pour des documents concrets ou non. Si vous définissez une réduction redondante de la largeur de la grille pour le document (qui n'en a pas besoin), le contenu texte extrait restera entièrement adéquat. Veuillez consulter le code suivant.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

Veuillez noter qu'il n'y a pas de correspondance directe entre le nouveau ScaleFactor et l'ancien coefficient de réduction manuelle de la police. Cependant, par défaut, l'algorithme prend en compte la valeur de la taille de police qui a déjà été réduite pour certaines raisons internes. Par exemple, réduire la taille de la police de 10 à 7 a le même effet que de définir un facteur d'échelle à 5/8 (= 0.625).

{{% /alert %}}

## Extraire le texte surligné d'un document PDF

Dans divers scénarios d'extraction de texte d'un document PDF, vous pouvez avoir besoin d'extraire uniquement le texte surligné du document PDF. Afin de mettre en œuvre cette fonctionnalité, nous avons ajouté les méthodes **TextMarkupAnnotation.GetMarkedText()** et **TextMarkupAnnotation.GetMarkedTextFragments()** dans l'API. Vous pouvez extraire le texte surligné d'un document PDF en filtrant **TextMarkupAnnotation** et en utilisant les méthodes mentionnées. Le code suivant montre comment vous pouvez extraire le texte surligné d'un document PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## Accéder aux éléments de fragment de texte et de segment à partir de XML

Parfois, nous avons besoin d'accéder aux éléments **TextFragment** ou **TextSegment** lors du traitement de documents PDF générés à partir de XML. Aspose.PDF for .NET fournit un accès à ces éléments par nom. Le code ci-dessous montre comment utiliser cette fonctionnalité.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```