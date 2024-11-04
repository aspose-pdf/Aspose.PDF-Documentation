---
title: Obtenir les propriétés de la fenêtre du document et de l'affichage de la page en Ruby
type: docs
weight: 40
url: /java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir les propriétés de la fenêtre du document et de l'affichage de la page

Pour obtenir les propriétés de la fenêtre du document et de l'affichage de la page d'un document Pdf en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **GetDocumentWindow**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtenez différentes propriétés du document

# Position de la fenêtre du document - Par défaut : false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Ordre de lecture prédominant; détermine la position de la page

# lorsqu'affichée côte à côte - Par défaut : L2R

puts "Direction :- " + doc.getDirection().to_s

# Si la barre de titre de la fenêtre doit afficher le titre du document.

# Si false, la barre de titre affiche le nom du fichier PDF - Par défaut : false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de

# la première page affichée - Par défaut : false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Si la barre de menu de l'application de visualisation doit être masquée - Par défaut : false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Si la barre d'outils de l'application de visualisation doit être masquée - Par défaut : false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Si les éléments de l'interface utilisateur comme les barres de défilement doivent être masqués

# et ne laisser que le contenu de la page affiché - Par défaut : false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# Le mode page du document. Comment afficher le document en quittant le mode plein écran.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# La mise en page, c'est-à-dire une seule page, une colonne

puts "PageLayout :-" + doc.getPageLayout().to_s

# Comment le document doit s'afficher lorsqu'il est ouvert.

puts "pageMode :-" + doc.getPageMode().to_s
```


## Téléchargement du code en cours d'exécution

Téléchargez **Obtenez les propriétés de la fenêtre et de l'affichage de la page du document (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)