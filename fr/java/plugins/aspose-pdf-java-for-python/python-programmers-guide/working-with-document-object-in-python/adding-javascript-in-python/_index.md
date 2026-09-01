---
title: Ajout de JavaScript en Python
linktitle: Ajout de JavaScript en Python
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: Découvrez comment intégrer du code JavaScript dans un document PDF à l'aide de Python et Aspose.PDF pour améliorer l'interactivité.
lastmod: "2026-06-09"
---

Pour ajouter Add Javascript à l'aide d'Aspose.PDF Java en Python, invoquez simplement la méthode AddJavascript() de la classe Document.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```


**Télécharger le code d'exécution**

Téléchargez **Ajouter Javascript (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
