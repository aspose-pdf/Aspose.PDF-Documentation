---
title: Formatage du Document PDF
linktitle: Formatage du Document PDF
type: docs
weight: 20
url: /fr/php-java/formatting-pdf-document/
description: Formater le Document PDF avec Aspose.PDF pour PHP via Java. Utilisez l'extrait de code suivant pour résoudre vos tâches.
lastmod: "2024-06-05"
---

## Obtenir les Propriétés de la Fenêtre du Document et de l'Affichage des Pages

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation et comment les pages sont affichées.

Pour définir ces différentes propriétés, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Vous pouvez maintenant obtenir les méthodes de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), telles que

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centrer la fenêtre du document à l'écran. Par défaut : false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Ordre de lecture.
 Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Afficher le titre du document dans la barre de titre de la fenêtre du document. Par défaut : faux (le titre est affiché).
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – Obtient le drapeau spécifiant si la barre de menu doit être cachée lorsque le document est actif.
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – Obtient le drapeau spécifiant si la barre d'outils doit être cachée lorsque le document est actif.
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – Obtient le drapeau spécifiant si les éléments de l'interface utilisateur doivent être cachés lorsque le document est actif.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – Obtient le mode de page, spécifiant comment afficher le document lors de la sortie du mode plein écran.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – La mise en page.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – Obtient le mode de page, spécifiant comment le document doit être affiché lorsqu'il est ouvert.

Le code suivant vous montre comment obtenir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // Ouvrir le document
    $document = new Document($inputFile);

    // Obtenir différentes propriétés du document
    // Position de la fenêtre du document - Par défaut : false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Ordre de lecture prédominant; déterminer la position de la page
    // lorsqu'elle est affichée côte à côte - Par défaut : L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Si la barre de titre de la fenêtre doit afficher le titre du document.
    // Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
    // la première page affichée - Par défaut : false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Si la barre de menu de l'application de visualisation doit être masquée - Par défaut : false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Si la barre d'outils de l'application de visualisation doit être masquée - Par défaut : false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Si les éléments d'interface utilisateur comme les barres de défilement doivent être masqués
    // et ne laisser que le contenu de la page affiché - Par défaut : false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // Le mode de page du document. Comment afficher le document en quittant
    // le mode plein écran.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // La mise en page du document c'est-à-dire page unique, une colonne
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // Comment le document doit être affiché lorsqu'il est ouvert.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## Définir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage des pages.

Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

Les méthodes disponibles sont :

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

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    // Définir différentes propriétés du document
    // spécifier pour positionner la fenêtre du document - Par défaut : false
    $document->setCenterWindow(true);
    // Ordre de lecture prédominant ; détermine la position de la page
    // lorsqu'elle est affichée côte à côte - Par défaut : L2R
    $document->setDirection(Direction::$R2L);
    // Spécifier si la barre de titre de la fenêtre doit afficher le titre du document
    // si false, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    $document->setDisplayDocTitle(true);
    // Spécifier si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
    // la première page affichée - Par défaut : false
    $document->setFitWindow(true);
    // Spécifier si la barre de menu de l'application de visualisation doit être masquée - Par défaut :
    // false
    $document->setHideMenubar(true);
    // Spécifier si la barre d'outils de l'application de visualisation doit être masquée - Par défaut :
    // false
    $document->setHideToolBar(true);
    // Spécifier si les éléments d'interface utilisateur comme les barres de défilement doivent être masqués
    // et laisser uniquement le contenu de la page affiché - Par défaut : false
    $document->setHideWindowUI(true);
    // Mode de la page du document. spécifier comment afficher le document lors de la sortie
    // du mode plein écran.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Spécifier la mise en page de la page, c'est-à-dire page unique, une colonne
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Spécifier comment le document doit s'afficher lorsqu'il est ouvert
    // c'est-à-dire afficher les vignettes, plein écran, afficher le panneau des pièces jointes
    $document->setPageMode(PageMode::$UseThumbs);
    // Enregistrer le fichier PDF mis à jour
    $document->save($outputFile);
    $document->close();

```


## Incorporation de polices dans un fichier PDF existant

Les lecteurs PDF prennent en charge [un noyau de 14 polices](http://fr.wikipedia.org/wiki/Portable_Document_Format#Fonts) afin que les documents puissent être affichés de la même manière, quel que soit le plateau sur lequel le document est affiché. Lorsqu'un PDF contient une police qui est en dehors des polices de base, incorporez la police pour éviter la substitution de police.

Aspose.PDF pour PHP via Java prend en charge l'incorporation de polices dans les documents PDF existants. Vous pouvez intégrer une police complète ou un sous-ensemble. Pour incorporer la police :

1. Ouvrez un fichier PDF existant en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utilisez la classe [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) pour incorporer la police.
   1. La méthode setEmbedded(true) intègre la police complète.
   1. La [méthode isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) intègre un sous-ensemble de la police.

Un sous-ensemble de police n'intègre que les caractères qui sont utilisés et est utile lorsque les polices sont utilisées pour des phrases courtes ou des slogans, par exemple lorsqu'une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal.
 Utiliser un sous-ensemble réduit la taille du fichier du PDF de sortie.

Cependant, si une police personnalisée est utilisée pour le texte principal, intégrez-la dans son intégralité.

Le fragment de code suivant montre comment intégrer une police dans un fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // Vérifier si la police est déjà intégrée
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Vérifier les objets Form
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // Vérifier si la police est déjà intégrée
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // Enregistrer le fichier PDF mis à jour
    $document->save($outputFile);
    $document->close();
```

## Incorporation des polices lors de la création de PDF

Si vous devez utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez incorporer la description de la police lors de la génération d'un fichier PDF. Si les informations sur la police ne sont pas incorporées, Adobe Reader les prendra à partir du système d'exploitation si elles sont installées, ou il construira une police de substitution selon le descripteur de police dans le PDF. Veuillez noter que la police incorporée doit être installée sur la machine hôte, c'est-à-dire que dans le cas du code suivant, la police 'Univers Condensed' est installée sur le système.

Nous utilisons la propriété setEmbedded de la classe [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) pour incorporer les informations de police dans le fichier PDF. Définir la valeur de cette propriété à 'true' incorporera le fichier complet de la police dans le PDF, sachant que cela augmentera la taille du fichier PDF. Voici l'extrait de code qui peut être utilisé pour incorporer les informations de police dans le PDF.

```php

    // Instancier un objet PDF en appelant son constructeur vide
    $document = new Document();

    // Créer une section dans l'objet Pdf
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("Ceci est un texte d'exemple utilisant une police personnalisée.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // Enregistrer le fichier PDF mis à jour
    $document->save($outputFile);
    $document->close();
```


## Définir le nom de la police par défaut lors de l'enregistrement du PDF

Lorsqu'un document PDF contient des polices qui ne sont ni disponibles dans le document lui-même ni sur l'appareil, l'API remplace ces polices par la police par défaut. Lorsqu'une police est disponible (installée sur l'appareil ou intégrée dans le document), le PDF de sortie doit avoir la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (et non le chemin vers les fichiers de police). Nous avons implémenté une fonctionnalité pour définir le nom de la police par défaut lors de l'enregistrement d'un document en tant que PDF. Le code suivant peut être utilisé pour définir la police par défaut :

```php

    // Charger un document PDF existant
    $document = new Document($inputFile);
    $newName = "Arial";

    // Initialiser les options de sauvegarde pour le format PDF
    $ops = new PdfSaveOptions();

    // Définir le nom de la police par défaut
    $ops->setDefaultFontName($newName);

    // Enregistrer le fichier PDF
    $document->save($outputFile, $ops);
    // Enregistrer le fichier PDF mis à jour
    $document->close();
```

## Obtenir toutes les polices du document PDF

Si vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode **Document.getFontUtilities().getAllFonts()** fournie dans la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 Veuillez vérifier l'extrait de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```php

    // Charger un document PDF existant
    $document = new Document($inputFile);

    // Obtenez toutes les polices du document
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Enregistrez le fichier PDF mis à jour
    $document->close();
```

## Obtenir-Définir le facteur de zoom du fichier PDF

Parfois, vous souhaitez définir ou obtenir le facteur de zoom d'un document PDF. Vous pouvez facilement accomplir cette tâche avec Aspose.PDF.

L'objet [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) vous permet d'obtenir la valeur de zoom associée à un fichier PDF. De même, il peut être utilisé pour définir le facteur de zoom d'un fichier.

```php

    // Charger un document PDF existant
    $document = new Document($inputFile);

    // Créer un objet GoToAction
    $action = $document->getOpenAction();

    // Obtenez le facteur de zoom du fichier PDF
    $responseData = $action->getDestination()->getZoom();

    // Enregistrez le fichier PDF mis à jour
    $document->close();  
```

Le fragment de code suivant montre comment obtenir le facteur de zoom d'un fichier PDF.

```php

    // Charger un document PDF existant
    $document = new Document($inputFile);
    $zoom = 0.5;
    // définir le facteur de zoom du document
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // définir l'action pour ajuster à la largeur de la page avec zoom
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // définir l'action pour ajuster à la hauteur de la page avec zoom
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Enregistrer le fichier PDF mis à jour
    $document->save($outputFile);
    $document->close();  
```