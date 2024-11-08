---
title: Ajouter une chaîne HTML en utilisant DOM dans Python
type: docs
weight: 10
url: /fr/python-java/add-html-string-using-dom-in-python/
---

Pour ajouter une chaîne HTML dans un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer le module **AddHtml**.

```python

# Instancier l'objet Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Définir les informations de marge
title.setMargin(margin)

# Ajouter le fragment HTML à la collection de paragraphes de la page
page.getParagraphs().add(title)

# Enregistrer le fichier PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML ajouté avec succès"
```

**Télécharger le Code Exécutable**

Téléchargez **Add HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)