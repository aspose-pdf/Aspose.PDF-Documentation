---
title: Insertar una página vacía en un archivo PDF en Ruby
linktitle: Insertar una página vacía en un archivo PDF en Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Aprenda a insertar una página vacía en una ubicación específica dentro de un documento PDF usando Ruby y Aspose.PDF para una gestión precisa de los documentos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Insertar una página vacía



Para insertar una página vacía en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **InsertEmptyPage**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Inserte una página vacía (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
