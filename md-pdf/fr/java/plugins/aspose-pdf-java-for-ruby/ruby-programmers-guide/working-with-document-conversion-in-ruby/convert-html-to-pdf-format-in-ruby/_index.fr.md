---
title: Convertir HTML en format PDF en Ruby
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir HTML en format PDF

Pour convertir HTML en format PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **HtmlToPdf**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Charger le fichier HTML

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Enregistrer le fichier de sortie concaténé (le document cible)

pdf.save(data_dir + "html.pdf")

puts "Le document a été converti avec succès"
```

## Télécharger le code en cours d'exécution

Téléchargez **Convertir HTML en format PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)