---
title: Obtenez des informations sur un fichier PDF en Python
type: docs
weight: 40
url: fr/python-java/get-pdf-file-information-in-python/
---

<ins>Pour obtenir des informations sur un fichier PDF en utilisant **Aspose.PDF Java for Python**, il suffit d'invoquer la classe **GetPdfFileInfo**.

**Code Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtenir des informations sur le document
doc_info = doc.getInfo();

# Afficher les informations du document
print "Auteur:-" + str(doc_info.getAuthor())
print "Date de création:-" + str(doc_info.getCreationDate())
print "Mots-clés:-" + str(doc_info.getKeywords())
print "Date de modification:-" + str(doc_info.getModDate())
print "Sujet:-" + str(doc_info.getSubject())
print "Titre:-" + str(doc_info.getTitle())
```

**Télécharger le code d'exécution**

Téléchargez **Obtenez des informations sur un fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)