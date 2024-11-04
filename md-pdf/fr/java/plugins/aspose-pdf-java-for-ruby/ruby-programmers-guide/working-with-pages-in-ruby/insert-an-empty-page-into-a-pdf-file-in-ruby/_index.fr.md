---
title: Insérer une Page Vide dans un Fichier PDF en Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insérer une Page Vide

Pour insérer une page vide dans un document PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **InsertEmptyPage**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insérer une page vide dans un PDF

pdf.getPages().insert(1)

# Sauvegarder le fichier de sortie concaténé (le document cible)

pdf.save(data_dir+ "output.pdf")

puts "Page vide ajoutée avec succès!"
```

## Télécharger le Code en Exécution

Téléchargez **Insert an Empty Page (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)