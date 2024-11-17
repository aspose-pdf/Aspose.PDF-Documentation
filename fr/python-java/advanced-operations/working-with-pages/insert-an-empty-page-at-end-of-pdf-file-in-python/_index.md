---
title: Insérer une Page Vide à la Fin d'un Fichier PDF en Python
type: docs
weight: 60
url: /fr/python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>Pour insérer une page vide à la fin d'un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **InsertEmptyPageAtEndOfFile**.

**Code Python**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insérer une page vide dans un PDF
pdf_document.getPages().add();

# Enregistrer le fichier de sortie concaténé (le document cible)
pdf_document.save(self.dataDir + "output.pdf")

print "Page vide ajoutée avec succès!"

```

**Télécharger le Code Exécutable**

Téléchargez **Insérer une Page Vide à la Fin d'un Fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)