---
title: Ajouter une table des matières à un PDF existant en Python
type: docs
weight: 20
url: /fr/java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

Pour ajouter une table des matières dans un document Pdf à l'aide de **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **AddToc**.

```python

# Ouvrir un document pdf.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Accéder à la première page du fichier PDF
toc_page = doc.getPages().insert(1)

# Créer un objet pour représenter les informations de la table des matières
toc_info = self.TocInfo()
title = self.TextFragment("Table des matières")
title.getTextState().setFontSize(20)

# Définir le titre pour la table des matières
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Créer des objets de chaîne qui seront utilisés comme éléments de la table des matières
titles = ["Première page", "Deuxième page"]

i = 0;
while (i < 2):

# Créer un objet Heading
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Spécifier la page de destination pour l'objet heading
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Page de destination
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Coordonnée de destination
segment2.setText(titles[i])

# Ajouter l'en-tête à la page contenant la table des matières
toc_page.getParagraphs().add(heading2)

i +=1;

# Enregistrer le document PDF
doc.save(self.dataDir + "TOC.pdf")

print "Table des matières ajoutée avec succès, veuillez vérifier le fichier de sortie."
```


**Télécharger le Code Exécutif**

Téléchargez **Ajouter TOC (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)