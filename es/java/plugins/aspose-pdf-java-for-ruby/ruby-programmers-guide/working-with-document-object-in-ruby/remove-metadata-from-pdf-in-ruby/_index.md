---
title: Eliminar metadatos de PDF en Ruby
linktitle: Eliminar metadatos de PDF en Ruby
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: Borre metadatos confidenciales o no deseados de archivos PDF mediante programación con Aspose.PDF para Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Eliminar metadatos



Para eliminar metadatos de un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **RemoveMetadata**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## 
Descargar código de ejecución



DescargarВ **Eliminar metadatos (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
