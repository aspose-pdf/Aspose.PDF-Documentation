---
title: Supprimer une Page Particulière du Fichier PDF en Ruby
type: docs
weight: 20
url: /fr/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Supprimer une Page

Pour supprimer une Page Particulière du document PDF en utilisant **Aspose.PDF Java pour Ruby**, invoquez simplement le module **DeletePage**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# supprimer une page particulière

pdf.getPages().delete(2)

# enregistrer le fichier PDF nouvellement généré

pdf.save(data_dir + "output.pdf")

puts "Page supprimée avec succès!"
```

## Télécharger le Code Exécutant

Téléchargez **Supprimer la Page (Aspose.PDF)** depuis n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)