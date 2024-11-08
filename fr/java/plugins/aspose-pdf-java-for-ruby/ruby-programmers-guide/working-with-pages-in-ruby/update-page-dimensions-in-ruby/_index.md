---
title: Mettre à jour les dimensions de la page en Ruby
type: docs
weight: 90
url: /fr/java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mettre à jour les dimensions de la page

Pour mettre à jour les dimensions de la page en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **UpdatePageDimensions**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtenir la collection de pages

page_collection = pdf.getPages()

# obtenir une page particulière

pdf_page = page_collection.get_Item(1)

# définir la taille de la page comme A4 (11.7 x 8.3 in) et dans Aspose.PDF, 1 pouce = 72 points

# donc les dimensions A4 en points seront (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# enregistrer le fichier PDF nouvellement généré

pdf.save(data_dir + "output.pdf")

puts "Dimensions mises à jour avec succès !"
```

## Télécharger le code en cours d'exécution

Téléchargez **Update Page Dimensions (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)