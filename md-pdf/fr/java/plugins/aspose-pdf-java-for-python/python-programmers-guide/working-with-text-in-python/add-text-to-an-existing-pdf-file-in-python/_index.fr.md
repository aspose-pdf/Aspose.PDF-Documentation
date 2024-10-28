---
title: Ajouter du texte à un PDF existant avec Python
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: ajouter texte pdf python, écrire texte pdf python
description: Exemple de code pour ajouter ou écrire du texte dans un document Pdf en utilisant Python avec la bibliothèque PDF.
---

## Écrire ou ajouter du texte dans un PDF en utilisant Python

Pour ajouter une chaîne de texte dans un document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer le module **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("texte principal")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Enregistrer le fichier PDF
doc.save(self.dataDir + "Text_Added.pdf")
print "Texte ajouté avec succès"
```


**Télécharger le Code Exécutable**

Téléchargez **Ajouter du Texte (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)