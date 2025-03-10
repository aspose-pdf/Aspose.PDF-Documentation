---
title: Convertir HTML en PDF dans .NET
linktitle: Convertir un fichier HTML en PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "La fonctionnalité de conversion dans Aspose.PDF for .NET permet la transformation transparente de documents HTML et MHTML en fichiers PDF de haute qualité. Avec des options de personnalisation avancées, les utilisateurs peuvent contrôler l'incorporation des polices, les requêtes multimédias et la gestion des ressources externes tout en s'assurant que les pages web ou les fichiers HTML locaux sont rendus avec précision au format PDF avec une flexibilité adaptée à leurs besoins spécifiques.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Aperçu 

Cet article explique comment **convertir HTML en PDF en utilisant C#**. Il couvre les sujets suivants.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_: **HTML**
- [C# HTML en PDF](#csharp-html-to-pdf)
- [C# Convertir HTML en PDF](#csharp-html-to-pdf)
- [C# Comment convertir HTML en PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [C# MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# Convertir MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# Comment convertir MHTML en PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [C# WebPage en PDF](#csharp-webpage-to-pdf)
- [C# Convertir WebPage en PDF](#csharp-webpage-to-pdf)
- [C# Comment convertir WebPage en PDF](#csharp-webpage-to-pdf)

## Conversion C# HTML en PDF

**Aspose.PDF for .NET** est une API de manipulation PDF qui vous permet de convertir n'importe quel document HTML existant en PDF de manière transparente. Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

Le code C# suivant montre comment convertir un document HTML en PDF.

<a name="csharp-html-to-pdf"><strong>Étapes : Convertir HTML en PDF en C#</strong></a>

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["HTML en PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion HTML en PDF utilisant l'application gratuite](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Conversion avancée de HTML en PDF

Le moteur de conversion HTML a plusieurs options qui nous permettent de contrôler le processus de conversion.

### Support des requêtes multimédias

Les requêtes multimédias sont une technique populaire pour fournir une feuille de style adaptée à différents appareils. Nous pouvons définir le type d'appareil en utilisant la propriété [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### Activer (désactiver) l'incorporation des polices

Les pages HTML utilisent souvent des polices (par exemple, des polices du dossier local, Google Fonts, etc.). Nous pouvons également contrôler l'incorporation des polices dans un document en utilisant la propriété [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### Gérer le chargement des ressources externes

Le moteur de conversion fournit un mécanisme qui vous permet de contrôler le chargement de certaines ressources associées au document HTML. La classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) a la propriété [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) avec laquelle nous pouvons définir le comportement du chargeur de ressources. Supposons que nous devions remplacer toutes les images PNG par une seule image `test.jpg` et remplacer l'URL externe par interne pour d'autres ressources. Pour ce faire, nous pouvons définir un chargeur personnalisé `SamePictureLoader` et pointer [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) vers ce nom.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## Convertir une page Web en PDF

La conversion d'une page Web est légèrement différente de la conversion d'un document HTML local. Pour convertir le contenu d'une page Web en format PDF, nous pouvons d'abord récupérer le contenu de la page HTML en utilisant une instance HttpClient, créer un objet Stream, passer le contenu à l'objet Document et rendre la sortie au format PDF.

Lors de la conversion d'une page Web hébergée sur un serveur Web en PDF :

<a name="csharp-webpage-to-pdf"><strong>Étapes : Convertir WebPage en PDF en C#</strong></a>

1. Lisez le contenu de la page en utilisant un objet HttpClient.
1. Instanciez l'objet [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) et définissez l'URL de base.
1. Initialisez un objet Document tout en passant l'objet stream.
1. Optionnellement, définissez la taille de la page et/ou l'orientation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Fournir des identifiants pour la conversion de page Web en PDF

Parfois, nous devons effectuer la conversion de fichiers HTML qui nécessitent une authentification et des privilèges d'accès, afin que seuls les utilisateurs authentiques puissent récupérer le contenu de la page. Cela inclut également le scénario où certaines ressources/données référencées à l'intérieur de HTML sont récupérées depuis un serveur externe qui nécessite une authentification et afin de répondre à cette exigence, la propriété [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) a été ajoutée à la classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). Le code suivant montre les étapes pour passer des identifiants afin de demander HTML et ses ressources respectives lors de la conversion d'un fichier HTML en PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Rendre tout le contenu HTML sur une seule page

Aspose.PDF for .NET offre la possibilité de rendre tout le contenu sur une seule page lors de la conversion d'un fichier HTML en format PDF. Par exemple, si vous avez un contenu HTML dont la taille de sortie est supérieure à une page, vous pouvez utiliser l'option pour rendre les données de sortie sur une seule page PDF. Pour utiliser cette option, la classe HtmlLoadOptions a été étendue par le drapeau IsRenderToSinglePage. Le code ci-dessous montre comment utiliser cette fonctionnalité.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### Rendre HTML avec des données SVG

Aspose.PDF for .NET offre la possibilité de convertir une page HTML en document PDF. Étant donné que HTML permet d'ajouter des éléments graphiques SVG en tant que balise dans la page, Aspose.PDF prend également en charge la conversion de telles données dans le fichier PDF résultant. Le code suivant montre comment convertir des fichiers HTML avec des balises graphiques SVG en documents PDF tagués.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## Convertir MHTML en PDF 

{{% alert color="success" %}}
**Essayez de convertir MHTML en PDF en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["MHTML en PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion MHTML en PDF utilisant l'application gratuite](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="Encapsulation MIME de documents HTML agrégés">MHTML</abbr>, abréviation de MIME HTML, est un format d'archive de page Web utilisé pour combiner des ressources qui sont généralement représentées par des liens externes (tels que des images, des animations Flash, des applets Java et des fichiers audio) avec du code HTML dans un seul fichier. Le contenu d'un fichier MHTML est encodé comme s'il s'agissait d'un message email HTML, en utilisant le type MIME multipart/related. Aspose.PDF for .NET peut convertir des fichiers HTML en format PDF et avec la sortie de Aspose.PDF for .NET 9.0.0, nous avons introduit une nouvelle fonctionnalité qui vous permet de convertir des fichiers MHTML en format PDF. Le code suivant montre comment convertir des fichiers MHTML en format PDF avec C# :

<a name="csharp-mhtml-to-pdf"><strong>Étapes : Convertir MHTML en PDF en C#</strong></a>

1. Créez une instance de la classe [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## Voir aussi 

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **HTML**
- [C# Code HTML en PDF](#csharp-html-to-pdf)
- [C# API HTML en PDF](#csharp-html-to-pdf)
- [C# HTML en PDF par programmation](#csharp-html-to-pdf)
- [C# Bibliothèque HTML en PDF](#csharp-html-to-pdf)
- [C# Enregistrer HTML en tant que PDF](#csharp-html-to-pdf)
- [C# Générer PDF à partir de HTML](#csharp-html-to-pdf)
- [C# Créer PDF à partir de HTML](#csharp-html-to-pdf)
- [C# Convertisseur HTML en PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [C# Code MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# API MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# MHTML en PDF par programmation](#csharp-mhtml-to-pdf)
- [C# Bibliothèque MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# Enregistrer MHTML en tant que PDF](#csharp-mhtml-to-pdf)
- [C# Générer PDF à partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Créer PDF à partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Convertisseur MHTML en PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [C# Code WebPage en PDF](#csharp-webpage-to-pdf)
- [C# API WebPage en PDF](#csharp-webpage-to-pdf)
- [C# WebPage en PDF par programmation](#csharp-webpage-to-pdf)
- [C# Bibliothèque WebPage en PDF](#csharp-webpage-to-pdf)
- [C# Enregistrer WebPage en tant que PDF](#csharp-webpage-to-pdf)
- [C# Générer PDF à partir de WebPage](#csharp-webpage-to-pdf)
- [C# Créer PDF à partir de WebPage](#csharp-webpage-to-pdf)
- [C# Convertisseur WebPage en PDF](#csharp-webpage-to-pdf)