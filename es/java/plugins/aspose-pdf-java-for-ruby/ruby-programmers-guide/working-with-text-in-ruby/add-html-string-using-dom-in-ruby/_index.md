---
title: Agregar cadena HTML usando DOM en Ruby
linktitle: Agregar cadena HTML usando DOM en Ruby
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: Descubra cómo agregar una cadena HTML a un documento PDF usando la API DOM en Ruby con Aspose.PDF para la generación de contenido dinámico.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Agregar HTML



Para agregar una cadena HTML en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **AddHtml**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Agregue HTML (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
