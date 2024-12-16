---
title: Convertir PDF en formats d'images
linktitle: Convertir PDF en images
type: docs
weight: 70
url: /fr/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir PDF en divers formats d'images. Convertissez des pages PDF en images PNG, JPEG, BMP avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** utilise quelques approches pour convertir PDF en image. En général, nous utilisons deux approches : la conversion en utilisant l'approche Device et la conversion en utilisant SaveOption. Cette section vous montrera comment convertir des documents PDF en formats d'image tels que BMP, JPEG, PNG, TIFF, et SVG en utilisant l'une de ces approches.

Il y a plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est orienté pour la conversion de l'ensemble du document, mais ImageDevice - pour une page particulière.

## Convertir PDF en utilisant la classe DocumentDevice

**Aspose.PDF for C++** rend possible la conversion de pages PDF en images TIFF.

Le [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (basé sur DocumentDevice) permet de convertir les pages PDF en images TIFF. Cette classe fournit une méthode nommée [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="success" %}}
**Essayez de convertir un PDF en TIFF en ligne**

Aspose.PDF pour C++ vous présente une application gratuite en ligne ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en TIFF avec l'application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une seule image TIFF

Aspose.PDF pour С++ explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

1.  Ouvrir [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) avec MakeObject.
1. Créer un objet Resolution.
1. Créer un objet [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. Créer un [Tiff device](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) avec des attributs spécifiés.
1. Convertir une page particulière et enregistrer l'image dans le flux.

Le code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Créer un objet Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Créer un objet TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // Créer un appareil TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // Convertir les pages et enregistrer l'image dans le flux
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### Convertir une page en image TIFF

Aspose.PDF pour C++ vous permet de convertir une page particulière dans un fichier PDF en une image TIFF, en utilisant une version surchargée de la méthode Process(..) qui prend un numéro de page comme argument pour la conversion. L'extrait de code suivant montre comment convertir la première page d'un PDF au format TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Créer un objet Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Créer un périphérique TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Convertir une page particulière et enregistrer l'image dans le flux
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Utiliser l'algorithme de Bradley lors de la conversion

Aspose.PDF pour C++ prend en charge la fonctionnalité de conversion de PDF en TIF en utilisant la compression LZW et ensuite avec l'utilisation d'AForge, la binarisation peut être appliquée. Cependant, l'un des clients a demandé que pour certaines images, ils ont besoin d'obtenir le seuil en utilisant Otsu, donc ils aimeraient aussi utiliser Bradley.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Créer un objet Résolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Créer un objet TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Créer un dispositif TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Convertir une page particulière et enregistrer l'image dans le flux
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convertir un PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.
- La classe [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.

- La classe [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Prenons un moment pour voir comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) fournit une méthode nommée [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) qui vous permet de convertir une page particulière du fichier PDF au format image BMP. Les autres classes ont la même méthode. Donc, si nous avons besoin de convertir une page PDF en image, nous devons simplement instancier la classe requise.

L'extrait de code suivant montre cette possibilité :

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Créer un objet Resolution            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Créer un objet Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Convertir une page particulière et enregistrer l'image dans le flux
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // Fermer le flux
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de la façon dont nos applications gratuites fonctionnent, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour C++ vous présente l'application en ligne gratuite ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant C++ et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour C++ vous présente l'application en ligne gratuite ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

Afin de convertir un PDF en SVG, Aspose.PDF pour CPP propose la méthode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Vous devez passer le chemin de sortie et l'énumération SaveFormat:: svg à la méthode Save pour convertir le PDF en SVG. L'extrait de code suivant montre comment convertir un PDF en SVG :

Cet article vous apprend comment convertir un PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant C++.

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

Aspose.PDF pour C++ prend en charge la fonctionnalité de conversion d'image SVG au format PDF et offre également la possibilité de convertir des fichiers PDF au format SVG. Pour accomplir cette exigence, la classe `SvgSaveOptions` a été introduite dans l'espace de noms Aspose.PDF. Instanciez un objet de SvgSaveOptions et passez-le comme deuxième argument à la méthode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

L'exemple de code suivant montre les étapes pour convertir un fichier PDF au format SVG avec C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier un objet de SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // Ne pas compresser l'image SVG dans une archive Zip
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Enregistrer la sortie dans des fichiers SVG
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```