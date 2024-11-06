---
title: Définir les propriétés de la fenêtre du document et de l'affichage des pages en Ruby
type: docs
weight: 100
url: fr/java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Définir les propriétés de la fenêtre du document et de l'affichage des pages

Pour définir les propriétés de la fenêtre du document et de l'affichage des pages du document Pdf en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **SetDocumentWindow**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Définir différentes propriétés du document

# Position de la fenêtre du document - Par défaut : false

doc.setCenterWindow(true)

# Ordre de lecture prédominant ; détermine la position de la page

# lorsqu'elle est affichée côte à côte - Par défaut : L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Si la barre de titre de la fenêtre doit afficher le titre du document.

# Si false, la barre de titre affiche le nom du fichier PDF - Par défaut : false

doc.setDisplayDocTitle(true)

# Si redimensionner la fenêtre du document pour s'adapter à la taille de

# la première page affichée - Par défaut : false

doc.setFitWindow(true)

# Si masquer la barre de menu de l'application visionneuse - Par défaut : false

doc.setHideMenubar(true)

# Si masquer la barre d'outils de l'application visionneuse - Par défaut : false

doc.setHideToolBar(true)

# Si masquer les éléments de l'interface utilisateur comme les barres de défilement

# et ne laisser afficher que le contenu des pages - Par défaut : false

doc.setHideWindowUI(true)

# Le mode de page du document. Comment afficher le document à la sortie du mode plein écran.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# La mise en page, c'est-à-dire page unique, une colonne

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# Comment le document doit s'afficher à l'ouverture.

doc.setPageMode()

# Enregistrer le fichier PDF mis à jour

doc.save(data_dir + "Set Document Window.pdf")
```


## Télécharger le Code Exécutable

Téléchargez **Définir les Propriétés de la Fenêtre du Document et de l'Affichage de la Page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)