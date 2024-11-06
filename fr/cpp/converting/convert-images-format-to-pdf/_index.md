---
title: Convertir divers formats d'images en PDF 
linktitle: Convertir des images en PDF
type: docs
weight: 60
url: fr/cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment la bibliothèque Aspose.PDF pour C++ permet de convertir divers formats d'images en PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF pour C++** vous permet de convertir différents formats d'images en fichiers PDF. Notre bibliothèque démontre des extraits de code pour convertir les formats d'image les plus populaires, tels que - BMP, DICOM, EMF, JPG, PNG, SVG et TIFF.

## Convertir BMP en PDF

Convertir des fichiers BMP en document PDF en utilisant la bibliothèque **Aspose.PDF pour C++**.

Les images <abbr title="Bitmap Image File">BMP</abbr> sont des fichiers ayant une extension. BMP représente des fichiers d'image bitmap utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant de l'appareil (DIB). Vous pouvez convertir BMP en fichiers PDF avec l'API Aspose.PDF pour C++.  Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

1. Créez une [classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Une instance d'un nouvel objet Document est créée.
1. Ajoutez une nouvelle [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à ce [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Un nouveau BMP Aspose.Pdf est créé.
1. L'objet BMP Aspose.PDF est initialisé en utilisant le fichier d'entrée.
1. Aspose.PDF BMP est ajouté à la Page en tant que Paragraphe.
1. Enfin, enregistrez le fichier PDF de sortie

Ainsi, l'extrait de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant C++ :

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.bmp");

    // String for input file name
    String outfilename("ImageToPDF-BMP.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir BMP en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF BMP en PDF en utilisant l'application gratuite](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir DICOM en PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est le format standard de l'industrie médicale pour la création, le stockage, la transmission et la visualisation d'images médicales numériques et de documents de patients examinés.

**Aspsoe.PDF pour C++** vous permet de convertir des images DICOM et SVG, mais pour des raisons techniques, pour ajouter des images vous devez spécifier le type de fichier à ajouter au PDF :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom de chemin et le nom de fichier.
1.  Instancier l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Ajouter une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à la collection de pages du document.
1. Aspose.PDF TDicom est ajouté à la Page en tant que Paragraphe.
1. Charger et [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier image d'entrée.

Le code suivant montre comment convertir des fichiers DICOM au format PDF avec Aspose.PDF. Vous devez charger l'image DICOM, placer l'image sur une page dans un fichier PDF et enregistrer le résultat en tant que PDF.

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir DICOM en PDF en ligne**

Aspose vous présente l'application gratuite en ligne ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion DICOM en PDF avec l'application gratuite](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF en PDF

<abbr title="Enhanced metafile format">EMF</abbr>EMF stocke des images graphiques de manière indépendante du périphérique. Les métadonnées EMF se composent d'enregistrements de longueur variable dans un ordre chronologique qui peuvent restituer l'image stockée après analyse sur n'importe quel périphérique de sortie. Par ailleurs, vous pouvez convertir EMF en image PDF en utilisant les étapes ci-dessous :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom de chemin et le nom de fichier.
1. Une instance d'un nouvel objet Document est créée.
1. Ajoutez une nouvelle Page à ce [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose.Pdf TIFF is created.  
1. L'objet Aspose.PDF TIFF est initialisé en utilisant le fichier d'entrée.  
1. Aspose.PDF TIFF est ajouté à la Page en tant que Paragraphe.  
1. Charger et [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier image d'entrée.  

Moreover, the following code snippet shows how to convert an EMF to PDF with C++ in your code snippet:

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir EMF en PDF en ligne**

Aspose vous présente l'application en ligne gratuite ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion EMF en PDF en utilisant l'application gratuite](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir JPG en PDF

Pas besoin de se demander comment convertir JPG en PDF, car la bibliothèque **Aspose.PDF pour C++** a la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour C++ en suivant les étapes :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le chemin et le nom de fichier.
1. Une instance d'un nouvel objet Document est créée.
1. Ajoutez une nouvelle Page à ce [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Une nouvelle Aspose::Pdf::Image est créée.
1. L'objet Image d'Aspose.PDF est initialisé à l'aide du fichier d'entrée.
1. Aspose.PDF Image est ajouté à la Page en tant que Paragraphe.
1. Chargez et enregistrez le fichier image d'entrée.

Le code ci-dessous montre comment convertir une image JPG en PDF en utilisant C++ :

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.jpg");

    // Chaîne pour le nom du fichier d'entrée
    String outfilename("ImageToPDF-JPEG.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();

    // Ajouter une page vide dans un document vide
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Ajouter l'image sur une page
    page->get_Paragraphs()->Add(image);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Ensuite, vous pouvez voir comment convertir une image en PDF avec la **même hauteur et largeur de la page**. Nous allons obtenir les dimensions de l'image et, en conséquence, définir les dimensions de page du document PDF avec les étapes suivantes :

1. Charger le fichier image d'entrée
1. Obtenir la hauteur et la largeur de l'image
1. Définir la hauteur, la largeur et les marges d'une page
1. Enregistrer le fichier PDF de sortie

Le code suivant montre comment convertir une image en PDF avec la même hauteur et largeur de page en utilisant C++ :

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir JPG en PDF en ligne**

Aspose vous présente une application en ligne gratuite ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion JPG en PDF en utilisant l'application gratuite](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG en PDF

**Aspose.PDF pour C++** prend en charge la fonctionnalité de conversion des images PNG au format PDF. Consultez l'extrait de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> fait référence à un type de format de fichier d'image matricielle qui utilise une compression sans perte, ce qui le rend populaire parmi ses utilisateurs.

Vous pouvez convertir une image PNG en PDF en suivant les étapes ci-dessous :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Une instance d'un nouvel objet Document est créée.
1. Ajouter une nouvelle page à ce [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Un nouveau PNG Aspose.Pdf est créé.
1. L'objet PNG Aspose.PDF est initialisé à l'aide du fichier d'entrée.
1. Le PNG Aspose.PDF est ajouté à la page en tant que paragraphe.
1. Charger et enregistrer le fichier image d'entrée.

De plus, l'extrait de code ci-dessous montre comment convertir un PNG en PDF dans vos applications C++ :

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.png");

    // Chaîne pour le nom du fichier de sortie
    String outfilename("ImageToPDF-PNG.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();

    // Ajouter une page vide dans le document vide
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Ajouter l'image sur une page
    page->get_Paragraphs()->Add(image);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir PNG en PDF en ligne**

Aspose vous présente l'application gratuite en ligne ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PNG en PDF à l'aide de l'application gratuite](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG en PDF

**Aspose.PDF pour C++** explique comment convertir des images SVG en format PDF et comment obtenir les dimensions du fichier source <abbr title="Scalable Vector Graphics">SVG</abbr>.

Les graphiques vectoriels évolutifs (SVG) sont une famille de spécifications d'un format de fichier basé sur XML pour des graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

1. Créez une [classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Créez une instance de la classe [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. Créez une instance de la [classe Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le nom de fichier source mentionné et les options.
1. Enregistrez le document avec le nom de fichier souhaité.

Le fragment de code suivant montre le processus de conversion d'un fichier SVG en format PDF avec Aspose.PDF pour C++.

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
Сonsidérer un exemple avec des fonctionnalités avancées :

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "Conversion SVG en PDF : Début" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "Conversion SVG en PDF : Fin" << std::endl;
}
```

{{% alert color="success" %}}
**Essayez de convertir le format SVG en PDF en ligne**


Aspose.PDF pour C++ vous présente une application en ligne gratuite ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF en PDF

Le format de fichier **Aspose.PDF** est pris en charge, qu'il s'agisse d'une image <abbr title="Tag Image File Format">TIFF</abbr> à un seul cadre ou à plusieurs cadres. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications C++.

TIFF ou TIF, Tagged Image File Format, représente des images raster destinées à être utilisées sur une variété d'appareils conformes à cette norme de format de fichier. L'image TIFF peut contenir plusieurs cadres avec différentes images. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une image TIFF à un seul cadre ou à plusieurs cadres. Vous pouvez donc convertir l'image TIFF en PDF dans vos applications C++. Par conséquent, nous allons examiner un exemple de conversion d'une image TIFF multi-pages en document PDF multi-pages avec les étapes ci-dessous :

1. Créer une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le chemin d'accès et le nom de fichier.
1. Un instance d'un nouvel objet Document est créé.
1. Ajoutez une nouvelle Page à ce [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Un nouveau Aspose.Pdf TIFF est créé.
1. L'objet Aspose.PDF TIFF est initialisé en utilisant le fichier d'entrée.
1. Aspose.PDF TIFF est ajouté à la Page en tant que Paragraphe.
1. Chargez et enregistrez le fichier image d'entrée.

De plus, l'extrait de code suivant montre comment convertir une image TIFF multi-pages ou multi-cadres en PDF avec C++ :

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```