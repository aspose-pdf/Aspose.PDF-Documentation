---
title: Obtenir des métadonnées XMP à partir d'un fichier PDF en Ruby
linktitle: Obtenir des métadonnées XMP à partir d'un fichier PDF en Ruby
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Accédez et manipulez les métadonnées XMP dans les documents PDF à l'aide de Ruby avec Aspose.PDF.
lastmod: "2026-09-21"
---
## Aspose.PDF - Obtenir les métadonnées XMP

Pour obtenir les métadonnées XMP d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, utilisez le module **GetXMPMetadata**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Télécharger l’exemple de code

Téléchargez **Obtenez des métadonnées XMP (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
