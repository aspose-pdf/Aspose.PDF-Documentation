---
title: Eliminar Metadatos de PDF en Ruby
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Eliminar Metadatos

Para eliminar metadatos de un documento Pdf usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **RemoveMetadata**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abre un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# guarda el documento actualizado con nueva información

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Metadatos eliminados con éxito, por favor verifica el archivo de salida."
```

## Descargar Código en Ejecución

Descargar **Eliminar Metadatos (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)