---
title: Eliminar una página concreta del archivo PDF en Ruby
linktitle: Eliminar una página concreta del archivo PDF en Ruby
type: docs
weight: 20
url: /es/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Eliminar páginas específicas de archivos PDF de forma programática usando Aspose.PDF for Ruby.
lastmod: "2026-09-03"
---
## Aspose.PDF - Eliminar página

Para eliminar una página concreta del documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **DeletePage**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## Descargar código en ejecución

Descargar **Delete Page (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
