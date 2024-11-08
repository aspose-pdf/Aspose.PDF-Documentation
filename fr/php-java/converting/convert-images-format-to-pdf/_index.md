---
title: Convertir divers formats d'images en PDF 
linktitle: Convertir des images en PDF
type: docs
weight: 60
url: /fr/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment la bibliothèque Aspose.PDF pour PHP permet de convertir divers formats d'images en PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF pour PHP** vous permet de convertir différents formats d'images en fichiers PDF. Notre bibliothèque présente des extraits de code pour convertir les formats d'image les plus populaires, tels que - BMP, CGM, D    MF, JPG, PNG, SVG et TIFF.

## Convertir BMP en PDF

Convertissez des fichiers BMP en document PDF en utilisant la bibliothèque **Aspose.PDF pour PHP**.

Les images <abbr title="Bitmap Image File">BMP</abbr> sont des fichiers ayant l'extension .BMP représentant des fichiers d'image bitmap utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant du dispositif (DIB).
Vous pouvez convertir BMP en PDF avec l'API Aspose.PDF pour PHP.
 Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

1. Créez un nouvel objet Document
1. Ajoutez une nouvelle page au document
1. Réglez les marges de la page à 0 (si nécessaire)
1. Créez un nouvel objet Image et définissez le fichier BMP d'entrée
1. Ajoutez l'image à la page
1. Enregistrez le document dans le fichier PDF de sortie

Ainsi, l'extrait de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant PHP :

```php
// Créez un nouvel objet Document
$document = new Document();

// Ajoutez une nouvelle page au document
$page = $document->getPages()->add();

// Réglez les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créez un nouvel objet Image et définissez le fichier BMP d'entrée
$image = new Image();
$image->setFile($inputFile);

// Ajoutez l'image à la page
$page->getParagraphs()->add($image);

// Enregistrez le document dans le fichier PDF de sortie
$document->save($outputFile);
```

## Convertir CGM en PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> est une norme ISO qui fournit un format de fichier d'image 2D vectorielle pour le stockage et la récupération d'informations graphiques. CGM est un format indépendant du périphérique. CGM est un format de graphiques vectoriels qui prend en charge trois méthodes d'encodage différentes : binaire (meilleur pour la vitesse de lecture par programme), basé sur des caractères (produit la plus petite taille de fichier et permet des transferts de données plus rapides) ou encodage en texte clair (permet aux utilisateurs de lire et de modifier le fichier avec un éditeur de texte)

Le code suivant vous montre comment convertir des fichiers CGM en format PDF en utilisant Aspose.PDF pour PHP.

1. Créez une instance de [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) pour spécifier des options spécifiques pour le chargement du fichier CGM
1. Créez une instance de la classe [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) avec le nom de fichier source mentionné et les options.
1. Enregistrez le document avec le nom de fichier souhaité.

```php
$options = new CgmLoadOptions();

// Créez un objet Document et chargez le fichier CGM en utilisant les options spécifiées
$document = new Document($inputFile, $options);

// Enregistrez le document en tant que fichier PDF
$document->save($outputFile);
```


## Convertir DICOM en PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est une norme pour gérer, stocker, imprimer et transmettre des informations en imagerie médicale. Elle comprend une définition de format de fichier et un protocole de communication réseau.

Aspose.PDF pour PHP vous permet de convertir des fichiers DICOM en format PDF, consultez le code suivant :

1. Créez un nouvel objet Document
1. Ajoutez une nouvelle page au document
1. Définissez les marges de la page à 0 (si nécessaire)
1. Créez un nouvel objet Image et définissez le fichier BMP d'entrée
1. Définissez le fichier DICOM comme fichier source pour l'image
1. Définissez le type de fichier de l'image sur DICOM
1. Ajoutez l'image à la page
1. Enregistrez le document dans le fichier PDF de sortie

```php
// Créez un nouvel objet Document
$document = new Document();

// Ajoutez une nouvelle page au document
$page = $document->getPages()->add();

// Définissez les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créez un nouvel objet Image
$image = new Image();

// Définissez le fichier DICOM comme fichier source pour l'image
$image->setFile($inputFile);

// Définissez le type de fichier de l'image sur DICOM
$image->setFileType(ImageFileType::$Dicom);

// Ajoutez l'image à la page
$page->getParagraphs()->add($image);

// Enregistrez le document en tant que fichier PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Essayez de convertir DICOM en PDF en ligne**

Aspose vous présente une application en ligne gratuite ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion DICOM en PDF en utilisant l'application gratuite](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF en PDF

Le format de métafichier amélioré (<abbr title="Enhanced metafile format">EMF</abbr>) stocke des images graphiques de manière indépendante des périphériques. Les métafichiers EMF comprennent des enregistrements de longueur variable dans l'ordre chronologique qui peuvent rendre l'image stockée après analyse sur n'importe quel périphérique de sortie.

Nous avons plusieurs approches pour convertir EMF en PDF.

## Utilisation de la classe Image

Un document PDF comprend des pages et chaque page contient un ou plusieurs objets paragraphe. Un paragraphe peut être un texte, une image, un tableau, une boîte flottante, un graphique, un titre, un champ de formulaire ou une pièce jointe.

Pour convertir un fichier image en format PDF, enveloppez-le dans un paragraphe.

Il est possible de convertir des images à un emplacement physique sur le disque dur local, trouvées à une URL Web ou dans une instance Stream.

Pour ajouter une image :

1. Créez un objet de la classe com.aspose.pdf.Image.
1. Ajoutez l'image à une collection [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de l'instance de page.
1. Spécifiez le chemin ou la source de l'image.
    - Si une image se trouve à un emplacement sur le disque dur, spécifiez l'emplacement du chemin en utilisant la méthode [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Si une image est placée dans un FileInputStream, passez l'objet contenant l'image à la méthode [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Le code suivant montre comment charger un objet image, définir la marge de la page, placer l'image sur la page et sauvegarder la sortie en tant que PDF.

```php
$inputFile = "sample.emf";

// Créer un nouvel objet Document
$document = new Document();

// Ajouter une nouvelle page au document
$page = $document->getPages()->add();

// Définir les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créer un nouvel objet Image et définir le fichier d'entrée
$image = new Image();
$image->setFile($inputFile);

// Ajouter l'image à la page
$page->getParagraphs()->add($image);

// Sauvegarder le document en tant que fichier PDF
$document->save($outputFile);
```


## Convertir JPG en PDF

Pas besoin de se demander comment convertir JPG en PDF, car la bibliothèque Apose.PDF pour PHP a la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour PHP en suivant les étapes suivantes :

1. Initialiser un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Ajouter une nouvelle page au document
1. Définir les marges de la page à 0
1. Créer un nouvel objet Image et définir le fichier d'entrée
1. Enregistrer le PDF de sortie

L'extrait de code ci-dessous montre comment convertir une image JPG en PDF en utilisant PHP :

```php
$inputFile = "sample.jpg";

// Créer un nouvel objet Document
$document = new Document();

// Ajouter une nouvelle page au document
$page = $document->getPages()->add();

// Définir les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créer un nouvel objet Image et définir le fichier d'entrée
$image = new Image();
$image->setFile($inputFile);

// Ajouter l'image à la page
$page->getParagraphs()->add($image);

// Enregistrer le document en tant que fichier PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Essayez de convertir JPG en PDF en ligne**

Aspose vous présente l'application en ligne gratuite ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion JPG en PDF utilisant l'application gratuite](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG en PDF

**Aspose.PDF pour PHP** prend en charge la fonctionnalité de conversion des images PNG en format PDF. Consultez l'extrait de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> se réfère à un type de format de fichier d'image matricielle qui utilise une compression sans perte, ce qui le rend populaire parmi ses utilisateurs.

Vous pouvez convertir une image PNG en PDF en utilisant les étapes ci-dessous :

1. Initialisez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Ajoutez une nouvelle page au document
1. Réglez les marges de la page à 0
1. Créez un nouvel objet Image et définissez le fichier d'entrée
1. Enregistrez le PDF de sortie

De plus, l'extrait de code ci-dessous montre comment convertir PNG en PDF dans vos applications PHP :

```php
$inputFile = "sample.png";

// Créez un nouvel objet Document
$document = new Document();

// Ajoutez une nouvelle page au document
$page = $document->getPages()->add();

// Réglez les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créez un nouvel objet Image et définissez le fichier d'entrée
$image = new Image();
$image->setFile($inputFile);

// Ajoutez l'image à la page
$page->getParagraphs()->add($image);

// Enregistrez le document en tant que fichier PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir PNG en PDF en ligne**

Aspose vous présente l'application en ligne gratuite ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez essayer de découvrir la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## Convertir SVG en PDF

Les Scalable Vector Graphics (SVG) sont une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et, si nécessaire, compressées. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

## Comment convertir un fichier SVG en format PDF

Pour convertir des fichiers SVG en PDF, utilisez la classe nommée [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) qui est utilisée pour initialiser l'objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 Plus tard, cet objet est passé comme argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le snippet de code suivant montre le processus de conversion d'un fichier SVG en format PDF.

```php
// Créer un nouvel objet SvgLoadOptions
$loadOption = new SvgLoadOptions();

// Créer un nouvel objet Document et charger le fichier SVG
$document = new Document($inputFile, $loadOption);

// Enregistrer le document en tant que fichier PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir le format SVG en PDF en ligne**

Aspose.PDF pour PHP vous présente l'application gratuite en ligne ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion SVG en PDF avec application gratuite](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF en PDF

**Aspose.PDF pour PHP** prend en charge le format de fichier, qu'il s'agisse d'une image <abbr title="Tag Image File Format">TIFF</abbr> à cadre unique ou à cadres multiples. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications Java.

TIFF ou TIF, Tagged Image File Format, représente des images matricielles destinées à être utilisées sur une variété de dispositifs conformes à cette norme de format de fichier. Une image TIFF peut contenir plusieurs cadres avec des images différentes. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une image TIFF à cadre unique ou à cadres multiples. Vous pouvez donc convertir l'image TIFF en PDF dans vos applications Java. Par conséquent, nous allons examiner un exemple de conversion d'une image TIFF multi-pages en document PDF multi-pages avec les étapes suivantes :

1. Créer un nouvel objet Document
1. Ajouter une nouvelle page au document
1. Définir les marges de la page à 0
1. Créer un nouvel objet Image
1. Définir le chemin du fichier de l'image TIFF d'entrée
1. Ajouter l'image à la page
1. Enregistrer le document en tant que fichier PDF

De plus, le code suivant montre comment convertir une image TIFF multi-pages ou à cadres multiples en PDF :

```php
// Créer un nouvel objet Document
$document = new Document();

// Ajouter une nouvelle page au document
$page = $document->getPages()->add();

// Définir les marges de la page à 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Créer un nouvel objet Image
$image = new Image();

// Définir le chemin du fichier de l'image TIFF d'entrée
$image->setFile($inputFile);

// Ajouter l'image à la page
$page->getParagraphs()->add($image);

// Enregistrer le document en tant que fichier PDF
$document->save($outputFile);
```