---
title: Convert various Images formats to PDF in .NET
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Convertir divers formats d'images tels que BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF et SVG en PDF en utilisant C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Vue d'ensemble

Cet article explique comment convertir divers formats d'images en PDF en utilisant C#. Il couvre ces sujets.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_ : **BMP**
- [C# BMP en PDF](#csharp-bmp-to-pdf)
- [C# Convertir BMP en PDF](#csharp-bmp-to-pdf)
- [C# Comment convertir une image BMP en PDF](#csharp-bmp-to-pdf)

_Format_ : **CGM**
- [C# CGM en PDF](#csharp-cgm-to-pdf)
- [C# Convertir CGM en PDF](#csharp-cgm-to-pdf)
- [C# Comment convertir une image CGM en PDF](#csharp-cgm-to-pdf)

_Format_ : **DICOM**
- [C# DICOM en PDF](#csharp-dicom-to-pdf)
- [C# Convertir DICOM en PDF](#csharp-dicom-to-pdf)
- [C# Comment convertir une image DICOM en PDF](#csharp-dicom-to-pdf)
- [C# Comment convertir une image DICOM en PDF](#csharp-dicom-to-pdf)

_Format_ : **EMF**
- [C# EMF en PDF](#csharp-emf-to-pdf)
- [C# Convertir EMF en PDF](#csharp-emf-to-pdf)
- [C# Comment convertir une image EMF en PDF](#csharp-emf-to-pdf)

_Format_ : **GIF**
- [C# GIF en PDF](#csharp-gif-to-pdf)
- [C# Convertir GIF en PDF](#csharp-gif-to-pdf)
- [C# Comment convertir une image GIF en PDF](#csharp-gif-to-pdf)

_Format_ : **JPG**
- [C# JPG en PDF](#csharp-jpg-to-pdf)
- [C# Convertir JPG en PDF](#csharp-jpg-to-pdf)
- [C# Comment convertir une image JPG en PDF](#csharp-jpg-to-pdf)

_Format_ : **PNG**
- [C# PNG en PDF](#csharp-png-to-pdf)
- [C# Convertir PNG en PDF](#csharp-png-to-pdf)
- [C# Comment convertir une image PNG en PDF](#csharp-png-to-pdf)

_Format_ : **SVG**
- [C# SVG en PDF](#csharp-svg-to-pdf)
- [C# Convertir SVG en PDF](#csharp-svg-to-pdf)
- [C# Comment convertir une image SVG en PDF](#csharp-svg-to-pdf)

_Format_ : **TIFF**
- [C# TIFF en PDF](#csharp-tiff-to-pdf)
- [C# Convertir TIFF en PDF](#csharp-tiff-to-pdf)
- [C# Comment convertir une image TIFF en PDF](#csharp-tiff-to-pdf)
- [C# Comment convertir une image TIFF en PDF](#csharp-tiff-to-pdf)

Autres sujets abordés par cet article
- [Voir aussi](#see-also)


## Conversions d'images en PDF en C#

**Aspose.PDF pour .NET** vous permet de convertir différents formats d'images en fichiers PDF. Notre bibliothèque montre des extraits de code pour convertir les formats d'images les plus populaires, tels que - BMP, CGM, DICOM, EMF, JPG, PNG, SVG et TIFF.

## Convertir BMP en PDF

Convertissez des fichiers BMP en document PDF en utilisant la bibliothèque **Aspose.PDF pour .NET**.

<abbr title="Fichier d'image Bitmap">BMP</abbr> sont des fichiers ayant l'extension .BMP représentant des fichiers d'images Bitmap utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant du périphérique (DIB).
Vous pouvez convertir des BMP en fichiers PDF avec l'API Aspose.PDF pour .NET. Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Étapes : Convertir BMP en PDF en C#</strong></a>

1.
1.
2. Charger l'image **BMP** d'entrée.
3. Enfin, enregistrez le fichier PDF de sortie.

Le code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant C#:

```csharp
//Initialiser un document PDF vide
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Charger le fichier image BMP exemple
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Enregistrer le document PDF de sortie
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Essayez de convertir BMP en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion BMP en PDF utilisant l'application gratuite](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM en PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> est une extension de fichier pour un format de métafichier graphique informatique couramment utilisé dans les applications de CAO (conception assistée par ordinateur) et de graphiques de présentation.
<abbr title="Métafichier de graphiques informatiques">CGM</abbr> est une extension de fichier pour un format de métafichier de graphiques informatiques couramment utilisé dans les applications de CAO (conception assistée par ordinateur) et de graphiques de présentation.

Vérifiez le prochain extrait de code pour convertir des fichiers CGM en format PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Étapes : Convertir CGM en PDF en C#</strong></a>

1. Créez une instance de la classe [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions).
2. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le nom de fichier source mentionné et les options.
3. Enregistrez le document avec le nom de fichier désiré.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## Convertir DICOM en PDF

<abbr title="Imagerie numérique et communications en médecine">DICOM</abbr> est le standard de l'industrie médicale pour la création, le stockage, la transmission et la visualisation d'images médicales numériques et de documents de patients examinés.
Le format <abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est la norme de l'industrie médicale pour la création, le stockage, la transmission et la visualisation d'images médicales numériques et de documents de patients examinés.

**Aspose.PDF pour .NET** vous permet de convertir des images DICOM et SVG, mais pour des raisons techniques, pour ajouter des images, vous devez spécifier le type de fichier à ajouter au PDF :

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Étapes : Convertir DICOM en PDF en C#</strong></a>

1. Créez un objet de la classe Image.
2. Ajoutez l'image à la collection Paragraphs d'une page.
3. Spécifiez la propriété [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype).
4. Spécifiez le chemin ou la source du fichier.
    - Si une image se trouve à un emplacement sur le disque dur, spécifiez l'emplacement du chemin à l'aide de la propriété Image.File.
    - Si une image est placée dans un MemoryStream, passez l'objet contenant l'image à la propriété Image.ImageStream.

Le code suivant montre comment convertir des fichiers DICOM en format PDF avec Aspose.PDF.
L'extrait de code suivant montre comment convertir des fichiers DICOM en format PDF avec Aspose.PDF.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Convertir les images DICOM en PDF en utilisant la classe Image
public static void ConvertDICOMtoPDF()
{
    // Instancier l'objet Document
    Document pdfDocument = new Document();

    // Ajouter une page à la collection de pages du document
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Enregistrer la sortie au format PDF
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**Essayez de convertir DICOM en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion DICOM en PDF avec application gratuite](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
[![Conversion Aspose.PDF de DICOM à PDF avec une application gratuite](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF en PDF

<abbr title="Format de métafichier amélioré">EMF</abbr>EMF stocke des images graphiques de manière indépendante du dispositif. Les métafichiers EMF comprennent des enregistrements de longueur variable dans l'ordre chronologique qui peuvent restituer l'image stockée après analyse sur tout dispositif de sortie. De plus, vous pouvez convertir une image EMF en PDF en suivant les étapes ci-dessous :

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Étapes : Convertir EMF en PDF en C#</strong></a>

1. Tout d'abord, initialisez l'objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Chargez le fichier image **EMF**.
3. Ajoutez l'image EMF chargée à une Page.
4. Enregistrez le document PDF.

De plus, le fragment de code suivant montre comment convertir un EMF en PDF avec C# dans votre extrait de code .NET :

```csharp
// Initialiser un nouveau document PDF
var doc = new Document();

// Spécifier le chemin du fichier image EMF d'entrée
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// Spécifier les propriétés de dimension de la page
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

// Enregistrer le document PDF de sortie
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**Essayez de convertir EMF en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion EMF en PDF utilisant l'application gratuite](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir GIF en PDF

Convertissez des fichiers GIF en document PDF en utilisant la bibliothèque **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> permet de stocker des données compressées sans perte de qualité dans un format ne dépassant pas 256 couleurs. Le format GIF, indépendant du matériel, a été développé en 1987 (GIF87a) par CompuServe pour la transmission d'images bitmap sur des réseaux.
Vous pouvez convertir des fichiers GIF en PDF avec l'API Aspose.PDF for .NET. Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images GIF :

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Étapes : Convertir GIF en PDF en C#</strong></a>

1.
1.
2. Charger l'image **GIF** d'entrée.
3. Enfin, enregistrez le fichier PDF de sortie.

Le code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant C# :

```csharp
//Initialiser un document PDF vide
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Charger un fichier image GIF exemple
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Enregistrer le document PDF de sortie
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Essayez de convertir GIF en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion GIF en PDF utilisant l'application gratuite](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Convertir JPG en PDF

Nul besoin de se demander comment convertir JPG en PDF, car la bibliothèque **Apose.PDF pour .NET** a la meilleure solution.
Pas besoin de se demander comment convertir un JPG en PDF, car la bibliothèque **Apose.PDF pour .NET** a la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour .NET en suivant les étapes :

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Étapes : Convertir JPG en PDF en C#</strong></a>

1. Initialiser un objet de la classe [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Ajouter une nouvelle page au document PDF.
3. Charger l'image **JPG** et l'ajouter au paragraphe.
4. Sauvegarder le PDF de sortie.

Le fragment de code ci-dessous montre comment convertir une image JPG en PDF en utilisant C# :

```csharp
// Charger le fichier JPG d'entrée
String path = dataDir + "Aspose.jpg";

// Initialiser un nouveau document PDF
Document doc = new Document();

// Ajouter une page vide dans le document vide
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Ajouter l'image sur une page
page.Paragraphs.Add(image);

// Sauvegarder le fichier PDF de sortie
doc.Save(dataDir + "ImagetoPDF.pdf");
```

Ensuite, vous pouvez voir comment convertir une image en PDF avec **la même hauteur et largeur que la page**.
Ensuite, vous pouvez voir comment convertir une image en PDF avec la **même hauteur et largeur de page**.

1. Charger le fichier image d'entrée
1. Obtenir la hauteur et la largeur de l'image
1. Définir la hauteur, la largeur et les marges d'une page
1. Sauvegarder le fichier PDF de sortie

Le code suivant montre comment convertir une image en PDF avec la même hauteur et largeur de page en utilisant C# :

```csharp
// Charger le fichier image JPG d'entrée
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// Lire la hauteur de l'image d'entrée
int h = srcImage.Height;

// Lire la largeur de l'image d'entrée
int w = srcImage.Width;

// Initialiser un nouveau document PDF
Document doc = new Document();

// Ajouter une page vide
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Définir les dimensions de la page et les marges
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Sauvegarder le fichier PDF de sortie
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**Essayez de convertir JPG en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion de JPG à PDF avec l'application gratuite](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG en PDF

**Aspose.PDF for .NET** prend en charge la fonctionnalité de conversion d'images PNG en format PDF. Consultez l'extrait de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> désigne un type de format de fichier d'image matricielle qui utilise une compression sans perte, ce qui le rend populaire parmi ses utilisateurs.

Vous pouvez convertir une image PNG en PDF en suivant les étapes ci-dessous :

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Étapes : Convertir PNG en PDF en C#</strong></a>

1. Chargez l'image **PNG** d'entrée.
2. Lisez les valeurs de hauteur et de largeur.
3.
3. Définir les dimensions de la page.
4. Enregistrer le fichier de sortie.

De plus, le fragment de code ci-dessous montre comment convertir un PNG en PDF avec C# dans vos applications .NET :

```csharp
// Charger le fichier PNG d'entrée
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// Initialiser un nouveau Document
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Définir les dimensions de la page
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Enregistrer le PDF de sortie
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**Essayez de convertir un PNG en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

Aspose vous présente une application gratuite en ligne ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion de PNG en PDF avec l'application gratuite](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG en PDF

**Aspose.PDF pour .NET** explique comment convertir des images SVG en format PDF et comment obtenir les dimensions du fichier <abbr title="Scalable Vector Graphics">SVG</abbr> source.

Les graphiques vectoriels évolutifs (SVG) constituent une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le Consortium World Wide Web (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML.
Les images SVG et leurs comportements sont définis dans des fichiers texte XML.

{{% alert color="success" %}}
**Essayez de convertir le format SVG en PDF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["SVG en PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion de SVG en PDF par Aspose.PDF avec application gratuite](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Pour convertir des fichiers SVG en PDF, utilisez la classe nommée [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions) qui est utilisée pour initialiser l'objet [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions). Plus tard, cet objet est passé comme argument lors de l'initialisation de l'objet Document et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Étapes : Convertir SVG en PDF en C#</strong></a>

1.
1.
2. Créez une instance de la classe [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le nom de fichier source et les options mentionnées.
3. Sauvegardez le document avec le nom de fichier désiré.

Le code suivant montre le processus de conversion d'un fichier SVG en format PDF avec Aspose.PDF pour .NET.

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument= new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## Obtenir les dimensions du SVG

Il est également possible d'obtenir les dimensions du fichier SVG source. Cette information peut être utile si nous voulons que le SVG couvre la totalité de la page du PDF de sortie. La propriété AdjustPageSize de la classe ScgLoadOption répond à cette exigence. La valeur par défaut de cette propriété est false. Si la valeur est réglée sur true, le PDF de sortie aura les mêmes dimensions que le SVG source.

Le code suivant montre le processus d'obtention des dimensions du fichier SVG source et de génération d'un fichier PDF.
Le code suivant montre le processus pour obtenir les dimensions du fichier SVG source et générer un fichier PDF.

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Le chemin vers le répertoire des documents.
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### Fonctionnalités SVG prises en charge

<table>
    <thead>
        <tr>
            <th>
                <p>Balise SVG</p>
            </th>
            <th>
                <p>Exemple d'utilisation</p>
            </th>
        </tr>
    </thead>
    <tbody>

<tbody>
    <tr>
        <td>
            <p>cercle</p>
        </td>
        <td>
            <code><pre>&lt;circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt;</pre></code>
        </td>
    </tr>
    <tr>
        <td>
            <p>définitions</p>
        </td>
        <td>
            <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
        </td>
    </tr>
</tbody>
```

         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Données de caractère référencées&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```

                    font-family="Verdana" font-size="100"
                    text-anchor="middle" >  
                    Texte masqué  
                    </text>  
                    <use xlink:href="#Text" fill="blue" /></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse</p>
            </td>
            <td>
                <p><ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g</p>
            </td>
            <td>
                <p><g fill="none" stroke="gris foncé" stroke-width="1.5" >  
                    <line x1="-7"
                    y1="-7" x2="-3" y2="-3"/>  
                    <line x1="7" y1="7" x2="3"
```

<tr>
    <td>
        <p>image</p>
    </td>
    <td>
        <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
            /&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>ligne</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
```

<tr>
    <td>
        <p>ligne</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>chemin</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>style</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>polygone</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>polyligne</p>
    </td>
```

<p>polyline</p>
</td>
<td>
    <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
        -3,1 -3,-5"/&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>rect</p>
</td>
<td>
    <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>svg</p>
</td>
<td>
    <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
</td>
</tr>
<tr>
<td>
    <p>texte</p>
</td>
<td>
    <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
        y="30" pointer-events="none"&gt;Titre de la carte&lt;/text&gt;</p>
</td>
```

## Convertir TIFF en PDF

**Aspose.PDF** prend en charge le format de fichier, qu'il s'agisse d'une image <abbr title="Tag Image File Format">TIFF</abbr> à un seul cadre ou à plusieurs cadres. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications .NET.

TIFF ou TIF, le format de fichier d'image balisé, représente des images raster destinées à être utilisées sur une variété d'appareils conformes à cette norme de format de fichier.
```

<table>
    <tbody>
        <tr>
            <td>
                <p>police</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; Texte d'exemple&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;entrée de valeur de couleur d'encre six. Ici, il le fera &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>
```
TIFF ou TIF, Tagged Image File Format, représente des images raster destinées à être utilisées sur une variété d'appareils qui respectent cette norme de format de fichier.

Vous pouvez convertir TIFF en PDF de la même manière que les autres formats de fichiers raster graphiques :

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Étapes : Convertir TIFF en PDF en C#</strong></a>

1. Créer un nouvel objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ajouter une Page.
2. Charger l'image **TIFF** d'entrée.
3. Sauvegarder le document PDF.

```csharp
Initialiser un document PDF vide
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Charger le fichier d'image Tiff exemple
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Sauvegarder le document PDF de sortie
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

Dans le cas où vous avez besoin de convertir une image TIFF multipage en un document PDF multipage et de contrôler certains paramètres, par exemple.
Dans le cas où vous auriez besoin de convertir une image TIFF multipage en document PDF multipage et de contrôler certains paramètres, par exemple :

1. Instancier une instance de la classe Document
1. Charger l'image TIFF d'entrée
1. Obtenir la FrameDimension des cadres
1. Ajouter une nouvelle page pour chaque cadre
1. Enfin, enregistrer les images dans des pages PDF

Le fragment de code suivant montre comment convertir une image TIFF multipage ou multiframe en PDF avec C# :

```csharp
public static void TiffToPDF2()
{
    // Initialiser un nouveau Document
    Document pdf = new Document();

    // Charger l'image TIFF dans un flux
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // Convertir un TIFF multipage ou multiframe en PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // Itérer à travers chaque cadre
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            // Appliquer d'autres options
            // ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // Enregistrer le fichier PDF de sortie
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## S'applique à

|**Plateforme**|**Pris en charge**|**Commentaires**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## Voir aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_ : **BMP**
- [C# BMP vers PDF Code](#csharp-bmp-to-pdf)
- [C# BMP vers PDF API](#csharp-bmp-to-pdf)
- [C# BMP vers PDF Programmation](#csharp-bmp-to-pdf)
- [C# BMP vers PDF Bibliothèque](#csharp-bmp-to-pdf)
- [C# Enregistrer BMP comme PDF](#csharp-bmp-to-pdf)
- [C# Générer PDF à partir de BMP](#csharp-bmp-to-pdf)
- [C# Créer PDF à partir de BMP](#csharp-bmp-to-pdf)
- [C# BMP vers PDF Convertisseur](#csharp-bmp-to-pdf)

_Format_ : **CGM**
- [C# CGM vers PDF Code](#csharp-cgm-to-pdf)
- [C# CGM vers PDF API](#csharp-cgm-to-pdf)
- [C# CGM vers PDF Programmation](#csharp-cgm-to-pdf)
- [C# CGM vers PDF Bibliothèque](#csharp-cgm-to-pdf)
- [C# Enregistrer CGM comme PDF](#csharp-cgm-to-pdf)
- [C# Générer PDF à partir de CGM](#csharp-cgm-to-pdf)
- [C# Créer PDF à partir de CGM](#csharp-cgm-to-pdf)
- [C# CGM vers PDF Convertisseur](#csharp-cgm-to-pdf)
- [Convertisseur C# CGM vers PDF](#csharp-cgm-to-pdf)

_Format_ : **DICOM**
- [Code C# DICOM vers PDF](#csharp-dicom-to-pdf)
- [API C# DICOM vers PDF](#csharp-dicom-to-pdf)
- [Programmation C# DICOM vers PDF](#csharp-dicom-to-pdf)
- [Bibliothèque C# DICOM vers PDF](#csharp-dicom-to-pdf)
- [Sauvegarder DICOM en PDF avec C#](#csharp-dicom-to-pdf)
- [Générer un PDF à partir de DICOM avec C#](#csharp-dicom-to-pdf)
- [Créer un PDF à partir de DICOM avec C#](#csharp-dicom-to-pdf)
- [Convertisseur C# DICOM vers PDF](#csharp-dicom-to-pdf)

_Format_ : **EMF**
- [Code C# EMF vers PDF](#csharp-emf-to-pdf)
- [API C# EMF vers PDF](#csharp-emf-to-pdf)
- [Programmation C# EMF vers PDF](#csharp-emf-to-pdf)
- [Bibliothèque C# EMF vers PDF](#csharp-emf-to-pdf)
- [Sauvegarder EMF en PDF avec C#](#csharp-emf-to-pdf)
- [Générer un PDF à partir de EMF avec C#](#csharp-emf-to-pdf)
- [Créer un PDF à partir de EMF avec C#](#csharp-emf-to-pdf)
- [Convertisseur C# EMF vers PDF](#csharp-emf-to-pdf)
