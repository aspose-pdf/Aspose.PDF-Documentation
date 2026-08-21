---
title: Obtenir les propriétés d'affichage de la fenêtre du document et de la page dans Ruby
linktitle: Obtenir les propriétés d'affichage de la fenêtre du document et de la page dans Ruby
type: docs
weight: 40
url: /java/get-document-window-and-page-display-properties-in-ruby/
description: Récupérez et personnalisez les propriétés d'affichage de la fenêtre du document et des pages dans les fichiers PDF à l'aide de Ruby et Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir les propriétés d'affichage de la fenêtre du document et de la page



Pour obtenir les propriétés d'affichage de la fenêtre et de la page du document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **GetDocumentWindow**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get different document properties

# Position of document's window - Default: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Predominant reading order; determine the position of page

# when displayed side by side - Default: L2R

puts "Direction :- " + doc.getDirection().to_s

# Whether window's title bar should display document title.

# If false, title bar displays PDF file name - Default: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Whether to resize the document's window to fit the size of

# first displayed page - Default: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Whether to hide menu bar of the viewer application - Default: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Whether to hide tool bar of the viewer application - Default: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Whether to hide UI elements like scroll bars

# and leaving only the page contents displayed - Default: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# The document's page mode. How to display document on exiting full-screen mode.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# The page layout i.e. single page, one column

puts "PageLayout :-" + doc.getPageLayout().to_s

# How the document should display when opened.

puts "pageMode :-" + doc.getPageMode().to_s
```

## 
Télécharger le code d'exécution



Téléchargez** Obtenez les propriétés d'affichage de la fenêtre et de la page du document (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)
