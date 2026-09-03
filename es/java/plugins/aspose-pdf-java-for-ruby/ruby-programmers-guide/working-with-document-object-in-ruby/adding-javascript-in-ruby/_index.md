---
title: Agregar JavaScript en Ruby
linktitle: Agregar JavaScript en Ruby
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
description: Habilite la funcionalidad JavaScript en archivos PDF usando Aspose.PDF en Ruby para interactividad y automatización.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Agregar JavaScript



Para agregar JavaScript en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **AddJavaScript**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## 
Descargar código de ejecución



Descargue **Agregar JavaScript (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
