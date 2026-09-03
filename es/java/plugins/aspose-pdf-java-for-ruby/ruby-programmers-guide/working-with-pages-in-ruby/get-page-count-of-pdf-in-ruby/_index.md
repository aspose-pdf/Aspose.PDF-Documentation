---
title: Obtener recuento de páginas de PDF en Ruby
linktitle: Obtener recuento de páginas de PDF en Ruby
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: Recupere el número total de páginas de un documento PDF mediante programación utilizando Ruby con Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener recuento de páginas



Para obtener el recuento de páginas de un documento PDF utilizando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **GetNumberOfPages**.

Código Rubí


```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 
Descargar código de ejecución



Descargue **Obtenga recuento de páginas (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
