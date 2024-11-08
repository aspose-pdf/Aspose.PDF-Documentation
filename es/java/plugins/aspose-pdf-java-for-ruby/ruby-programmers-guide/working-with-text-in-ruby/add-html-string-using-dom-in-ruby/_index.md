---
title: Añadir Cadena HTML usando DOM en Ruby
type: docs
weight: 10
url: /es/java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Añadir HTML

Para añadir una cadena HTML en un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **AddHtml**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto Document

doc = Rjb::import('com.aspose.pdf.Document').new

# Añadir una página a la colección de páginas del archivo PDF

page = doc.getPages().add()

# Instanciar HtmlFragment con contenidos HTML

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# establecer MarginInfo para detalles de margen

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Establecer información de margen

title.setMargin(margin)

# Añadir Fragmento HTML a la colección de párrafos de la página

page.getParagraphs().add(title)

# Guardar el archivo PDF

doc.save(data_dir + "html.output.pdf")

puts "HTML añadido con éxito"
```


## Descargar Código en Ejecución

Descargar **Agregar HTML (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)