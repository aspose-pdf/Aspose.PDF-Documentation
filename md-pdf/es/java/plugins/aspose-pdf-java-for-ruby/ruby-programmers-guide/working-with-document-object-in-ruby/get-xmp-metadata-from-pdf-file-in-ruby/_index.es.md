---
title: Obtener Metadatos XMP de un Archivo PDF en Ruby
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Metadatos XMP

Para obtener Metadatos XMP de un documento Pdf usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **GetXMPMetadata**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtener propiedades

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Descargar Código en Ejecución

Descargar **Obtener Metadatos XMP (Aspose.PDF)** de cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)