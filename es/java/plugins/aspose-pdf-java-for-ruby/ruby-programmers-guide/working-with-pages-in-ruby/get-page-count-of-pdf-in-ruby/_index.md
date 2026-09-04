---
title: Obtener el Recuento de Páginas del PDF en Ruby
type: docs
weight: 40
url: /es/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener el Recuento de Páginas

Para obtener el recuento de páginas de un documento Pdf usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **GetNumberOfPages**.

Código en Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Crear documento PDF

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Recuento de Páginas:" + page_count.to_s
```

## Descargar Código en Ejecución

Descargar **Obtener el Recuento de Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)