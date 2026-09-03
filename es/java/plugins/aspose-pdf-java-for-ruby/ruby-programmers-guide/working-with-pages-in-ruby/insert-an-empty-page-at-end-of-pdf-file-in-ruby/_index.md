---
title: Insertar una página en blanco al final del archivo PDF en Ruby
linktitle: Insertar una página en blanco al final del archivo PDF en Ruby
type: docs
weight: 60
url: /es/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Descubra cómo insertar una página en blanco al final de un documento PDF usando Ruby con Aspose.PDF, añadiendo flexibilidad a sus tareas de procesamiento de PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Insertar una página en blanco al final del archivo PDF

Para insertar una página en blanco al final del documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **InsertEmptyPageAtEndOfFile**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Descargar código en ejecución

Descargar **Insert an Empty Page at End of PDF File (Aspose.PDF)**В fromВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
