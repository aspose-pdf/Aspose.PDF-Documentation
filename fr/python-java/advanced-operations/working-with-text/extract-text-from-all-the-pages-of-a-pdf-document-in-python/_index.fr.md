---
title: Extraire le texte de toutes les pages d'un document PDF en Python
type: docs
weight: 30
url: /python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

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

**Télécharger le code en cours d'exécution**

Téléchargez **Extract Text From All the Pages (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)