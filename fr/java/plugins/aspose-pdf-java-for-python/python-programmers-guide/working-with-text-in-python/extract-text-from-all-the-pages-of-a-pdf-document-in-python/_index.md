---
title: Extraire le Texte de Toutes les Pages d'un Document PDF en Python
type: docs
weight: 30
url: /fr/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
keywords: extraire texte pdf python
description: Explique comment extraire le texte des pages PDF en Python en utilisant l'API de format de fichier PDF.
---

## Extraire le Texte d'un PDF en utilisant Python

Pour extraire le texte de toutes les pages d'un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer le module **ExtractTextFromAllPages**.

```python

# Ouvrir le document cible
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Texte extrait avec succès. Vérifiez le fichier de sortie."

```

**Télécharger le Code Exécuté**

Téléchargez **Extraire le Texte de Toutes les Pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)