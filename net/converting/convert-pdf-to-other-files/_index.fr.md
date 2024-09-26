---
title: Convertir PDF en EPUB, LaTeX, Texte, XPS en C#
linktitle: Convertir PDF en d'autres formats 
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: convertir, PDF, EPUB, LaTeX, Texte, XPS, C#
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichiers comme EPUB, LaTeX, Texte, XPS etc. en utilisant C# ou .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir un PDF en EPUB en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion de PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publication Électronique">EPUB</abbr>** est une norme de livre électronique gratuite et ouverte de l'International Digital Publishing Forum (IDPF).
**<abbr title="Publication Électronique">EPUB</abbr>** est un standard de livre électronique libre et ouvert de l'International Digital Publishing Forum (IDPF).
EPUB est conçu pour un contenu refluant, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un dispositif d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné comme un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Aspose.PDF pour .NET prend également en charge la fonctionnalité de conversion de documents PDF au format EPUB. Aspose.PDF pour .NET dispose d'une classe nommée EpubSaveOptions qui peut être utilisée comme second argument à la méthode [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index), pour générer un fichier EPUB.
Veuillez essayer d'utiliser le code suivant pour accomplir cette exigence avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Charger le document PDF
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Instancier les options de sauvegarde Epub
EpubSaveOptions options = new EpubSaveOptions();
// Spécifier la mise en page pour le contenu
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// Sauvegarder le document ePUB
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour .NET** prend en charge la conversion de PDF en LaTeX/TeX.
Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial et utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir un PDF en LaTeX/TeX en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF en LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF dispose de la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) qui fournit la propriété OutDirectoryPath pour sauvegarder les images temporaires pendant le processus de conversion.

Le fragment de code suivant montre le processus de conversion de fichiers PDF au format TEX avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Créer un objet Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// Instancier l'option de sauvegarde LaTex          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// Spécifier le répertoire de sortie
string pathToOutputDirectory = dataDir;

// Définir le chemin du répertoire de sortie pour l'objet option de sauvegarde
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// Sauvegarder le fichier PDF au format LaTex           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## Convertir PDF en Texte

**Aspose.PDF pour .NET** prend en charge la conversion de l'ensemble du document PDF et d'une seule page en fichier Texte.

### Convertir l'ensemble du document PDF en fichier Texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la méthode [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) de la classe [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

Le fragment de code suivant explique comment extraire les textes de toutes les pages.

```csharp
public static void ConvertPDFDocToTXT()
{
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Sauvegarder le texte extrait dans un fichier texte
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**Essayez de convertir Convertir PDF en Texte en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF en Texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez tester la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Texte avec App Gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF pour .NET. Vous devriez utiliser la méthode `Visit` de la classe `TextAbsorber` pour résoudre cette tâche.

Le code suivant explique comment extraire les textes des pages spécifiques.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // Sauvegarder le texte extrait dans un fichier texte
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## Convertir PDF en XPS

**Aspose.PDF pour .NET** offre la possibilité de convertir des fichiers PDF au format <abbr title="XML Paper Specification">XPS</abbr>. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF en format XPS avec C#.

{{% alert color="success" %}}
**Essayez de convertir un PDF en XPS en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification de papier XML par Microsoft Corporation. La Spécification de Papier XML (XPS), anciennement connue sous le nom de code Metro et englobant le concept marketing de Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) qui est utilisée comme second argument de la méthode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) pour générer le fichier XPS.
Pour convertir des fichiers PDF en XPS, Aspose.PDF utilise la classe [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) qui est utilisée comme second argument dans la méthode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) pour générer le fichier XPS.

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XPS.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Charger le document PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instancier les options de sauvegarde XPS
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// Sauvegarder le document XPS
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
