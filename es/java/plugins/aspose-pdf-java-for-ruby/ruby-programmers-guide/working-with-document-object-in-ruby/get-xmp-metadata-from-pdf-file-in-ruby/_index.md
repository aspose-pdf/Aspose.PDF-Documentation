---
title: Obtenga metadatos XMP de un archivo PDF en Ruby
linktitle: Obtenga metadatos XMP de un archivo PDF en Ruby
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Acceda y manipule metadatos XMP en documentos PDF usando Ruby con Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener metadatos XMP



Para obtener metadatos XMP de un documento PDF utilizando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **GetXMPMetadata**.

Código Rubí


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

## 
Descargar código de ejecución



DescargarВ **Obtener metadatos XMP (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
