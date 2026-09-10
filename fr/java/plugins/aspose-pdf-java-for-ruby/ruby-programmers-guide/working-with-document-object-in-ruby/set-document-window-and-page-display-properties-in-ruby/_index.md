---
title: Définir les propriétés d'affichage de la fenêtre du document et de la page dans Ruby
linktitle: Définir les propriétés d'affichage de la fenêtre du document et de la page dans Ruby
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
description: Personnalisez les paramètres d'affichage des documents et des pages dans les PDF à l'aide de Ruby et Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Définir les propriétés d'affichage de la fenêtre du document et de la page



Pour définir les propriétés d'affichage de la fenêtre du document et de la page d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SetDocumentWindow**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Set different document properties

# Position of document's window - Default: false

doc.setCenterWindow(true)

# Predominant reading order; determine the position of page

# when displayed side by side - Default: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Whether window's title bar should display document title.

# If false, title bar displays PDF file name - Default: false

doc.setDisplayDocTitle(true)

# Whether to resize the document's window to fit the size of

# first displayed page - Default: false

doc.setFitWindow(true)

# Whether to hide menu bar of the viewer application - Default: false

doc.setHideMenubar(true)

# Whether to hide tool bar of the viewer application - Default: false

doc.setHideToolBar(true)

# Whether to hide UI elements like scroll bars

# and leaving only the page contents displayed - Default: false

doc.setHideWindowUI(true)

# The document's page mode. How to display document on exiting full-screen mode.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# The page layout i.e. single page, one column

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# How the document should display when opened.

doc.setPageMode()

# Save updated PDF file

doc.save(data_dir + "Set Document Window.pdf")
```

## 
Télécharger le code d'exécution



Téléchargez** Définir les propriétés d'affichage de la fenêtre du document et de la page (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
