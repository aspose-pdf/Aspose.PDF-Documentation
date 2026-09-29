---
title: Insertar una página vacía en un archivo PDF en Ruby
linktitle: Insertar una página vacía en un archivo PDF en Ruby
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Aprenda cómo insertar una página vacía en una ubicación específica dentro de un documento PDF utilizando Ruby y Aspose.PDF para una gestión precisa del documento.
lastmod: "2026-09-29"
---
## Aspose.PDF - insertar una página vacía

Para insertar una página vacía en un documento Pdf utilizando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **InsertEmptyPage**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Descargar código en ejecución

Descargar **Insert an Empty Page (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
