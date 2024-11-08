---
title: Définir les informations du fichier PDF en Python
type: docs
weight: 90
url: /fr/python-java/set-pdf-file-information-in-python/
---

<ins>Pour mettre à jour les informations du document Pdf en utilisant **Aspose.PDF Java for Python**, il suffit d'invoquer la classe **SetPdfFileInfo**.

**Code Python**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtenir les informations du document
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF pour java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Informations PDF");
doc_info.setTitle("Définir les informations du document PDF");

# enregistrer le document mis à jour avec de nouvelles informations

doc.save(self.dataDir + "Updated_Information.pdf")
print "Mettre à jour les informations du document, veuillez vérifier le fichier de sortie."
```

**Télécharger le code en cours d'exécution**

Téléchargez **Définir les informations du fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)