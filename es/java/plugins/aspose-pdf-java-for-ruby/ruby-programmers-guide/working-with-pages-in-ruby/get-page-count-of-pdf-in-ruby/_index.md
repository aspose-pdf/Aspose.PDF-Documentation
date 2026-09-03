---
title: Obtener recuento de páginas de PDF en Ruby
linktitle: Obtener recuento de páginas de PDF en Ruby
type: docs
weight: 40
url: /es/java/get-page-count-of-pdf-in-ruby/
description: Recupera el número total de páginas de un documento PDF programáticamente usando Ruby con Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Obtener recuento de páginas

Para obtener el recuento de páginas de un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoca el módulo **GetNumberOfPages**.

Código Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Descargar código en ejecución

DownloadВ **Obtener recuento de páginas (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
