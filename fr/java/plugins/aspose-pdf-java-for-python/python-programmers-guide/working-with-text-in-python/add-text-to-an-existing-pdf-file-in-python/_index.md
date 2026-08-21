---
title: Ajouter du texte au PDF existant à l'aide de Python
linktitle: Ajouter du texte au PDF existant à l'aide de Python
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-06-09"
description: Exemple de code comment ajouter ou écrire du texte dans un document PDF en utilisant Python avec la bibliothèque PDF.
---
## 
Écrire ou ajouter du texte au format PDF à l'aide de Python



Pour ajouter une chaîne de texte dans un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement le module **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**Télécharger le code d'exécution**



Téléchargez** Ajouter du texte (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
