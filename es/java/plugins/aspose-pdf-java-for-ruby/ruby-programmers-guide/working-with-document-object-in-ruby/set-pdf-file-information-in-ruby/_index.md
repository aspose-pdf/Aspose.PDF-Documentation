---
title: Establecer Información del Archivo PDF en Ruby
type: docs
weight: 120
url: /es/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Establecer Información del Archivo PDF

Para actualizar la información del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SetPdfFileInfo**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtener la información del documento

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF para java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("Información del PDF")

doc_info.setTitle("Estableciendo Información del Documento PDF")

# guardar el documento actualizado con la nueva información

doc.save(data_dir + "Updated_Information.pdf")

puts "Actualizar la información del documento, por favor verifique el archivo de salida."
```


## Descargar Código en Ejecución

Descargar **Establecer Información de Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)