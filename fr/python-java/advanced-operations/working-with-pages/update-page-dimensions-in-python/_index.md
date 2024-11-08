---
title: Mettre à jour les dimensions de la page en Python
type: docs
weight: 90
url: /fr/python-java/update-page-dimensions-in-python/
---

<ins>Pour mettre à jour les dimensions de la page en utilisant **Aspose.PDF Java pour Python**, invoquez simplement la classe **UpdatePageDimensions**.

**Code Python**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obtenir la collection de pages
page_collection = pdf.getPages()

# obtenir une page particulière
pdf_page = page_collection.get_Item(1)

# définir la taille de la page comme A4 (11.7 x 8.3 in) et dans Aspose.PDF, 1 pouce = 72 points
# donc les dimensions A4 en points seront (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# enregistrer le fichier PDF nouvellement généré
pdf.save(self.dataDir + "output.pdf")

print "Dimensions mises à jour avec succès!"

```

**Télécharger le code en cours d'exécution**

Téléchargez **Mettre à jour les dimensions de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)