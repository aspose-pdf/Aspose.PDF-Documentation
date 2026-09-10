---
title: Extraire le texte de toutes les pages d'un document PDF en Python
linktitle: Extraire le texte de toutes les pages d'un document PDF en Python
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: Explique comment extraire le texte des pages PDF en Python à l'aide de l'API du format de fichier PDF.
---
## 
Extraire le texte d'un PDF à l'aide de Python



Pour extraire TextrFrom All the Pages Pdf à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement le module **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Télécharger le code d'exécution**



Téléchargez** Extraire le texte de toutes les pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
