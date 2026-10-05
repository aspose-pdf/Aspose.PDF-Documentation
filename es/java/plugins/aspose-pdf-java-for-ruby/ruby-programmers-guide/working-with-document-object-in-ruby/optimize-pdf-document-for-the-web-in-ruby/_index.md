---
title: Optimizar documento PDF para la web en Ruby
linktitle: Optimizar documento PDF para la web en Ruby
type: docs
weight: 70
url: /es/java/optimize-pdf-document-for-the-web-in-ruby/
description: Optimice PDFs para una entrega web más rápida y reduzca el tamaño del archivo usando Aspose.PDF en Ruby.
lastmod: "2026-09-29"
---
## Aspose.PDF - optimizar PDF para la web

Para optimizar un documento PDF para la web usando **Aspose.PDF Java for Ruby**, simplemente invoque el método **optimize_web** del módulo **Optimize**.

Código Ruby

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## Descargar código en ejecución

Descargar **Optimize PDF for Web (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
