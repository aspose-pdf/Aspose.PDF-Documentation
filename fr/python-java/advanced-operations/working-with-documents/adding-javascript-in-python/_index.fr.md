---
title: Ajouter JavaScript en Python
type: docs
weight: 10
url: /python-java/adding-javascript-in-python/
---

Pour ajouter JavaScript en utilisant Aspose.PDF Java en Python, il suffit d'appeler la méthode AddJavascript() de la classe Document.

**Code Python**

```python

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js = self.JavascriptAction("app.alert('page 2 is opened')")

# Ajout de JavaScript au niveau de la page
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Enregistrer le document PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript ajouté avec succès, veuillez vérifier le fichier de sortie."

```

**Télécharger le code en cours d'exécution**

Téléchargez **Ajouter Javascript (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)