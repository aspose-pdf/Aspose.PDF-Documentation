---
title: Convertir un PDF en différents formats d'image en C#
linktitle: Convertir un PDF en Images
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour convertir des PDF en différents formats d'images tels que TIFF, BMP, EMF, JPEG, PNG, GIF, SVG avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Aperçu

Cet article explique comment convertir un PDF en différents formats d'image en utilisant C#. Il couvre les sujets suivants.

_Format d'image_ : **TIFF**
- [C# PDF en TIFF](#csharp-pdf-to-tiff)
- [C# Convertir PDF en TIFF](#csharp-pdf-to-tiff)
- [C# Convertir des pages uniques ou particulières du PDF en TIFF](#csharp-pdf-to-tiff-pages)

_Format d'image_ : **BMP**
- [C# PDF en BMP](#csharp-pdf-to-bmp)
- [C# Convertir PDF en BMP](#csharp-pdf-to-bmp)
- [C# Convertisseur de PDF en BMP](#csharp-pdf-to-bmp)

_Format d'image_ : **EMF**
- [C# PDF en EMF](#csharp-pdf-to-emf)
- [C# Convertir PDF en EMF](#csharp-pdf-to-emf)
- [C# Convertisseur de PDF en EMF](#csharp-pdf-to-emf)
- [Convertisseur C# PDF en EMF](#csharp-pdf-to-emf)

_Forme d'Image_ : **JPG**
- [C# PDF en JPG](#csharp-pdf-to-jpg)
- [C# Convertir PDF en JPG](#csharp-pdf-to-jpg)
- [Convertisseur C# PDF en JPG](#csharp-pdf-to-jpg)

_Forme d'Image_ : **PNG**
- [C# PDF en PNG](#csharp-pdf-to-png)
- [C# Convertir PDF en PNG](#csharp-pdf-to-png)
- [Convertisseur C# PDF en PNG](#csharp-pdf-to-png)

_Forme d'Image_ : **GIF**
- [C# PDF en GIF](#csharp-pdf-to-gif)
- [C# Convertir PDF en GIF](#csharp-pdf-to-gif)
- [Convertisseur C# PDF en GIF](#csharp-pdf-to-gif)

_Forme d'Image_ : **SVG**
- [C# PDF en SVG](#csharp-pdf-to-svg)
- [C# Convertir PDF en SVG](#csharp-pdf-to-svg)
- [Convertisseur C# PDF en SVG](#csharp-pdf-to-svg)

## C# Convertir PDF en Image

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF pour .NET** utilise plusieurs approches pour convertir un PDF en image.
**Aspose.PDF pour .NET** utilise plusieurs approches pour convertir des PDF en image.

Il existe plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est orienté pour la conversion de l'ensemble du document, mais ImageDevice - pour une page particulière.

## Convertir un PDF en utilisant la classe DocumentDevice

**Aspose.PDF pour .NET** rend possible la conversion des pages PDF en images TIFF.

La classe TiffDevice (basée sur DocumentDevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée `Process` qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="success" %}}
**Essayez de convertir un PDF en TIFF en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF en TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion de Aspose.PDF PDF en TIFF avec application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une seule image TIFF

Aspose.PDF pour .NET explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

<a name="csharp-pdf-to-tiff"><strong>Étapes : Convertir PDF en TIFF en C#</strong></a>

1. Créez un objet de la classe **Document**.
2. Créez des objets **TiffSettings** et **TiffDevice**
3. Appelez la méthode **TiffDevice.Process()** pour convertir le document PDF en TIFF.
4. Pour définir les propriétés du fichier de sortie, utilisez la classe **TiffSettings**.

Le code suivant montre comment convertir toutes les pages du PDF en une seule image TIFF.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Créer un objet Résolution
    Resolution resolution = new Resolution(300);

    // Créer un objet TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Créer un appareil TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convertir une page particulière et sauvegarder l'image dans le flux
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### Convertir une page en image TIFF

Aspose.PDF pour .NET permet de convertir une page spécifique d'un fichier PDF en image TIFF, utilisez une version surchargée de la méthode Process(..) qui prend un numéro de page comme argument pour la conversion. Le fragment de code suivant montre comment convertir la première page d'un PDF au format TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Étapes : Convertir des pages simples ou spécifiques d'un PDF en TIFF en C#</strong></a>

1. Créer un objet de la classe **Document**.
2. Créer des objets **TiffSettings** et **TiffDevice**
3. Appeler la méthode surchargée **TiffDevice.Process()** avec les paramètres **fromPage** et **toPage** pour convertir les pages du document PDF en TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Créer un objet Resolution
    Resolution resolution = new Resolution(300);

    // Créer un objet TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Créer un dispositif TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convertir une page spécifique et sauvegarder l'image dans un flux
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Utilisez l'algorithme de Bradley lors de la conversion

Aspose.PDF pour .NET prend en charge la fonctionnalité de conversion de PDF en TIF utilisant la compression LZW et ensuite, avec l'utilisation de AForge, la binarisation peut être appliquée. Cependant, l'un des clients a demandé que pour certaines images, ils doivent obtenir le seuil en utilisant Otsu, donc ils aimeraient également utiliser Bradley.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // Ouvrir le document
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Créer un objet Résolution
    Resolution resolution = new Resolution(300);
    // Créer un objet TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Créer un dispositif TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Convertir une page particulière et sauvegarder l'image dans un flux
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## Convertir un PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.
- La classe [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.
- La classe [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Jetons un coup d'œil à la manière de convertir une page PDF en image.
Jetons un œil à comment convertir une page PDF en image.

La classe `BmpDevice` fournit une méthode nommée [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) qui permet de convertir une page spécifique du fichier PDF en format d'image BMP. Les autres classes disposent de la même méthode. Donc, si nous avons besoin de convertir une page PDF en image, nous instancions simplement la classe requise.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

Les étapes suivantes et le fragment de code en C# montrent cette possibilité

 - [Convertir PDF en BMP en C#](#csharp-pdf-to-image)
 - [Convertir PDF en EMF en C#](#csharp-pdf-to-image)
 - [Convertir PDF en JPG en C#](#csharp-pdf-to-image)
 - [Convertir PDF en PNG en C#](#csharp-pdf-to-image)
 - [Convertir PDF en GIF en C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Étapes : PDF en Image (BMP, EMF, JPG, PNG, GIF) en C#</strong></a>

1.
1.
2. Créez une instance d'une sous-classe de **ImageDevice** par exemple :
   * **BmpDevice** (pour convertir un PDF en BMP)
   * **EmfDevice** (pour convertir un PDF en Emf)
   * **JpegDevice** (pour convertir un PDF en JPG)
   * **PngDevice** (pour convertir un PDF en PNG)
   * **GifDevice** (pour convertir un PDF en GIF)
3. Appelez la méthode **ImageDevice.Process()** pour effectuer la conversion de PDF en image.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Créer un objet Resolution            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // Convertir une page spécifique et enregistrer l'image dans le flux
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Fermer le flux
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**Essayez de convertir des PDF en PNG en ligne**

Voici un exemple de fonctionnement de nos applications gratuites.

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["PDF en PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG avec l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir un PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir un PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant C# et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir des PDF en SVG en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["PDF en SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.
{{% /alert %}}

[![Conversion de PDF en SVG avec l'application gratuite Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
**Graphiques Vectoriels Scalables (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour des graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

Aspose.PDF pour .NET prend en charge la fonctionnalité de conversion d'images SVG en format PDF et offre également la capacité de convertir des fichiers PDF en format SVG.
Aspose.PDF pour .NET prend en charge la fonctionnalité de conversion d'une image SVG en format PDF et offre également la capacité de convertir des fichiers PDF en format SVG.

Le code suivant montre les étapes pour convertir un fichier PDF en format SVG avec .NET.

<a name="csharp-pdf-to-svg"><strong>Étapes : Convertir PDF en SVG en C#</strong></a>

1. Créez un objet de la classe **Document**.
2. Créez un objet **SvgSaveOptions** avec les paramètres nécessaires.
3. Appelez la méthode **Document.Save()** et passez-lui l'objet **SvgSaveOptions** pour convertir le document PDF en SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // Charger le document PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // Instancier un objet de SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // Ne pas compresser l'image SVG en archive Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Sauvegarder la sortie en fichiers SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

