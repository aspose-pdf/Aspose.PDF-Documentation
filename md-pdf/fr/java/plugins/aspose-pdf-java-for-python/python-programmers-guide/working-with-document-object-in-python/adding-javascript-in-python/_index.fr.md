---
title: Ajouter JavaScript dans Python
type: docs
weight: 10
url: /java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

Pour ajouter JavaScript en utilisant Aspose.PDF Java dans Python, invoquez simplement la méthode AddJavascript() de la classe Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('la page 2 est ouverte')")

# Ajout de JavaScript au niveau de la page
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('la page 2 est fermée')"))

# Enregistrer le document PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript ajouté avec succès, veuillez vérifier le fichier de sortie."

```

**Télécharger le code en cours d'exécution**

Téléchargez **Ajouter JavaScript (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)