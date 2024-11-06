---
title: Ajouter une Image à un Fichier PDF Existant 
linktitle: Ajouter une Image
type: docs
weight: 10
url: fr/java/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant une bibliothèque Java.
lastmod: "2021-06-05"
---

Chaque page PDF contient des propriétés de Ressources et de Contenu. Les ressources peuvent être des images et des formulaires par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son nom et son argument. Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Pour ajouter une image à un fichier PDF existant :

- Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrez le document PDF d'entrée.
- Obtenez la page à laquelle vous souhaitez ajouter une image.
- Ajoutez l'image dans la collection [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) de la page.
- Utilisez des opérateurs pour placer l'image sur la page :
- Utilisez l'opérateur GSave pour enregistrer l'état graphique actuel.

- Utilisez l'opérateur [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) pour spécifier où l'image doit être placée.
- Utilisez l'opérateur [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) pour dessiner l'image sur la page.
- Enfin, utilisez l'opérateur [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) pour sauvegarder l'état graphique mis à jour.
- Enregistrez le fichier.

Le code suivant montre comment ajouter l'image dans un document PDF.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Ouvrir un document
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Définir les coordonnées
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Obtenir la page à laquelle vous souhaitez ajouter l'image
        Page page = pdfDocument1.getPages().get_Item(1);

        // Charger l'image dans le flux
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Ajouter une image à la collection Images des ressources de la page
        page.getResources().getImages().add(imageStream);

        // Utiliser l'opérateur GSave : cet opérateur sauvegarde l'état graphique actuel
        page.getContents().add(new GSave());

        // Créer des objets Rectangle et Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Utiliser l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment
        // l'image doit être placée
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Utiliser l'opérateur Do : cet opérateur dessine l'image
        page.getContents().add(new Do(ximage.getName()));

        // Utiliser l'opérateur GRestore : cet opérateur restaure l'état graphique
        page.getContents().add(new GRestore());

        // Enregistrer le nouveau PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Fermer le flux d'image
        imageStream.close();
    }
```


## Ajout d'une image à partir de BufferedImage dans un PDF

Depuis la version 9.5.0 d'Aspose.PDF pour Java, nous avons introduit la prise en charge de l'ajout d'une image à partir d'une instance BufferedImage dans un document PDF. Pour répondre à cette exigence, une méthode est implémentée : [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
Vous pouvez utiliser n'importe quel InputStream et pas seulement un objet FileInputStream pour ajouter une image. Ainsi, en utilisant l'objet java.io.ByteArrayInputStream, vous n'avez pas besoin de stocker des fichiers sur le système :

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## Ajouter une Image dans un Fichier PDF Existant (Facades)

Il existe également une alternative plus simple pour ajouter une image à un fichier PDF. Vous pouvez utiliser la méthode AddImage de la classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). La méthode AddImage nécessite l'image à ajouter, le numéro de la page à laquelle l'image doit être ajoutée et les informations de coordonnées. Après cela, enregistrez le fichier PDF mis à jour en utilisant la méthode Close.

Le code suivant vous montre comment ajouter une image dans un fichier PDF existant.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Ouvrir le document
        PdfFileMend mender = new PdfFileMend();

        // Créer un objet PdfFileMend pour ajouter du texte
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Ajouter une image dans le fichier PDF
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Enregistrer les modifications
        mender.save(_dataDir + "AddImage_out.pdf");

        // Fermer l'objet PdfFileMend
        mender.close();
    }
```


## Ajouter la référence d'une seule image plusieurs fois dans un document PDF

Parfois, nous avons besoin d'utiliser la même image plusieurs fois dans un document PDF. Ajouter une nouvelle instance augmente le document PDF résultant. Nous avons ajouté une nouvelle méthode XImageCollection.add(XImage) qui prend en charge l'objet Ximage pour l'ajouter dans la collection d'images. Cette méthode permet d'ajouter une référence au même objet PDF que l'image originale, ce qui optimise la taille du document PDF.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## Identifier si l'image à l'intérieur du PDF est en couleur ou en noir et blanc

Différents types de compression peuvent être appliqués aux images pour réduire leur taille. Le type de compression appliqué à une image dépend de l'espace colorimétrique de l'image source, c'est-à-dire que si l'image est en couleur (RGB), alors une compression JPEG2000 est appliquée, et si elle est en noir et blanc, une compression JBIG2/JBIG2000 doit être appliquée. Par conséquent, identifier chaque type d'image et utiliser un type de compression approprié créera un résultat optimal.

Un fichier PDF peut contenir des éléments tels que du texte, des images, des graphiques, des pièces jointes, des annotations, etc., et si le fichier PDF source contient des images, nous pouvons déterminer l'espace colorimétrique de l'image et appliquer une compression appropriée pour réduire la taille du fichier PDF. Le code suivant montre les étapes pour identifier si l'image à l'intérieur du PDF est en couleur ou en noir et blanc.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // itérer à travers toutes les pages du fichier PDF
            for (Page page : (Iterable<Page>) document.getPages()) {
                // créer une instance de Image Placement Absorber
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* Type de Couleur */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Image en niveaux de gris");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Image en couleur");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Erreur de lecture du fichier = " + document.getFileName());
        }
    }
}
```