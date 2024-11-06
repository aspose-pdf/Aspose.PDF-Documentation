---
title: Convertir d'autres formats de fichiers en PDF en .NET
linktitle: Convertir d'autres formats de fichiers en PDF
type: docs
weight: 80
url: fr/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir d'autres formats de fichiers tels que EPUB, MD, PCL, XPS, PS, XML et LaTeX en document PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Vue d'ensemble

Cet article explique comment **convertir divers autres types de formats de fichiers en PDF en utilisant C#**. Il couvre les sujets suivants.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_ : **EPUB**
- [C# EPUB en PDF](#csharp-convert-epub-to-pdf)
- [C# Convertir EPUB en PDF](#csharp-convert-epub-to-pdf)
- [C# Comment convertir un fichier EPUB en PDF](#csharp-convert-epub-to-pdf)

_Format_ : **Markdown**
- [C# Markdown en PDF](#csharp-convert-markdown-to-pdf)
- [C# Convertir Markdown en PDF](#csharp-convert-markdown-to-pdf)
- [C# Comment convertir un fichier Markdown en PDF](#csharp-convert-markdown-to-pdf)
- [C# Comment convertir un fichier Markdown en PDF](#csharp-convert-markdown-to-pdf)

_Format_: **MD**
- [C# MD en PDF](#csharp-convert-md-to-pdf)
- [C# Convertir MD en PDF](#csharp-convert-md-to-pdf)
- [C# Comment convertir un fichier MD en PDF](#csharp-convert-md-to-pdf)

_Format_: **PCL**
- [C# PCL en PDF](#csharp-convert-pcl-to-pdf)
- [C# Convertir PCL en PDF](#csharp-convert-pcl-to-pdf)
- [C# Comment convertir un fichier PCL en PDF](#csharp-convert-pcl-to-pdf)

_Format_: **Texte**
- [C# Texte en PDF](#csharp-convert-text-to-pdf)
- [C# Convertir Texte en PDF](#csharp-convert-text-to-pdf)
- [C# Comment convertir un fichier Texte en PDF](#csharp-convert-text-to-pdf)

_Format_: **TXT**
- [C# TXT en PDF](#csharp-convert-txt-to-pdf)
- [C# Convertir TXT en PDF](#csharp-convert-txt-to-pdf)
- [C# Comment convertir un fichier TXT en PDF](#csharp-convert-txt-to-pdf)

_Format_: **Texte Brut**
- [C# Texte Brut en PDF](#csharp-convert-plain-text-to-pdf)
- [C# Convertir Texte Brut en PDF](#csharp-convert-plain-text-to-pdf)
- [C# Comment convertir un fichier Texte Brut en PDF](#csharp-convert-plain-text-to-pdf)
- [C# Comment convertir un fichier texte brut en PDF](#csharp-convert-plain-text-to-pdf)

_Format_ : **TXT Préformaté**
- [C# Texte préformaté en PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Convertir texte préformaté en PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Comment convertir un fichier de texte préformaté en PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_Format_ : **Texte Pré**
- [C# Texte Pré en PDF](#csharp-convert-pre-text-to-pdf)
- [C# Convertir texte Pré en PDF](#csharp-convert-pre-text-to-pdf)
- [C# Comment convertir un fichier texte Pré en PDF](#csharp-convert-pre-text-to-pdf)

_Format_ : **XPS**
- [C# XPS en PDF](#csharp-convert-xps-to-pdf)
- [C# Convertir XPS en PDF](#csharp-convert-xps-to-pdf)
- [C# Comment convertir un fichier XPS en PDF](#csharp-convert-xps-to-pdf)

## Convertir EPUB en PDF

**Aspose.PDF pour .NET** vous permet de convertir facilement les fichiers EPUB au format PDF.

<abbr title="publication électronique">EPUB</abbr> (abréviation de publication électronique) est une norme de livre électronique gratuite et ouverte de l'International Digital Publishing Forum (IDPF).
<abbr title="publication électronique">EPUB</abbr> (abréviation de publication électronique) est une norme de livre électronique libre et ouverte de l'International Digital Publishing Forum (IDPF).

EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook. La version EPUB 3 est également approuvée par le Book Industry Study Group (BISG), une association commerciale de premier plan pour les meilleures pratiques standardisées, la recherche, l'information et les événements, pour l'emballage de contenu.

{{% alert color="success" %}}
**Essayez de convertir EPUB en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["EPUB en PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF EPUB en PDF avec application gratuite](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Étapes :</em> Convertir EPUB en PDF en C#</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Étapes :</em> Convertir EPUB en PDF en C#</strong></a>

1. Créez une instance de la classe [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions).
2. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) en mentionnant le nom de fichier source et les options.
3. Enregistrez le document avec le nom de fichier souhaité.

Le code suivant montre comment convertir des fichiers EPUB en format PDF avec C#.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

Vous pouvez également définir la taille de page pour la conversion. Pour définir une nouvelle taille de page, utilisez l'objet `SizeF` et passez-le au constructeur de [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## Convertir Markdown en PDF

**Cette fonctionnalité est prise en charge par la version 19.6 ou supérieure.**

{{% alert color="success" %}}
**Essayez de convertir Markdown en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["Markdown en PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion de Markdown en PDF avec Aspose.PDF App gratuite](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF pour .NET fournit la fonctionnalité pour créer un document PDF basé sur un fichier de données [Markdown](https://daringfireball.net/projects/markdown/syntax). Pour convertir le Markdown en PDF, vous devez initialiser le [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) en utilisant [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions).

Le fragment de code suivant montre comment utiliser cette fonctionnalité avec la bibliothèque Aspose.PDF :

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Étapes :</em> Convertir Markdown en PDF en C#</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Étapes :</em> Convertir Markdown en PDF en C#</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>Étapes :</em> Convertir MD en PDF en C#</strong></a>

1. Créez une instance de la classe [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/).
2. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) en mentionnant le nom de fichier source et les options.
3. Enregistrez le document avec le nom de fichier souhaité.

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Ouvrir le document Markdown
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// Enregistrer le document au format PDF
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## Convertir PCL en PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) est un langage d'imprimante développé par Hewlett-Packard pour accéder aux fonctionnalités standard de l'imprimante.
<abbr title="Langage de Commande d'Imprimante">PCL</abbr> (Langage de Commande d'Imprimante) est un langage d'imprimante développé par Hewlett-Packard pour accéder aux fonctionnalités standard de l'imprimante.

{{% alert color="success" %}}
**Essayez de convertir PCL en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PCL en PDF avec application gratuite](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Actuellement, seules les versions PCL5 et antérieures sont prises en charge**

<table>
    <thead>
        <tr>
            <th>
                Ensembles de commandes
            </th>
            <th>
                Prise en charge
            </th>
            <th>
                Exceptions
            </th>
            <th>
                Description
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Commandes de contrôle de travaux

        <tr>
            <td>
                Commandes de contrôle des travaux
            </td>
            <td>
                +
            </td>
            <td>
                Mode d'impression recto verso
            </td>
            <td>
                Contrôler le processus d'impression : nombre de copies, bac de sortie, impression recto/verso, décalages gauche et haut, etc.
            </td>
        </tr>
        <tr>
            <td>
                Commandes de contrôle de page
            </td>
            <td>
                +
            </td>
            <td>
                Commande de saut de perforation
            </td>
            <td>
                Spécifiez une taille de page, des marges, une orientation de page, des distances inter-lignes, inter-caractères, etc.
            </td>
        </tr>
        <tr>
            <td>
                Commandes de positionnement du curseur
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Spécifiez la position du curseur et, par conséquent, les origines du texte, des images matricielles ou vectorielles et des détails.
            </td>
        </tr>
```

<tr>
    <td>
        Spécifiez la position du curseur et, par conséquent, les origines des images de texte, raster ou vectorielles et des détails.
    </td>
</tr>
<tr>
    <td>
        Commandes de sélection de police
    </td>
    <td>
        +
    </td>
    <td>
        <ol>
            <li>Commande d'impression de données transparentes.</li>
            <li>Polices douces intégrées. Dans la version actuelle, au lieu de créer une police douce, notre bibliothèque sélectionne
                une police adéquate parmi les polices TrueType "dures" existantes installées sur une machine cible. <br/>
                L'adéquation est définie par le rapport largeur/hauteur.<br/>
                Cette fonctionnalité ne fonctionne que pour les polices Bitmap et TrueType et ne garantit pas
                que le texte imprimé avec la police douce sera pertinent par rapport à celui d'un fichier source.<br/>
                Car les codes de caractères dans la police douce peuvent ne pas correspondre à ceux par défaut.
            </li>
            <li>Jeux de symboles définis par l'utilisateur.</li>
        </ol>
    </td>
</tr>
```

<li>Jeux de symboles définis par l'utilisateur.</li>
</ol>
</td>
<td>
    Permet le chargement de polices douces (intégrées) à partir du fichier PCL et leur gestion en mémoire.
</td>
</tr>
<tr>
<td>
    Commandes graphiques raster
</td>
<td>
    +
</td>
<td>
    Noir et blanc uniquement
</td>
<td>
    Permet le chargement d'images raster à partir du fichier PCL en mémoire, spécifiez les paramètres raster. <br
        > tels que largeur, hauteur, type de compression, résolution, etc.
</td>
</tr>
<tr>
<td>
    Commandes de couleur
</td>
<td>
    +
</td>
<td>
    &nbsp;
</td>
<td>
    Permet la coloration pour tous les objets imprimables.
</td>
</tr>
<tr>
<td>
    Commandes du modèle d'impression
```
```
                 Commandes d'impression de modèle
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permet de remplir du texte, des images raster et des zones rectangulaires avec des motifs raster prédéfinis et <br>
                des motifs définis par l'utilisateur, spécifie le mode de transparence pour les motifs et
                l'image raster source. <br> Les motifs prédéfinis sont le hachurage, le croisillonnage
                et les ombrages.
            </td>
        </tr>
        <tr>
            <td>
                Commandes de remplissage de zone rectangulaire
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permet la création et le remplissage de zones rectangulaires avec des motifs.
            </td>
        </tr>
        <tr>
            <td>
                Commandes graphiques vectorielles HP-GL/2
            </td>
            <td>
                +
            </td>
            <td>
                Commande vectorielle écranée (SV), Commande de mode de transparence (TR), Commande de données transparentes (TD), RO
```
Les commandes Screened Vector Command (SV), Transparency Mode Command (TR), Transparent Data Command (TD), RO (Rotate Coordinate System), Scalable or Bitmap Fonts Command (SB), Character Slant Command (SL) et Extra Space (ES) ne sont pas implémentées et les commandes DV (Define Variable Text Path) sont réalisées en version bêta.

Permet de charger des images vectorielles HP-GL/2 à partir d'un fichier PCL en mémoire. L'image vectorielle a son origine dans le coin inférieur gauche de la zone imprimable, peut être mise à l'échelle, translatée, tournée et rognée.
L'image vectorielle peut contenir du texte, comme des étiquettes, et des figures géométriques telles que rectangle, cercle, ellipse, ligne, arc, courbe de Bézier et figures complexes composées des simples.
Les figures fermées incluant les lettres des étiquettes peuvent être remplies avec un remplissage uni ou un motif vectoriel. Le motif peut être un hachurage, un croisillon, un ombrage, un raster défini par l'utilisateur, un hachurage PCL ou un croisillon PCL.

hachage, hachage croisé, ombrage, raster défini par l'utilisateur, hachage ou hachage croisé PCL et PCL défini par l'utilisateur. Les motifs PCL sont des rasters. Les étiquettes peuvent être individuellement tournées, mises à l'échelle et dirigées dans quatre directions : haut, bas, gauche et droite. Les directions gauche et droite impliquent un arrangement des lettres l'une après l'autre. Les directions haut et bas impliquent un arrangement des lettres l'une sous l'autre.
```

Macros
```

―
```

Permet de charger une séquence de commandes PCL en mémoire et d'utiliser cette séquence plusieurs fois, par exemple, pour imprimer l'en-tête d'une page ou définir un formatage pour un ensemble de pages.
```

Texte Unicode
```

―
```

### Conversion d'un fichier PCL en format PDF

Pour permettre la conversion de PCL à PDF, Aspose.PDF dispose de la classe [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) qui est utilisée pour initialiser l'objet LoadOptions.
```

<table>
    <tbody>
        <tr>
            <td>
                Autoriser l'impression de caractères non ASCII. Non implémenté en raison de l'absence de fichiers exemples avec du texte Unicode
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                Réalisé uniquement en version Beta en raison du manque de fichiers de test. Les polices intégrées ne sont également pas
                prises en charge. L'extension JetReady n'est pas prise en charge car il est
                impossible d'avoir la spécification JetReady.
            </td>
            <td>
                Format de fichier binaire.
            </td>
        </tr>
    </tbody>
</table>
```
Pour permettre la conversion de PCL en PDF, Aspose.PDF dispose de la classe [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) qui est utilisée pour initialiser l'objet LoadOptions.

Le code suivant montre le processus de conversion d'un fichier PCL en format PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>Étapes :</em> Convertir PCL en PDF en C#</strong></a>

1. Créer une instance de la classe [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/).
2. Créer une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) avec le nom de fichier source mentionné et les options.
3. Enregistrer le document avec le nom de fichier souhaité.

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

Vous pouvez également surveiller la détection des erreurs pendant le processus de conversion.
Vous pouvez également surveiller la détection des erreurs pendant le processus de conversion.

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### Problèmes connus

1. L'origine des chaînes de texte et des images peut légèrement différer de celles dans un fichier PCL source si la direction d'impression n'est pas de 0°. Il en va de même pour les images vectorielles si le système de coordonnées du tracé vectoriel est pivoté (commande RO précédée).
1. L'origine des étiquettes dans les images vectorielles peut différer de celles dans un fichier PCL source si les étiquettes sont influencées par une séquence de commandes : Origine de l'étiquette (LO), Définir le chemin du texte variable (DV), Direction absolue (DI) ou Direction relative (DR).
1. Si le fichier PCL analysé contient des polices Intellifont ou Universal, une exception sera lancée, car les polices Intellifont et Universal ne sont pas du tout prises en charge.
1. Si le fichier PCL analysé contient des commandes de macros, le résultat de l'analyse différera fortement du fichier source, car les commandes de macros ne sont pas prises en charge.

## Convertir du texte en PDF

**Aspose.PDF pour .NET** prend en charge la fonctionnalité de conversion de fichiers texte simples et pré-formatés en format PDF.

Convertir du texte en PDF signifie ajouter des fragments de texte à la page PDF. En ce qui concerne les fichiers texte, nous traitons 2 types de texte : le pré-formatage (par exemple, 25 lignes de 80 caractères chacune) et le texte non formaté (texte brut). Selon nos besoins, nous pouvons contrôler nous-mêmes cette addition ou la confier aux algorithmes de la bibliothèque.

{{% alert color="success" %}}
**Essayez de convertir du TEXTE en PDF en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.
Aspose.PDF pour .NET vous présente une application gratuite en ligne ["Texte vers PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion de texte en PDF avec l'application gratuite Aspose.PDF](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

### Convertir un fichier texte en PDF

Dans le cas d'un fichier texte simple, nous pouvons utiliser la technique suivante :

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>Étapes :</em> Convertir du texte en PDF en C#</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>Étapes :</em> Convertir TXT en PDF en C#</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>Étapes :</em> Convertir du texte simple en PDF en C#</strong></a>

1. Utilisez un _TextReader_ pour lire l'intégralité du texte;
2.
2.
3. Créez un nouvel objet de [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/) et passez l'objet _TextReader_ à son constructeur ;
4. Ajoutez l'objet _TextFragment_ comme paragraphe dans la collection _Paragraphs_. Si la quantité de texte dépasse la taille de la page, l'algorithme de la bibliothèque ajoute automatiquement des pages supplémentaires ;
5. Utilisez la méthode **Save** de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) ;

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Lire le fichier texte source
TextReader tr = new StreamReader(dataDir + "log.txt");

// Instancier un objet Document en appelant son constructeur vide
Document pdfDocument = new Document();

// Ajouter une nouvelle page dans la collection Pages du Document
Page page = pdfDocument.Pages.Add();

// Créer une instance de TextFragmet et passer le texte de l'objet reader à son constructeur en argument
TextFragment text = new TextFragment(tr.ReadToEnd());

// Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
page.Paragraphs.Add(text);

// Sauvegarder le fichier PDF résultant
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### Convertir un fichier texte préformaté en PDF

Convertir un texte préformaté est similaire à du texte brut mais nécessite des actions supplémentaires telles que la configuration des marges, du type de police et de la taille. Évidemment, la police doit être à espacement fixe (par exemple Courier New).

Suivez ces étapes pour convertir un texte préformaté en PDF avec C# :

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>Étapes :</em> Convertir un texte préformaté en PDF en C#</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>Étapes :</em> Convertir un TXT préformaté en PDF en C#</strong></a>

1. Lire l'intégralité du texte sous forme de tableau de chaînes ;
2. Instanciez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) et ajoutez une nouvelle page dans la collection [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/) ;
Dans ce cas, l'algorithme de la bibliothèque ajoute également des pages supplémentaires, mais nous pouvons contrôler ce processus nous-mêmes.
L'exemple suivant montre comment convertir un fichier texte préformaté (80x25) en document PDF avec une taille de page A4.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // Lire le fichier texte comme un tableau de chaînes
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // Instancier un objet Document en appelant son constructeur vide
    Document pdfDocument= new Document();

    // Ajouter une nouvelle page dans la collection Pages du Document
    Page page = pdfDocument.Pages.Add();

    // Définir les marges gauche et droite pour une meilleure présentation
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // vérifier si la ligne contient le caractère "saut de page"
        // voir https://fr.wikipedia.org/wiki/Saut_de_page
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // Créer une instance de TextFragment et
            // passer la ligne à son
            // constructeur comme argument
            TextFragment text = new TextFragment(line);

            // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
            page.Paragraphs.Add(text);
        }
    }

    // Enregistrer le fichier PDF résultant
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## Convertir XPS en PDF

**Aspose.PDF pour .NET** prend en charge la fonctionnalité de conversion des fichiers <abbr title="XML Paper Specification">XPS</abbr> au format PDF. Consultez cet article pour résoudre vos tâches.

Le type de fichier XPS est principalement associé à la spécification de papier XML par Microsoft Corporation. La spécification de papier XML (XPS), anciennement connue sous le nom de code Metro et englobant le concept de marketing de Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans son système d'exploitation Windows.

{{% alert color="primary" %}}

Le format de fichier est essentiellement un fichier XML zippé qui est principalement utilisé pour la distribution et le stockage. Il est très difficile à modifier et principalement mis en œuvre par Microsoft.

{{% /alert %}}

Pour convertir XPS en PDF avec Aspose.PDF pour .NET, nous avons introduit une classe nommée [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) qui est utilisée pour initialiser un objet [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).
Pour convertir un XPS en PDF avec Aspose.PDF pour .NET, nous avons introduit une classe nommée [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) qui est utilisée pour initialiser un objet [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).

{{% alert color="primary" %}}

Dans XP et Windows 7, vous devriez trouver une imprimante XPS pré-installée si vous regardez dans le Panneau de configuration puis Imprimantes. Pour créer ces fichiers, vous pouvez utiliser cette imprimante comme périphérique de sortie. Dans Windows 7, vous devriez pouvoir simplement double-cliquer sur le fichier pour l'ouvrir dans un visualiseur XPS. Vous pouvez également télécharger le visualiseur XPS sur le site web de Microsoft.

{{% /alert %}}

Le fragment de code suivant montre le processus de conversion d'un fichier XPS en format PDF avec C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>Étapes :</em> Convertir XPS en PDF en C#</strong></a>

1. Créez une instance de la classe [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/).
2.
3. Enregistrez le document au format PDF avec le nom de fichier souhaité.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instancier l'objet LoadOption en utilisant l'option de chargement XPS
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// Créer un objet document
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// Enregistrer le document PDF résultant
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**Essayez de convertir le format XPS en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion XPS en PDF avec application gratuite](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
{{% /alert %}}

## Convertir PostScript en PDF

**Aspose.PDF pour .NET** prend en charge la conversion des fichiers PostScript en format PDF. Une des fonctionnalités d'Aspose.PDF est que vous pouvez définir un ensemble de dossiers de polices à utiliser pendant la conversion.

Pour convertir un fichier PostScript en format PDF, Aspose.PDF pour .NET propose la classe [PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions) qui est utilisée pour initialiser l'objet LoadOptions. Cet objet peut ensuite être passé comme argument au constructeur de l'objet Document, ce qui aidera le moteur de rendu PDF à déterminer le format du document source.

Le fragment de code suivant peut être utilisé pour convertir un fichier PostScript en format PDF avec Aspose.PDF pour .NET :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Créez une nouvelle instance de PsLoadOptions
PsLoadOptions options = new PsLoadOptions();
// Ouvrez le document .ps avec les options de chargement créées
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// Enregistrez le document
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
De plus, vous pouvez définir un ensemble de dossiers de polices qui seront utilisés lors de la conversion :

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## Convertir XML en PDF

Le format XML est utilisé pour stocker des données structurées. Il existe plusieurs méthodes pour convertir le XML en PDF avec Aspose.PDF :

1. Transformer n'importe quelle donnée XML en HTML en utilisant XSLT et convertir le HTML en PDF comme décrit ci-dessous
1. Générer un document XML en utilisant le schéma XSD de Aspose.PDF
1. Utiliser un document XML basé sur la norme XSL-FO

{{% alert color="success" %}}
**Essayez de convertir XML en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), où vous pouvez essayer d'explorer les fonctionnalités et la qualité de son fonctionnement.

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de XML à PDF avec une application gratuite](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

## Convertir XSL-FO en PDF

La conversion de fichiers XSL-FO en PDF peut être réalisée en utilisant la technique traditionnelle d'Aspose.PDF - instancier l'objet [Document](https://reference.aspose.com/page/net/aspose.page/document) avec [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Mais parfois, vous pouvez rencontrer une structure de fichier incorrecte. Dans ce cas, le convertisseur XSL-FO permet de définir la stratégie de gestion des erreurs. Vous pouvez choisir `ThrowExceptionImmediately`, `TryIgnore` ou `InvokeCustomHandler`.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // Instancier l'objet XslFoLoadOption
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // Définir la stratégie de gestion des erreurs
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Créer l'objet Document
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## Convertir LaTeX/TeX en PDF

Le format de fichier LaTeX est un format de fichier texte avec des balises dans la dérivée LaTeX de la famille de langages TeX et LaTeX est un format dérivé du système TeX. LaTeX (ˈleɪtɛk/lay-tek ou lah-tek) est un système de préparation de documents et un langage de balisage de documents. Il est largement utilisé pour la communication et la publication de documents scientifiques dans de nombreux domaines, y compris les mathématiques, la physique et l'informatique. Il joue également un rôle important dans la préparation et la publication de livres et d'articles contenant des matériaux multilingues complexes, tels que le sanskrit et l'arabe, y compris les éditions critiques. LaTeX utilise le programme de composition typographique TeX pour formater sa sortie, et est lui-même écrit dans le langage de macro TeX.

{{% alert color="success" %}}
**Essayez de convertir LaTeX/TeX en PDF en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["LaTex en PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion LaTeX/TeX en PDF avec application gratuite](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
[![Conversion Aspose.PDF LaTeX/TeX en PDF avec application gratuite](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF pour .NET prend en charge la fonctionnalité de conversion des fichiers TeX en format PDF et pour accomplir cette exigence, l'espace de noms Aspose.Pdf a une classe nommée [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions) qui offre les capacités de charger les fichiers LaTex et de rendre le résultat en format PDF en utilisant la [classe Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Le fragment de code suivant montre le processus de conversion d'un fichier LaTex en format PDF avec C#.

```csharp
public static void ConvertTeXtoPDF()
{
    // Instancier l'objet d'option de chargement Latex
    TeXLoadOptions options = new TeXLoadOptions();
    // Créer un objet Document
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // Enregistrer le résultat dans un fichier PDF
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
