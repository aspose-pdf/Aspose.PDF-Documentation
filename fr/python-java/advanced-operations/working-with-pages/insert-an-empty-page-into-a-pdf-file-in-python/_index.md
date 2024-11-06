---
title: Insérer une Page Vide dans un Fichier PDF en Python
type: docs
weight: 70
url: fr/python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>Pour insérer une page vide dans un document PDF en utilisant **Aspose.PDF Java pour Python**, invoquez simplement la classe **InsertEmptyPage**.

**Code Python**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insérer une page vide dans un PDF
pdf_document.getPages().insert(1)

# Enregistrer le fichier de sortie concaténé (le document cible)
pdf_document.save(self.dataDir + "output.pdf")

print "Page vide ajoutée avec succès!"

```

**Télécharger le Code Exécutant**

Téléchargez **Insérer une Page Vide (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)