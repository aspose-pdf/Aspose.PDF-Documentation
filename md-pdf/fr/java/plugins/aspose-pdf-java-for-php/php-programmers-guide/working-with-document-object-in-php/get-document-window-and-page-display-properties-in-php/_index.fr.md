---
title: Obtenir les Propriétés de Fenêtre et d'Affichage de Page du Document en PHP
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir les Propriétés de Fenêtre et d'Affichage de Page du Document

Pour obtenir les propriétés de fenêtre et d'affichage de page d'un document PDF en utilisant **Aspose.PDF Java for PHP**, il suffit d'invoquer la classe **GetDocumentWindow**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtenir différentes propriétés du document
# Position de la fenêtre du document - Par défaut : false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Ordre de lecture prédominant ; détermine la position de la page
# lorsqu'elle est affichée côte à côte - Par défaut : L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Si la barre de titre de la fenêtre doit afficher le titre du document.
# Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
# la première page affichée - Par défaut : false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Si la barre de menu de l'application de visualisation doit être masquée - Par défaut : false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Si la barre d'outils de l'application de visualisation doit être masquée - Par défaut : false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Si les éléments de l'interface utilisateur comme les barres de défilement doivent être masqués
# et laisser uniquement le contenu de la page affiché - Par défaut : false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# Le mode page du document. Comment afficher le document en quittant le mode plein écran.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# La mise en page, c'est-à-dire une seule page, une colonne
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# Comment le document doit être affiché lorsqu'il est ouvert.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Télécharger le Code Exécuté**

Télécharger **Obtenez les Propriétés de la Fenêtre et de l'Affichage de la Page du Document (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)