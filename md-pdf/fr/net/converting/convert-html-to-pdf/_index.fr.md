---
title: Convertir HTML en PDF en .NET
linktitle: Convertir un fichier HTML en PDF
type: docs
weight: 40
url: /net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## Aperçu 

Cet article explique comment **convertir HTML en PDF en utilisant C#**. Il couvre les sujets suivants.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_ : **HTML**
- [C# HTML en PDF](#csharp-html-to-pdf)
- [C# Convertir HTML en PDF](#csharp-html-to-pdf)
- [C# Comment convertir HTML en PDF](#csharp-html-to-pdf)

_Format_ : **MHTML**
- [C# MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# Convertir MHTML en PDF](#csharp-mhtml-to-pdf)
- [C# Comment convertir MHTML en PDF](#csharp-mhtml-to-pdf)

_Format_ : **Page Web**
- [C# Page Web en PDF](#csharp-webpage-to-pdf)
- [C# Convertir Page Web en PDF](#csharp-webpage-to-pdf)
- [C# Comment convertir une Page Web en PDF](#csharp-webpage-to-pdf)

## Conversion de HTML en PDF en C#
## Conversion de HTML en PDF en C#

**Aspose.PDF pour .NET** est une API de manipulation de PDF qui vous permet de convertir tout document HTML existant en PDF de manière transparente. Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

Le code C# suivant montre comment convertir un document HTML en PDF.

<a name="csharp-html-to-pdf"><strong>Étapes : Convertir HTML en PDF en C#</strong></a>

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose vous présente l'application gratuite en ligne ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

Aspose vous présente une application gratuite en ligne ["HTML en PDF"](https://products.aspose.app/html/fr/conversion/html-to-pdf), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF HTML en PDF utilisant l'application gratuite](html.png)](https://products.aspose.app/html/fr/conversion/html-to-pdf)
{{% /alert %}}

## Conversion avancée de HTML en PDF

Le moteur de conversion HTML dispose de plusieurs options qui nous permettent de contrôler le processus de conversion.

### Support des requêtes média

Les requêtes média sont une technique populaire pour fournir une feuille de style adaptée à différents appareils. Nous pouvons définir le type d'appareil en utilisant la propriété [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // définir le mode Impression ou Écran
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### Activer (désactiver) l'incorporation de polices

Les pages HTML utilisent souvent des polices (par exemple, des polices d'un dossier local, Google Fonts, etc.). Nous pouvons également contrôler l'incorporation de polices dans un document en utilisant la propriété [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // Désactivation de l'incorporation des polices
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### Gérer le chargement des ressources externes

Le moteur de conversion fournit un mécanisme qui vous permet de contrôler le chargement de certaines ressources associées au document HTML.
La classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) possède la propriété [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) avec laquelle nous pouvons définir le comportement du chargeur de ressources.
La classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) possède la propriété [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) avec laquelle nous pouvons définir le comportement du chargeur de ressources.
Supposons que nous devons remplacer toutes les images PNG par une image unique `test.jpg` et remplacer l'URL externe par une URL interne pour d'autres ressources.
Pour ce faire, nous pouvons définir un chargeur personnalisé `SamePictureLoader` et diriger [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) vers ce nom.

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument = new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            //Définir le type MIME
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## Convertir une page Web en PDF

Convertir une page Web est légèrement différent de convertir un document HTML local. Pour convertir le contenu d'une page Web en format PDF, nous pouvons d'abord récupérer le contenu de la page HTML en utilisant une instance HttpClient, créer un objet Stream, passer les contenus à l'objet Document et rendre la sortie en format PDF.

Lors de la conversion d'une page Web hébergée sur un serveur web en PDF :

<a name="csharp-webpage-to-pdf"><strong>Étapes : Convertir une page Web en PDF en C#</strong></a>

1. Lire le contenu de la page en utilisant un objet HttpClient.
1. Instancier l'objet [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) et définir l'URL de base.
1. Initialiser un objet Document en passant l'objet stream.
1. Facultativement, définir la taille de la page et/ou l'orientation.

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://en.wikipedia.org/wiki/Aspose_API";
    // Définir la taille de la page A3 et l'orientation Paysage;   
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Fournir des identifiants pour la conversion de pages Web en PDF

Parfois, nous devons effectuer la conversion de fichiers HTML qui nécessitent une authentification et des privilèges d'accès, afin que seuls les utilisateurs authentiques puissent récupérer le contenu de la page. Cela inclut également le scénario où certaines ressources/données référencées à l'intérieur de l'HTML sont extraites d'un serveur externe qui nécessite une authentification et, pour répondre à cette exigence, la propriété [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) est ajoutée à la classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). Le morceau de code suivant montre les étapes pour passer des identifiants à la requête HTML et ses ressources respectives lors de la conversion du fichier HTML en PDF.

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Rendre tout le contenu HTML sur une seule page

Aspose.PDF pour .NET offre la capacité de rendre tout le contenu sur une seule page lors de la conversion d'un fichier HTML en format PDF. Par exemple, si vous avez un contenu HTML dont la taille de sortie est supérieure à une page, vous pouvez utiliser l'option de rendu des données de sortie sur une seule page PDF. Pour utiliser cette option, la classe HtmlLoadOptions a été étendue par le drapeau IsRenderToSinglePage. Le fragment de code ci-dessous montre comment utiliser cette fonctionnalité.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Initialiser les options HTMLLoadSave
HtmlLoadOptions options = new HtmlLoadOptions();
// Définir la propriété de rendu sur une seule page
options.IsRenderToSinglePage = true;
// Charger le document
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// Sauvegarder
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### Rendre le HTML avec des données SVG
### Rendu HTML avec données SVG

Aspose.PDF pour .NET permet de convertir une page HTML en document PDF. Étant donné que HTML permet d'ajouter un élément graphique SVG comme balise dans la page, Aspose.PDF prend également en charge la conversion de ces données dans le fichier PDF résultant. Le fragment de code suivant montre comment convertir des fichiers HTML avec des balises graphiques SVG en documents PDF balisés.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Définir le chemin du fichier d'entrée
string inFile = dataDir + "HTMLSVG.html";
// Définir le chemin du fichier de sortie
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// Initialiser HtmlLoadOptions
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// Initialiser l'objet Document
Document pdfDocument = new Document(inFile, options);
// sauvegarder
pdfDocument.Save(outFile);
```

## Convertir MHTML en PDF

{{% alert color="success" %}}
**Essayez de convertir MHTML en PDF en ligne**
**Essayez de convertir MHTML en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion MHTML en PDF utilisant l'application gratuite](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="Encapsulation MIME de documents HTML agrégés">MHTML</abbr>, abrégé pour MIME HTML, est un format d'archive de page web utilisé pour combiner des ressources qui sont généralement représentées par des liens externes (tels que des images, des animations Flash, des applets Java et des fichiers audio) avec du code HTML dans un seul fichier.
<abbr title="Encapsulation MIME de documents HTML agrégés">MHTML</abbr>, abréviation de MIME HTML, est un format d'archive de page web utilisé pour combiner des ressources qui sont généralement représentées par des liens externes (tels que des images, des animations Flash, des applets Java et des fichiers audio) avec du code HTML dans un seul fichier.

<a name="csharp-mhtml-to-pdf"><strong>Étapes : Convertir MHTML en PDF en C#</strong></a>

1. Créez une instance de la classe [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## Voir aussi

Cet article couvre également ces sujets.
Cet article couvre également ces sujets.

_Format_ : **HTML**
- [Code C# HTML vers PDF](#csharp-html-to-pdf)
- [API C# HTML vers PDF](#csharp-html-to-pdf)
- [C# HTML vers PDF Programmation](#csharp-html-to-pdf)
- [Bibliothèque C# HTML vers PDF](#csharp-html-to-pdf)
- [C# Enregistrer HTML comme PDF](#csharp-html-to-pdf)
- [C# Générer un PDF à partir de HTML](#csharp-html-to-pdf)
- [C# Créer un PDF à partir de HTML](#csharp-html-to-pdf)
- [Convertisseur C# HTML vers PDF](#csharp-html-to-pdf)

_Format_ : **MHTML**
- [Code C# MHTML vers PDF](#csharp-mhtml-to-pdf)
- [API C# MHTML vers PDF](#csharp-mhtml-to-pdf)
- [C# MHTML vers PDF Programmation](#csharp-mhtml-to-pdf)
- [Bibliothèque C# MHTML vers PDF](#csharp-mhtml-to-pdf)
- [C# Enregistrer MHTML comme PDF](#csharp-mhtml-to-pdf)
- [C# Générer un PDF à partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Créer un PDF à partir de MHTML](#csharp-mhtml-to-pdf)
- [Convertisseur C# MHTML vers PDF](#csharp-mhtml-to-pdf)

_Format_ : **WebPage**
- [Code C# WebPage vers PDF](#csharp-webpage-to-pdf)
- [API C# WebPage vers PDF](#csharp-webpage-to-pdf)
- [C# WebPage vers PDF Programmation](#csharp-webpage-to-pdf)
- [C# Page Web en PDF Programmatically](#csharp-webpage-to-pdf)
- [C# Bibliothèque pour convertir une Page Web en PDF](#csharp-webpage-to-pdf)
- [C# Enregistrer une Page Web en tant que PDF](#csharp-webpage-to-pdf)
- [C# Générer un PDF à partir d'une Page Web](#csharp-webpage-to-pdf)
- [C# Créer un PDF à partir d'une Page Web](#csharp-webpage-to-pdf)
- [C# Convertisseur de Page Web en PDF](#csharp-webpage-to-pdf)
