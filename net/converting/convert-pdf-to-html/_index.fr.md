---
title: Convertir un PDF en HTML avec .NET
linktitle: Convertir un PDF en format HTML
type: docs
weight: 50
url: /net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir un fichier PDF en format HTML avec la bibliothèque Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Vue d'ensemble

Cet article explique comment **convertir un PDF en HTML en utilisant C#**. Il couvre ces sujets.

_Format_ : **HTML**
- [C# PDF en HTML](#csharp-pdf-to-html)
- [C# Convertir PDF en HTML](#csharp-pdf-to-html)
- [C# Comment convertir un fichier PDF en HTML](#csharp-pdf-to-html)

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir PDF en HTML

**Aspose.PDF pour .NET** offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et pour convertir des fichiers PDF en divers formats de sortie.
**Aspose.PDF pour .NET** offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie.

**Aspose.PDF pour .NET** prend en charge les fonctionnalités pour convertir un fichier PDF en HTML. Les principales tâches que vous pouvez accomplir avec la bibliothèque Aspose.PDF sont listées :

- convertir PDF en HTML ;
- diviser la sortie en HTML multi-pages ;
- spécifier le dossier pour stocker les fichiers SVG ;
- compresser les images SVG lors de la conversion ;
- spécifier le dossier des images ;
- créer des fichiers ultérieurs avec uniquement le contenu du corps ;
- rendu de texte transparent ;
- rendu des couches de documents PDF.

{{% alert color="success" %}}
**Essayez de convertir un PDF en HTML en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["PDF en HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en HTML avec l'application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF pour .NET fournit un code en deux lignes pour transformer un fichier PDF source en HTML.
Aspose.PDF pour .NET fournit un code en deux lignes pour transformer un fichier PDF source en HTML.

<a name="csharp-pdf-to-html"><strong>Étapes : Convertir PDF en HTML en C#</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.Html** en appelant la méthode **Document.Save()**.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Ouvrir le document PDF source
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Enregistrer le fichier au format de document MS
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### Diviser la sortie en HTML multi-page

Lors de la conversion d'un gros fichier PDF avec plusieurs pages en format HTML, la sortie apparaît comme une seule page HTML.
Lors de la conversion d'un fichier PDF volumineux avec plusieurs pages au format HTML, le résultat apparaît comme une seule page HTML.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Ouvrir le document PDF source
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Instancier l'objet HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Spécifier de diviser la sortie en plusieurs pages
htmlOptions.SplitIntoPages = true;

// Sauvegarder le document
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### Spécifier le dossier pour stocker les fichiers SVG

Lors de la conversion de PDF en HTML, il est possible de spécifier le dossier dans lequel les images SVG doivent être sauvegardées.
Lors de la conversion de PDF en HTML, il est possible de spécifier le dossier dans lequel les images SVG doivent être enregistrées.

```csharp
// Charger le fichier PDF
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// Instancier l'objet d'options de sauvegarde HTML
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Spécifier le dossier où les images SVG sont enregistrées lors de la conversion PDF en HTML
newOptions.SpecialFolderForSvgImages = dataDir;

// Enregistrer le fichier de sortie
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### Compression des images SVG lors de la conversion

Pour compresser les images SVG lors de la conversion de PDF en HTML, veuillez essayer d'utiliser le code suivant :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Créer HtmlSaveOption avec la fonctionnalité testée
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Compresser les images SVG s'il y en a
newOptions.CompressSvgGraphicsIfAny = true;
```

### Spécification du dossier des images

Nous pouvons également spécifier le dossier dans lequel les images seront enregistrées lors de la conversion de PDF en HTML :
Nous pouvons également spécifier le dossier dans lequel les images seront enregistrées lors de la conversion de PDF en HTML :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Créez HtmlSaveOption avec la fonctionnalité testée
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Spécifiez le dossier séparé pour enregistrer les images
newOptions.SpecialFolderForAllImages = dataDir;
```

### Créer des fichiers subséquents avec uniquement le contenu du corps

Récemment, on nous a demandé d'introduire une fonctionnalité où les fichiers PDF sont convertis en HTML et l'utilisateur peut obtenir uniquement le contenu de la balise `<body>` pour chaque page. Cela produirait un fichier avec CSS, détails `<html>`, `<head>` et toutes les pages dans d'autres fichiers juste avec le contenu `<body>`.

Pour répondre à cette exigence, une nouvelle propriété, HtmlMarkupGenerationMode, a été introduite dans la classe HtmlSaveOptions.

Avec le code simple suivant, vous pouvez diviser le HTML de sortie en pages.
Avec le simple extrait de code suivant, vous pouvez diviser le HTML de sortie en pages.

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// Ceci est le paramètre testé
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### Rendu de texte transparent

Dans le cas où le fichier PDF source/entrée contient des textes transparents ombragés par des images de premier plan, il pourrait y avoir des problèmes de rendu de texte. Ainsi, pour répondre à de tels scénarios, les propriétés SaveShadowedTextsAsTransparentTexts et SaveTransparentTexts peuvent être utilisées.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### Rendu des couches de documents PDF

Nous pouvons rendre les couches de documents PDF dans un élément de type couche séparé lors de la conversion de PDF en HTML :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// Instancier l'objet HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Spécifier pour rendre les couches de documents PDF séparément dans le HTML de sortie
htmlOptions.ConvertMarkedContentToLayers = true;

// Sauvegarder le document
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## Voir aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_ : **HTML**
- [C# PDF to HTML Code](#csharp-pdf-to-html)
- [C# PDF to HTML API](#csharp-pdf-to-html)
- [C# PDF to HTML Programmatically](#csharp-pdf-to-html)
- [C# PDF to HTML Library](#csharp-pdf-to-html)
- [C# Save PDF as HTML](#csharp-pdf-to-html)
- [C# Enregistrer PDF en tant que HTML](#csharp-pdf-to-html)
- [C# Générer HTML à partir de PDF](#csharp-pdf-to-html)
- [C# Créer HTML à partir de PDF](#csharp-pdf-to-html)
- [C# Convertisseur PDF en HTML](#csharp-pdf-to-html)
