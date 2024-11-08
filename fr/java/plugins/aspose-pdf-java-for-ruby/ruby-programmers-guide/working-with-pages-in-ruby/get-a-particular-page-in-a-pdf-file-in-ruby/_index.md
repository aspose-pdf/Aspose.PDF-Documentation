---
title: Obtenir une Page Particulière dans un Fichier PDF en Ruby
type: docs
weight: 30
url: /fr/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir une Page

Pour obtenir une Page Particulière dans un document PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **GetPage**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtenir la page à un index particulier de la collection de pages

pdf_page = pdf.getPages().get_Item(1)

# créer un nouvel objet Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# ajouter une page à la collection de pages du nouvel objet document

new_document.getPages().add(pdf_page)

# enregistrer le fichier PDF nouvellement généré

new_document.save(data_dir + "output.pdf")

puts "Processus terminé avec succès!"
```

## Télécharger le Code Exécutant

Téléchargez **Get Page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)