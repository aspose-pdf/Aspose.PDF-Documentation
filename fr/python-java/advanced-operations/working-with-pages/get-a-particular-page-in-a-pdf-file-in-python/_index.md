---
title: Obtenir une Page Particulière dans un Fichier PDF en Python
type: docs
weight: 30
url: /fr/python-java/get-a-particular-page-in-a-pdf-file-in-python/
---

Pour obtenir une Page Particulière dans un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obtenir la page à l'index particulier de la Collection de Pages
pdf_page = pdf.getPages().get_Item(1)

# créer un nouvel objet Document
new_document = self.Document()

# ajouter la page à la collection de pages du nouvel objet document
new_document.getPages().add(pdf_page)

# enregistrer le fichier PDF nouvellement généré
new_document.save(self.dataDir + "output.pdf")

print "Processus terminé avec succès!

```

**Télécharger le Code Exécutant**

Télécharger **Get Page (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)