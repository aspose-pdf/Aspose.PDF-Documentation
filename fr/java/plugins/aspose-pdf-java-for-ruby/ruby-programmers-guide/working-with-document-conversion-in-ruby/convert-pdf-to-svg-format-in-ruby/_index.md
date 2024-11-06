---
title: Convertir un PDF en format SVG en Ruby
type: docs
weight: 50
url: fr/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir un PDF en SVG

Pour convertir un PDF au format SVG en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **PdfToSvg**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instancier un objet de SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# ne pas compresser l'image SVG dans une archive Zip

save_options.CompressOutputToZipArchive = false

# Enregistrer le résultat au format XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "Le document a été converti avec succès"
```

## Télécharger le Code Exécuté

Téléchargez **Convertir un PDF en format SVG (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)