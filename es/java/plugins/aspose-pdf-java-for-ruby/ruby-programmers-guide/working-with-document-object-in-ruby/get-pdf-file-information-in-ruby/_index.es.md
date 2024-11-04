---
title: Obtener Información del Archivo PDF en Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Información del Archivo PDF

Para obtener información del archivo del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **GetPdfFileInfo**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtener información del documento

doc_info = doc.getInfo()

# Mostrar información del documento

puts "Autor:-" + doc_info.getAuthor().to_s

puts "Fecha de Creación:-" + doc_info.getCreationDate().to_string

puts "Palabras Clave:-" + doc_info.getKeywords().to_s

puts "Fecha de Modificación:-" + doc_info.getModDate().to_string

puts "Asunto:-" + doc_info.getSubject().to_s

puts "Título:-" + doc_info.getTitle().to_s
```

## Descargar Código en Ejecución

Descargar **Obtener Información del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)