---
title: Convertir un fichier SVG au format PDF en Ruby
type: docs
weight: 60
url: /fr/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir SVG en PDF

Pour convertir un fichier SVG au format PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **SvgToPdf**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instancier l'objet LoadOption en utilisant l'option de chargement SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Créer un objet document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Enregistrer la sortie au format XLS

pdf.save(data_dir + "SVG.pdf")

puts "Le document a été converti avec succès"
```

## Télécharger le code en cours d'exécution

Téléchargez **Convertir SVG en PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)