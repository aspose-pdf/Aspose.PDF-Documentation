---
title: Obtenir les métadonnées XMP à partir d'un fichier PDF en Ruby
type: docs
weight: 60
url: fr/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir les métadonnées XMP

Pour obtenir les métadonnées XMP d'un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **GetXMPMetadata**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtenir les propriétés

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Télécharger le code en cours d'exécution

Téléchargez **Get XMP Metadata (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)