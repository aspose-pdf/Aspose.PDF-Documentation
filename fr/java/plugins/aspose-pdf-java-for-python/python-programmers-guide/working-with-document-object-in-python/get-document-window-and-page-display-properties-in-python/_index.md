---
title: Obtenir les propriétés d'affichage de la fenêtre du document et de la page en Python
linktitle: Obtenir les propriétés d'affichage de la fenêtre du document et de la page en Python
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-python/
description: Comprenez comment récupérer les propriétés d'affichage de la fenêtre et de la page d'un document à partir d'un PDF en Python avec Aspose.PDF pour une présentation précise.
lastmod: "2026-06-09"
---

Pour obtenir les propriétés d'affichage de la fenêtre et de la page du document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **GetDocumentWindow**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get different document properties
# Position of document's window - Default: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Predominant reading order; determine the position of page
# when displayed side by side - Default: L2R
print "Direction :- " + str(doc.getDirection())

# Whether window's title bar should display document title.
# If false, title bar displays PDF file name - Default: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

#Whether to resize the document's window to fit the size of
#first displayed page - Default: false
print "FitWindow :- " + str(doc.getFitWindow())

# Whether to hide menu bar of the viewer application - Default: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Whether to hide tool bar of the viewer application - Default: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Whether to hide UI elements like scroll bars
# and leaving only the page contents displayed - Default: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# The document's page mode. How to display document on exiting full-screen mode.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# The page layout i.e. single page, one column
print "PageLayout :-" + str(doc.getPageLayout())

#How the document should display when opened.
print "pageMode :-" + str(doc.getPageMode())
```


**Télécharger le code d'exécution**

Téléchargez** Obtenez les propriétés d'affichage de la fenêtre et de la page du document (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)
