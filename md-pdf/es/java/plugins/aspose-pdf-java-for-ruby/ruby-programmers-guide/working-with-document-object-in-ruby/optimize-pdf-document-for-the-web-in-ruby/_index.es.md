---
title: Optimizar Documento PDF para la Web en Ruby
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimizar PDF para la Web

Para optimizar un documento PDF para la web usando **Aspose.PDF Java para Ruby**, simplemente invoca el método **optimize_web** del módulo **Optimize**.

Código Ruby

```java

 def optimize_web()

    # La ruta al directorio de documentos.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Abrir un documento pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimizar para la web

    doc.optimize()

    # Guardar el documento de salida

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "PDF optimizado para la Web, por favor revise el archivo de salida."

end
``` 

## Descargar Código en Ejecución

Descargar **Optimizar PDF para la Web (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)