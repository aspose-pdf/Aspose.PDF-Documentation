---
title: Ajouter une chaîne HTML en utilisant DOM en Python
type: docs
weight: 10
url: /fr/java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
description: Explique comment ajouter une chaîne HTML dans le DOM en utilisant Python avec une bibliothèque de format de fichier PDF
---

## Ajouter une chaîne HTML dans le DOM PDF en utilisant Python
Pour ajouter une chaîne HTML dans un document Pdf en utilisant **Aspose.PDF Java pour Python**, invoquez simplement le module **AddHtml**.

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

**Télécharger le code en cours d'exécution**

Téléchargez **Add HTML (Aspose.PDF)** depuis n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)