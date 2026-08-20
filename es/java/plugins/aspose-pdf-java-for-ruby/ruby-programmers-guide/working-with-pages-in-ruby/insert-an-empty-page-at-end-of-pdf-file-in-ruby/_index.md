---
title: Insertar una página vacía al final del archivo PDF en Ruby
linktitle: Insertar una página vacía al final del archivo PDF en Ruby
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Descubra cómo insertar una página vacía al final de un documento PDF usando Ruby con Aspose.PDF, agregando flexibilidad a sus tareas de procesamiento de PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Insertar una página vacía al final del archivo PDF



Para insertar una página vacía al final de un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **InsertEmptyPageAtEndOfFile**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Inserte una página vacía al final del archivo PDF (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
