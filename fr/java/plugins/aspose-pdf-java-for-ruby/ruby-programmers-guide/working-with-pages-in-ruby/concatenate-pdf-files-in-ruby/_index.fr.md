---
title: Concaténer des fichiers PDF en Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concaténer des fichiers PDF

Pour concaténer des fichiers PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **ConcatenatePdfFiles**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Ouvrir le document source

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Ajouter les pages du document source au document cible

pdf1.getPages().add(pdf2.getPages())

# Sauvegarder le fichier de sortie concaténé (le document cible)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "Le nouveau document a été sauvegardé, veuillez vérifier le fichier de sortie"
```

## Télécharger le code en cours d'exécution

Téléchargez **Concatenate PDF Files (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)