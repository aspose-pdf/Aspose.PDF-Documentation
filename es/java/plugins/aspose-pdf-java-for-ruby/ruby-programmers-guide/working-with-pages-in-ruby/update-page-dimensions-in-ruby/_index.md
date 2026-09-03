---
title: Actualizar dimensiones de página en Ruby
linktitle: Actualizar dimensiones de página en Ruby
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
description: Descubra cómo actualizar las dimensiones de la página de un documento PDF usando Ruby con Aspose.PDF para obtener un formato de página preciso.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Actualizar dimensiones de página



Para actualizar las dimensiones de la página usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **UpdatePageDimensions**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## 
Descargar código de ejecución



Descargue ** Actualizar dimensiones de la página (Aspose.PDF) ** desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
