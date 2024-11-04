---
title: Convertir PDF en format DOC ou DOCX en Ruby
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF en DOC ou DOCX

Pour convertir un document PDF en format DOC ou DOCX en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **PdfToDoc**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Enregistrer le fichier de sortie concaténé (le document cible)

pdf.save(data_dir + "output.doc")

puts "Le document a été converti avec succès"
```

## Télécharger le Code en Exécution

Téléchargez **Convertir PDF en DOC ou DOCX (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)