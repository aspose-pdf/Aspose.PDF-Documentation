---
title: Diviser un fichier PDF en pages individuelles en Python
type: docs
weight: 80
url: fr/java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

Pour diviser un document PDF en pages individuelles en utilisant **Aspose.PDF Java pour PHP**, invoquez simplement la classe **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# boucle à travers toutes les pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# créer un nouvel objet Document
new_document = self.Document();

# obtenir la page à un index particulier de la collection de pages
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# enregistrer le fichier PDF nouvellement généré
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Le processus de division s'est terminé avec succès!";
```

**Télécharger le code en cours d'exécution**

Téléchargez **Diviser les pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)