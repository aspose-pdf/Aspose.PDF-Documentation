---
title: Obtenez les Propriétés de la Fenêtre du Document et de l'Affichage de la Page en Python
type: docs
weight: 30
url: /python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>Pour obtenir les propriétés de la fenêtre du document et de l'affichage de la page d'un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetDocumentWindow**.

**Code Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtenez différentes propriétés du document
# Position de la fenêtre du document - Par défaut: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Ordre de lecture prédominant; déterminer la position de la page
# lorsqu'elle est affichée côte à côte - Par défaut: L2R
print "Direction :- " + str(doc.getDirection())

# Si la barre de titre de la fenêtre doit afficher le titre du document.
# Si false, la barre de titre affiche le nom du fichier PDF - Par défaut: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
# la première page affichée - Par défaut: false

print "FitWindow :- " + str(doc.getFitWindow())

# Si la barre de menu de l'application de visualisation doit être masquée - Par défaut : false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Si la barre d'outils de l'application de visualisation doit être masquée - Par défaut : false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Si les éléments de l'interface utilisateur comme les barres de défilement doivent être masqués
# et ne laisser que le contenu de la page affiché - Par défaut : false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# Le mode de page du document. Comment afficher le document en quittant le mode plein écran.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# La mise en page, c'est-à-dire une seule page, une colonne
print "PageLayout :-" + str(doc.getPageLayout())

# Comment le document doit s'afficher lorsqu'il est ouvert.
print "pageMode :-" + str(doc.getPageMode())


**Télécharger le Code en Exécution**

Télécharger **Obtenir les Propriétés de Fenêtre et d'Affichage de Page du Document (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)