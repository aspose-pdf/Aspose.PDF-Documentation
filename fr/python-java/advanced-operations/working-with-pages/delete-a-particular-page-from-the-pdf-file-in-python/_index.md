---
title: Supprimer une Page Particulière du Fichier PDF en Python
type: docs
weight: 20
url: /fr/python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

Pour supprimer une page particulière du document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **DeletePage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# supprimer une page particulière
pdf.getPages().delete(2)

# enregistrer le fichier PDF nouvellement généré
doc.save(self.dataDir + "output.pdf")

print "Page supprimée avec succès!"

```

**Télécharger le Code Exécutable**

Téléchargez **Supprimer la Page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)