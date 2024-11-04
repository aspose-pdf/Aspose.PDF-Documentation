---  
title: Formatting PDF Document  
linktitle: Formatting PDF Document  
type: docs  
weight: 20  
url: /java/formatting-pdf-document/  
description: Formatez le document PDF avec Aspose.PDF pour Java. Utilisez le prochain extrait de code pour résoudre vos tâches.  
lastmod: "2021-06-05"  
---

## Obtenir les propriétés de la fenêtre du document et de l'affichage de la page

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visionnage, et comment les pages sont affichées.

Pour définir ces différentes propriétés, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Vous pouvez maintenant obtenir les méthodes de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), telles que

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centrer la fenêtre du document à l'écran. Par défaut : faux.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Ordre de lecture.
 Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.

- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Afficher le titre du document dans la barre de titre de la fenêtre du document. Par défaut : faux (le titre est affiché).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : faux (la barre de menu est affichée).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : faux (la barre d'outils est affichée).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Masquer ou afficher les éléments de la fenêtre du document comme les barres de défilement. Par défaut : faux (les éléments de l'interface utilisateur sont affichés).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – Comment le document est affiché lorsqu'il n'est pas affiché en mode plein écran.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – La mise en page.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – Comment le document est affiché lors de la première ouverture. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le code suivant vous montre comment obtenir les propriétés à l'aide de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Obtenir différentes propriétés du document
    // Position de la fenêtre du document - Par défaut : false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Ordre de lecture prédominant ; déterminer la position de la page
    // lorsqu'elle est affichée côte à côte - Par défaut : L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Si la barre de titre de la fenêtre doit afficher le titre du document.
    // Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // S'il faut redimensionner la fenêtre du document pour s'adapter à la taille de
    // la première page affichée - Par défaut : false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // S'il faut masquer la barre de menus de l'application de visualisation - Par défaut : false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // S'il faut masquer la barre d'outils de l'application de visualisation - Par défaut : false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // S'il faut masquer les éléments de l'interface utilisateur comme les barres de défilement
    // et laisser uniquement le contenu de la page affiché - Par défaut : false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // Le mode de page du document. Comment afficher le document lors de la sortie
    // du mode plein écran.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // La mise en page du document, c'est-à-dire une seule page, une colonne
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // Comment le document doit être affiché lorsqu'il est ouvert.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## Définir les Propriétés de la Fenêtre du Document et de l'Affichage de la Page

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage de la page.

Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

Les propriétés disponibles sont :

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

Le code suivant vous montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // Définir différentes propriétés du document
    // spécifier pour positionner la fenêtre du document - Par défaut : false
    pdfDocument.setCenterWindow(true);
    
    // Ordre de lecture prédominant ; déterminer la position de la page
    // lorsqu'elle est affichée côte à côte - Par défaut : L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // Spécifier si la barre de titre de la fenêtre doit afficher le titre du document
    // si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    pdfDocument.setDisplayDocTitle(true);
    
    // Spécifier si redimensionner la fenêtre du document pour s'adapter à la taille de
    // la première page affichée - Par défaut : false
    pdfDocument.setFitWindow(true);
    
    // Spécifier si masquer la barre de menu de l'application de visualisation - Par défaut :
    // false
    pdfDocument.setHideMenubar(true);
    
    // Spécifier si masquer la barre d'outils de l'application de visualisation - Par défaut :
    // false
    pdfDocument.setHideToolBar(true);
    
    // Spécifier si masquer les éléments UI comme les barres de défilement
    // et laisser seulement le contenu de la page affiché - Par défaut : false
    pdfDocument.setHideWindowUI(true);
    
    // Mode page du document. spécifier comment afficher le document lors de la sortie
    // du mode plein écran.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // Spécifier la mise en page, c'est-à-dire une seule page, une colonne
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // Spécifier comment le document doit s'afficher lors de son ouverture
    // c'est-à-dire afficher les miniatures, en plein écran, afficher le panneau de pièces jointes
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // Enregistrer le fichier PDF mis à jour
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## Incorporation de Polices dans un Fichier PDF Existant

Les lecteurs PDF prennent en charge [un noyau de 14 polices](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) afin que les documents puissent être affichés de la même manière, quel que soit le plateforme sur laquelle le document est affiché. Lorsqu'un PDF contient une police qui n'est pas dans les polices de base, intégrez la police pour éviter la substitution de police.

Aspose.PDF pour Java prend en charge l'incorporation de polices dans les documents PDF existants. Vous pouvez incorporer une police complète ou un sous-ensemble. Pour incorporer la police :

1. Ouvrez un fichier PDF existant en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utilisez la classe [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) pour intégrer la police.
   1. La méthode setEmbedded(true) intègre la police complète.
   1. La méthode pageFont.isSubset(true) intègre un sous-ensemble de la police.

Un sous-ensemble de police intègre uniquement les caractères utilisés et est utile lorsque les polices sont utilisées pour de courtes phrases ou slogans, par exemple lorsque une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal.
 Utiliser un sous-ensemble réduit la taille du fichier du PDF de sortie.

Cependant, si une police personnalisée est utilisée pour le texte principal, intégrez-la dans son intégralité.

Le snippet de code suivant montre comment intégrer une police dans un fichier PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Itérer à travers toutes les pages
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Vérifier si la police est déjà intégrée
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Vérifier les objets Form
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Vérifier si la police est intégrée
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Sauvegarder le fichier PDF mis à jour
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Incorporation des polices lors de la création de PDF

Si vous avez besoin d'utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez inclure la description de la police lors de la génération d'un fichier PDF. Si les informations sur la police ne sont pas incorporées, Adobe Reader les prendra à partir du système d'exploitation si elles sont installées sur le système, ou il construira une police de remplacement selon le descripteur de police dans le PDF. Veuillez noter que la police incorporée doit être installée sur la machine hôte, c'est-à-dire que dans le cas du code suivant, la police 'Univers Condensed' est installée sur le système.

Nous utilisons la propriété setEmbedded de la classe [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) pour incorporer les informations de police dans le fichier PDF. Définir la valeur de cette propriété sur 'true' incorporera le fichier de police complet dans le PDF, sachant que cela augmentera la taille du fichier PDF. Voici l'extrait de code qui peut être utilisé pour incorporer les informations de police dans le PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Instancier l'objet PDF en appelant son constructeur vide
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Créer une section dans l'objet Pdf
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" Ceci est un texte d'exemple utilisant une police personnalisée.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Enregistrer le fichier PDF mis à jour
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Définir le nom de police par défaut lors de l'enregistrement du PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui-même et sur l'appareil, l'API remplace ces polices par la police par défaut. Lorsqu'une police est disponible (installée sur l'appareil ou intégrée dans le document), le PDF de sortie doit avoir la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (et non le chemin vers les fichiers de police). Nous avons implémenté une fonctionnalité pour définir le nom de la police par défaut lors de l'enregistrement d'un document en tant que PDF. Le code suivant peut être utilisé pour définir la police par défaut :

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Charger un document PDF existant
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Initialiser les options d'enregistrement pour le format PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // Définir le nom de la police par défaut
    ops.setDefaultFontName(newName);

    // Enregistrer le fichier PDF
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## Obtenir Toutes les Polices d'un Document PDF

Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode **Document.getFontUtilities().getAllFonts()** fournie dans la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Veuillez consulter l'extrait de code suivant pour obtenir toutes les polices d'un document PDF existant :

```java
public static void GetAllFontsFromPDFDocument() {

    // Charger un document PDF existant
    Document document = new Document(_dataDir + "sample.pdf");

    // Obtenir toutes les polices du document
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## Obtenir-Définir le Facteur de Zoom du Fichier PDF

Parfois, vous souhaitez définir ou obtenir le facteur de zoom d'un document PDF. Vous pouvez facilement accomplir cette exigence avec Aspose.PDF.

L'objet [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) vous permet d'obtenir la valeur de zoom associée à un fichier PDF.
 Similairement, il peut être utilisé pour définir le facteur de zoom d'un fichier.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Charger un document PDF existant
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // définir le facteur de zoom du document
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // définir l'action pour s'adapter à la largeur de la page en zoom
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // définir l'action pour s'adapter à la hauteur de la page en zoom
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // Instancier un nouvel objet Document
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Créer un objet GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Obtenir le facteur de zoom du fichier PDF
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Enregistrer le fichier PDF mis à jour
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```