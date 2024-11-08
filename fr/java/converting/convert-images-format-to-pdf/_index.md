---
title: Convertir divers formats d'images en PDF 
linktitle: Convertir des images en PDF
type: docs
weight: 60
url: /fr/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet montre comment la bibliothèque Aspose.PDF pour Java permet de convertir divers formats d'images en PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF pour Java** vous permet de convertir différents formats d'images en fichiers PDF. Notre bibliothèque démontre des extraits de code pour convertir les formats d'image les plus populaires, tels que - BMP, CGM, DICOM, EMF, JPG, PNG, SVG et TIFF.

## Convertir BMP en PDF

Convertir des fichiers BMP en document PDF en utilisant la bibliothèque **Aspose.PDF pour Java**.

Les images <abbr title="Bitmap Image File">BMP</abbr> sont des fichiers ayant l'extension .BMP qui représentent des fichiers d'image bitmap utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant de l'appareil (DIB).
Vous pouvez convertir BMP en PDF avec l'API Aspose.PDF pour Java.
 Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

1. Initialisez un nouveau Document
1. Chargez le fichier image BMP d'exemple
1. Enfin, enregistrez le fichier PDF de sortie

Ainsi, l'extrait de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant Java :

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialisez l'objet document
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Chargez le fichier image BMP d'exemple
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Enregistrez le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir BMP en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion BMP en PDF en utilisant l'application gratuite](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM en PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> est une norme ISO qui fournit un format de fichier d'image 2D basé sur des vecteurs pour le stockage et la récupération d'informations graphiques. CGM est un format indépendant des dispositifs. CGM est un format de graphiques vectoriels qui prend en charge trois méthodes d'encodage différentes : binaire (meilleur pour la vitesse de lecture par le programme), basé sur les caractères (produit la plus petite taille de fichier et permet des transferts de données plus rapides) ou l'encodage en texte clair (permet aux utilisateurs de lire et de modifier le fichier avec un éditeur de texte).

Le code suivant vous montre comment convertir des fichiers CGM au format PDF en utilisant Aspose.PDF pour Java.

1. Créez une classe [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. Créez une instance de la classe [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) avec le nom de fichier source mentionné et les options.
1. Enregistrez le document avec le nom de fichier souhaité.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Créer une CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // Initialiser l'objet document
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## Convertir DICOM en PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est une norme pour gérer, stocker, imprimer et transmettre des informations en imagerie médicale. Elle inclut une définition de format de fichier et un protocole de communication réseau.

Aspsoe.PDF pour Java vous permet de convertir des fichiers DICOM en format PDF, consultez l'extrait de code suivant :

1. Charger l'image dans le flux
1. Initialiser [l'objet Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Charger le fichier d'image DICOM d'exemple
1. Enregistrer le document PDF de sortie

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Charger l'image dans le flux
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Initialiser l'objet document
        Document document = new Document();
        document.getPages().add();
        
        // Charger le fichier d'image DICOM d'exemple
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Essayez de convertir DICOM en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion DICOM en PDF avec une application gratuite](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF en PDF

Le format de métafichier amélioré (<abbr title="Enhanced metafile format">EMF</abbr>) stocke des images graphiques indépendamment de l'appareil. Les métafichiers EMF se composent de records de longueur variable dans un ordre chronologique qui peuvent rendre l'image stockée après analyse sur n'importe quel appareil de sortie.

Nous avons plusieurs approches pour convertir EMF en PDF.

## Utilisation de la classe Image

Un document PDF comprend des pages et chaque page contient un ou plusieurs objets paragraphe. Un paragraphe peut être un texte, une image, un tableau, une boîte flottante, un graphique, un titre, un champ de formulaire ou une pièce jointe.

Pour convertir un fichier image au format PDF, incluez-le dans un paragraphe.

Il est possible de convertir des images à un emplacement physique sur le disque dur local, trouvées à une URL Web ou dans une instance Stream.

Pour ajouter une image :

1. Créez un objet de la classe com.aspose.pdf.Image.
1. Ajoutez l'image à une collection [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de l'instance de page.
1. Spécifiez le chemin ou la source de l'image.
    - Si une image se trouve à un emplacement sur le disque dur, spécifiez l'emplacement du chemin à l'aide de la méthode [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Si une image est placée dans un FileInputStream, passez l'objet contenant l'image à la méthode [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Le code ci-dessous montre comment charger un objet image, définir la marge de la page, placer l'image sur la page et enregistrer le résultat au format PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Convertir EMF en PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Instancier l'objet Document
        Document doc = new Document();
        // Ajouter une page à la collection de pages du document
        Page page = doc.getPages().add();
        // Charger le fichier image source dans un objet Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Définir les marges pour que l'image s'adapte, etc.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Créer un objet image
        Image image1 = new Image();
        // Ajouter l'image dans la collection de paragraphes de la section
        page.getParagraphs().add(image1);
        // Définir le flux de fichier image
        image1.setImageStream(fs);
        // Enregistrer le fichier PDF résultant
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // voir code ci-dessous
    } 
}
```


### Ajouter une image à partir de BufferedImage

Aspose.PDF pour Java offre également la fonctionnalité de charger une image à partir d'une instance Stream où une image peut être chargée dans un objet BufferedImage et peut être placée à l'intérieur de la collection de paragraphes d'un fichier Pdf.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // ajouter une page à la collection de pages du fichier Pdf
    Page page = doc.getPages().add();
    // créer une instance d'image
    Image image1 = new Image();
    // créer une instance BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // écrire l'image tamponnée dans une instance OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // ajouter l'image à la collection de paragraphes de la première page
    page.getParagraphs().add(image1);
    // définir le flux d'image comme OutputStream contenant l'image tamponnée
    image1.setImageStream(bais);
    // enregistrer le fichier PDF résultant
    doc.save("BufferedImage.pdf");
}
```


## Ajouter une image en utilisant les opérateurs PDF

Chaque objet de page PDF contient les méthodes [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) et [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). Les ressources peuvent être des images et des formulaires, par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son propre nom et argument.

Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Pour ajouter une image à un fichier PDF existant :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrez le document PDF d'entrée.
1. Obtenez la page à laquelle vous souhaitez ajouter une image.
1. Ajoutez l'image dans la collection [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) de la page.
1. Utilisez les opérateurs pour placer l'image sur la page :
   1. Utilisez l'opérateur GSave pour enregistrer l'état graphique actuel.
   1. Utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.

1. Utilisez l'opérateur Do pour dessiner l'image sur la page.
   1. Enfin, utilisez l'opérateur GRestore pour enregistrer l'état graphique mis à jour.
1. Enregistrez le fichier.

Le code suivant montre comment ajouter une image à un document PDF.

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Ouvrir un document
Document pdfDocument1 = new Document("input.pdf");

// Définir les coordonnées
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtenez la page à laquelle vous souhaitez ajouter l'image
Page page = pdfDocument1.getPages().get_Item(1);

// Charger l'image dans le flux
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Ajouter une image à la collection d'images des ressources de la page
page.getResources().getImages().add(imageStream);

// Utilisation de l'opérateur GSave : cet opérateur enregistre l'état graphique actuel
page.getContents().add(new Operator.GSave());

// Créer des objets Rectangle et Matrix
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Utilisation de l'opérateur ConcatenateMatrix (concatenation de matrice) : définit comment l'image doit être placée
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Utilisation de l'opérateur Do : cet opérateur dessine l'image
page.getContents().add(new Operator.Do(ximage.getName()));

// Utilisation de l'opérateur GRestore : cet opérateur restaure l'état graphique
page.getContents().add(new Operator.GRestore());

// Enregistrez le nouveau PDF
pdfDocument1.save("Updated_document.pdf");

// Fermer le flux d'image
imageStream.close();
```


{{% alert color="success" %}}
**Essayez de convertir EMF en PDF en ligne**

Aspose vous propose une application en ligne gratuite ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion EMF en PDF en utilisant l'application gratuite](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir JPG en PDF

Pas besoin de se demander comment convertir JPG en PDF, car la bibliothèque Apose.PDF pour Java a la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour Java en suivant les étapes :

1. Initialisez l'objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Chargez l'image JPG et ajoutez-la au paragraphe
1. Enregistrez le PDF de sortie

Le code ci-dessous montre comment convertir une image JPG en PDF en utilisant Java :

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialiser l'objet document
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Charger le fichier image JPEG exemple
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Essayez de convertir JPG en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion JPG en PDF en utilisant l'application gratuite](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG en PDF

**Aspose.PDF pour Java** prend en charge la fonctionnalité de conversion des images PNG au format PDF. Consultez le prochain extrait de code pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> fait référence à un type de format de fichier d'image raster qui utilise une compression sans perte, ce qui le rend populaire parmi ses utilisateurs.

Vous pouvez convertir PNG en image PDF en suivant les étapes ci-dessous :

1. Charger l'image PNG d'entrée
1. Lire les valeurs de hauteur et de largeur
1. Créer un nouveau document et ajouter une page
1. Définir les dimensions de la page
1. Enregistrer le fichier de sortie

De plus, l'extrait de code ci-dessous montre comment convertir PNG en PDF dans vos applications Java :

```java
package com.aspose.pdf.examples;

/**
 * Convertir PNG en PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialiser l'objet document
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Charger le fichier image BMP d'exemple
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**Essayez de convertir PNG en PDF en ligne**

Aspose vous présente une application en ligne gratuite ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion PNG en PDF en utilisant l'application gratuite](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG en PDF

Scalable Vector Graphics (SVG) est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML.
 Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

## Comment convertir un fichier SVG en format PDF

Pour convertir des fichiers SVG en PDF, utilisez la classe nommée [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) qui est utilisée pour initialiser l'objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Plus tard, cet objet est passé en argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

L'extrait de code suivant montre le processus de conversion d'un fichier SVG au format PDF.

```java
// Initialiser l'objet document

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**Essayez de convertir le format SVG en PDF en ligne**

Aspose.PDF pour Java vous présente une application gratuite en ligne ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de SVG en PDF avec l'application gratuite](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF en PDF

**Aspose.PDF pour Java** prend en charge le format de fichier, qu'il s'agisse d'une image <abbr title="Tag Image File Format">TIFF</abbr> à un seul cadre ou multi-cadres. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications Java.

TIFF ou TIF, Tagged Image File Format, représente des images raster destinées à être utilisées sur une variété d'appareils conformes à cette norme de format de fichier.
 TIFF image peut contenir plusieurs cadres avec différentes images. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une image TIFF à un seul cadre ou à plusieurs cadres. Vous pouvez donc convertir l'image TIFF en PDF dans vos applications Java. Par conséquent, nous allons examiner un exemple de conversion d'une image TIFF multipage en document PDF multipage avec les étapes ci-dessous :

1. Instancier une instance de la classe Document
1. Charger l'image TIFF en entrée
1. Enfin, enregistrer l'image comme page PDF

De plus, l'extrait de code suivant montre comment convertir une image TIFF multipage ou à plusieurs cadres en PDF :

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir TIFF en PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // Initialiser l'objet document
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```