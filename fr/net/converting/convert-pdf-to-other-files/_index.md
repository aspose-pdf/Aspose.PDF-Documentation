---
title: Convertir PDF en EPUB, LaTeX, Texte, XPS en C#
linktitle: Convertir PDF en d'autres formats
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichier comme EPUB, LaTeX, Texte, XPS, etc. en utilisant C# ou .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to EPUB, LaTeX, Text, XPS in C#",
    "alternativeHeadline": "Add PDF format conversion to EPUB, LaTeX, Text, XPS in C#",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante qui permet la conversion transparente de fichiers PDF en divers formats, y compris EPUB, LaTeX, Texte, XPS et Markdown. Cette fonctionnalité améliore l'accessibilité et l'utilisabilité des documents en permettant aux développeurs d'intégrer sans effort diverses conversions de formats de fichiers dans leurs applications C#, répondant ainsi à un public plus large et optimisant le contenu pour différentes plateformes.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1419",
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
    "url": "/net/convert-pdf-to-other-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-other-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec l'application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publication Électronique">EPUB</abbr>** est une norme de livre électronique gratuite et ouverte de l'International Digital Publishing Forum (IDPF). Les fichiers ont l'extension .epub.
EPUB est conçu pour un contenu reflowable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Aspose.PDF for .NET prend également en charge la fonctionnalité de conversion de documents PDF au format EPUB. Aspose.PDF for .NET a une classe nommée EpubSaveOptions qui peut être utilisée comme deuxième argument de la méthode [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) pour générer un fichier EPUB.
Veuillez essayer d'utiliser le code suivant pour accomplir cette exigence avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoEPUB()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToEPUB.pdf"))
    {
        // Instantiate Epub Save options
        EpubSaveOptions options = new EpubSaveOptions();
        // Specify the layout for contents
        options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;

        // Save ePUB document
        document.Save(dataDir + "PDFToEPUB_out.epub", options);
    }
}
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF for .NET** prend en charge la conversion de PDF en LaTeX/TeX.
Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial et utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec l'application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF a la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) qui fournit la propriété OutDirectoryPath pour enregistrer des images temporaires pendant le processus de conversion.

Le code suivant montre le processus de conversion de fichiers PDF au format TEX avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTeX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf"))
    {
        // Instantiate LaTex save option          
        LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

        // Specify the output directory
        string pathToOutputDirectory = dataDir;

        // Set the output directory path for save option object
        saveOptions.OutDirectoryPath = pathToOutputDirectory;

        // Save PDF document into LaTex format           
        document.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
    }
}
```

## Convertir PDF en Texte

**Aspose.PDF for .NET** prend en charge la conversion de l'ensemble du document PDF et d'une seule page en un fichier texte.

### Convertir l'ensemble du document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la méthode [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) de la classe [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

Le code suivant explique comment extraire les textes de toutes les pages.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        ta.Visit(document);

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt",ta.Text);
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir PDF en Texte en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Texte avec l'application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF for .NET. Vous devez utiliser la méthode `Visit` de la classe `TextAbsorber` pour résoudre cette tâche.

Le code suivant explique comment extraire les textes de pages particulières.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        var pages = new [] {1, 3, 4};
        foreach (var page in pages)
        {
            ta.Visit(document.Pages[page]);
        }
    
        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", ta.Text);
    }
}
```

## Convertir PDF en XPS

**Aspose.PDF for .NET** offre la possibilité de convertir des fichiers PDF en format <abbr title="XML Paper Specification">XPS</abbr>. Essayez d'utiliser le code présenté pour convertir des fichiers PDF en format XPS avec C#.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec l'application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification XML Paper de Microsoft Corporation. La spécification XML Paper (XPS), anciennement connue sous le nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF a la classe [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) qui est utilisée comme deuxième argument de la méthode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) pour générer le fichier XPS.

Depuis la version 24.2, Aspose.PDF a mis en œuvre la conversion de PDF consultables en XPS tout en gardant le texte sélectionnable dans le XPS résultant. Pour préserver le texte, il est nécessaire de définir la propriété XpsSaveOptions.SaveTransparentTexts sur true.

Le code suivant montre le processus de conversion d'un fichier PDF en format XPS.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoXPS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var xpsOptions = new XpsSaveOptions
        {
            SaveTransparentTexts = true
        };

        // Save XPS document
        document.Save(dataDir + "PDFtoXPS_out.xps", xpsOptions);
    }
}
```

## Convertir PDF en Markdown

**Aspose.PDF for .NET** offre la possibilité de convertir des fichiers PDF en format <abbr title="Markdown">MD</abbr>. Essayez d'utiliser le code présenté pour convertir des fichiers PDF en format MD avec C#.

Markdown est un langage de balisage léger conçu pour représenter le formatage de texte brut avec une lisibilité humaine maximale et une lisibilité machine pour des langages de publication avancés.

### Optimiser l'utilisation des images par le convertisseur PDF en Markdown

Vous pouvez remarquer que dans les répertoires avec des images, le nombre d'images est inférieur au nombre d'images dans les fichiers PDF.

Puisque le fichier markdown ne peut pas définir la taille de l'image, sans l'option MarkdownSaveOptions.UseImageHtmlTag, le même type d'images avec des tailles différentes est enregistré comme différent.

Pour l'option activée MarkdownSaveOptions.UseImageHtmlTag, des images uniques seront enregistrées, qui sont mises à l'échelle dans le document par la balise img.

Le code ouvre un document PDF, configure les paramètres pour le convertir en un fichier Markdown (en enregistrant toutes les images dans le dossier nommé "images"), et enregistre le fichier Markdown résultant dans le chemin de sortie spécifié.

Le code suivant montre le processus de conversion d'un fichier PDF en format MD.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        }
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options   
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

### Convertir PDF en MobiXml

MobiXML est un format de livre électronique populaire, conçu pour être utilisé sur des plateformes mobiles.
Le code suivant explique comment convertir un document PDF en fichier MobiXML.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void ConvertPdfToMobiXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToXML.pdf"))
    {
        // Save PDF document in XML format
        document.Save(dataDir + "PDFToXML_out.xml", Aspose.Pdf.SaveFormat.MobiXml);
    }
}
```