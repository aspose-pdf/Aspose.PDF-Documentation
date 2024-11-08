---
title: Ajouter du texte à un fichier PDF existant en Python
type: docs
weight: 20
url: /fr/python-java/add-text-to-an-existing-pdf-file-in-python/
---

Pour ajouter une chaîne de texte dans un document Pdf en utilisant **Aspose.PDF Java for Python**, invoquez simplement le module **AddText**.

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

doc.save(self.dataDir + "Texte_Ajouté.pdf")

print "Texte ajouté avec succès"

```

**Télécharger le code en cours d'exécution**

Téléchargez **Ajouter du texte (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)