---
title: Obtenir des Informations de Fichier PDF en Python
type: docs
weight: 40
url: /fr/java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Pour obtenir les informations de fichier d'un document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetPdfFileInfo**.

```python

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Obtenir les informations du document
doc_info = doc.getInfo();

# Afficher les informations du document
print "Auteur:-" + str(doc_info.getAuthor())
print "Date de création:-" + str(doc_info.getCreationDate())
print "Mots-clés:-" + str(doc_info.getKeywords())
print "Date de modification:-" + str(doc_info.getModDate())
print "Sujet:-" + str(doc_info.getSubject())
print "Titre:-" + str(doc_info.getTitle())
```

**Télécharger le Code Exécutant**

Téléchargez **Obtenir des Informations de Fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)