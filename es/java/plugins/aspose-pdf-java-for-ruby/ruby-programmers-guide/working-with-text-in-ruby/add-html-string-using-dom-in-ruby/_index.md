---
title: Agregar cadena HTML usando DOM en Ruby
linktitle: Agregar cadena HTML usando DOM en Ruby
type: docs
weight: 10
url: /es/java/add-html-string-using-dom-in-ruby/
description: Descubra cómo agregar una cadena HTML a un documento PDF usando la API DOM en Ruby con Aspose.PDF para la generación dinámica de contenido.
lastmod: "2026-09-03"
---
## Aspose.PDF - Agregar HTML

Para agregar una cadena HTML en un documento Pdf usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **AddHtml**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## Descargar código en ejecución

Descargar **Agregar HTML (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
