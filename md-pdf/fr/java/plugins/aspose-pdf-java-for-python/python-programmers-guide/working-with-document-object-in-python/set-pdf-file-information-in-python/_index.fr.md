---
title: Définir les Informations du Fichier PDF en Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Pour mettre à jour les informations du document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **SetPdfFileInfo**.

```python
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Obtenir des informations sur le document
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF pour java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Informations PDF");
doc_info.setTitle("Définir les Informations du Document PDF");

# enregistrer le document mis à jour avec les nouvelles informations

doc.save(self.dataDir + "Updated_Information.pdf")
print "Mettre à jour les informations du document, veuillez vérifier le fichier de sortie."
```

**Télécharger le Code Exécuté**

Téléchargez **Définir les Informations du Fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)