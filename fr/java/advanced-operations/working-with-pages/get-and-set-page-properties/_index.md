---
title: Obtenir et Définir les Propriétés de Page
type: docs
weight: 30
url: fr/java/get-and-set-page-properties/
description: Ce sujet explique comment obtenir des numéros dans un fichier PDF, obtenir les propriétés de page et déterminer la couleur de la page en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
---

Aspose.PDF pour Java vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications Java. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de la page.

## Obtenir le Nombre de Pages dans un Fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Ensuite, utilisez la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (à partir de l'objet Document) pour obtenir le nombre total de pages dans le document.

L'extrait de code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Obtenir le nombre de pages
        System.out.println("Nombre de pages : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Obtenir le nombre de pages sans enregistrer le document

À moins que le fichier PDF ne soit enregistré et que tous les éléments ne soient effectivement placés à l'intérieur du fichier PDF, nous ne pouvons pas obtenir le nombre de pages pour un document particulier (car nous ne pouvons pas être sûrs du nombre de pages dans lesquelles tous les éléments seront accommodés).
 Cependant, à partir de la version Aspose.PDF pour Java 10.1.0, nous avons introduit une méthode nommée [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) qui offre la fonctionnalité d'obtenir le nombre de pages d'un document PDF, sans enregistrer le fichier. Ainsi, nous pouvons obtenir des informations sur le nombre de pages à la volée. Veuillez essayer d'utiliser l'extrait de code suivant pour répondre à cette exigence.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // Pour des exemples complets et des fichiers de données, veuillez aller sur
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // instancier une instance de Document
        Document doc = new Document();
        // ajouter une page à la collection de pages du fichier PDF
        Page page = doc.getPages().add();
        // créer une boucle pour ajouter 300 instances de TextFragment
        for (int i = 0; i < 300; i++)
            // ajouter TextFragment à la collection de paragraphes de la première page du PDF
            page.getParagraphs().add(new TextFragment("Test de comptage des pages"));
        // traiter les paragraphes pour obtenir des informations sur le nombre de pages
        doc.processParagraphs();
        System.out.println("Nombre de pages dans le PDF = " + doc.getPages().size());
    }
```

## Obtenir les propriétés de la page

Chaque page dans un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, la boîte de fond perdu, de coupe et de rognage. Aspose.PDF vous permet d'accéder à ces propriétés.

### **Comprendre les propriétés de la page : la différence entre les propriétés Artbox, BleedBox, CropBox, MediaBox, TrimBox et Rect**

- **Boîte des médias** : La boîte des médias est la plus grande boîte de la page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la boîte des médias détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu** : Si le document a un fond perdu, le PDF aura également une boîte de fond perdu.
 Bleed est la quantité de couleur (ou l'œuvre) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille (« retaillé »), l'encre ira jusqu'au bord de la page. Même si la page est mal retaillée - coupée légèrement en dehors des repères de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Trim box**: La boîte de coupe indique la taille finale d'un document après impression et découpe.
- **Art box**: La boîte d'art est la boîte dessinée autour du contenu réel des pages dans vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box**: La boîte de rognage est la taille de "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de rognage sont affichés dans Adobe Acrobat.
  Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect**: l'intersection (rectangle communément visible) du MediaBox et du DropBox. L'image ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accéder aux propriétés de la page

La classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fournit toutes les propriétés relatives à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

À partir de là, il est possible d'accéder à des objets Page individuels en utilisant leur index, ou de parcourir la collection en boucle foreach pour obtenir toutes les pages. Une fois qu'une page individuelle est accédée, nous pouvons obtenir ses propriétés. Le code suivant montre comment obtenir les propriétés d'une page.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Obtenir la collection de pages
        PageCollection pageCollection = pdfDocument.getPages();

        // Obtenir une page spécifique
        Page pdfPage = pageCollection.get_Item(1);

        // Obtenir les propriétés de la page
        System.out.printf("\n ArtBox : Hauteur = " + pdfPage.getArtBox().getHeight() + ", Largeur = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Hauteur = " + pdfPage.getBleedBox().getHeight() + ", Largeur = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Hauteur = " + pdfPage.getCropBox().getHeight() + ", Largeur = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Hauteur = " + pdfPage.getMediaBox().getHeight() + ", Largeur = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Hauteur = " + pdfPage.getTrimBox().getHeight() + ", Largeur = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Hauteur = " + pdfPage.getRect().getHeight() + ", Largeur = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Numéro de page :- " + pdfPage.getNumber());
        System.out.printf("\n Rotation :-" + pdfPage.getRotate());
    }
```

## Déterminer la Couleur de la Page

La classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fournit les propriétés liées à une page particulière dans un document PDF, y compris le type de couleur - RGB, noir et blanc, niveaux de gris ou indéfini - utilisé par la page.

Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). La propriété [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur pour une page PDF particulière, utilisez la propriété [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) de l'objet de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

L'extrait de code suivant montre comment parcourir une page individuelle du fichier PDF pour obtenir des informations sur la couleur.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Itérer à travers toutes les pages du fichier PDF
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Obtenir les informations de type de couleur pour une page PDF particulière
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Page # -" + pageCount + " est en Noir et blanc..");
                break;
            case 1:
                System.out.println("Page # -" + pageCount + " est en Niveaux de gris...");
                break;
            case 0:
                System.out.println("Page # -" + pageCount + " est en RGB..");
                break;
            case 3:
                System.out.println("Page # -" + pageCount + " La couleur est indéfinie..");
                break;
            }
        }
    }
}
```