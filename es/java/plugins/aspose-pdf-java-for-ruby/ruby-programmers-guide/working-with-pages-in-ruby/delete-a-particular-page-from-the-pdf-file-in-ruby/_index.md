---
title: Eliminar una página particular del archivo PDF en Ruby
linktitle: Eliminar una página particular del archivo PDF en Ruby
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Elimine páginas específicas de archivos PDF mediante programación utilizando Aspose.PDF para Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Eliminar página



Para eliminar una página particular del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **DeletePage**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Eliminar página (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
