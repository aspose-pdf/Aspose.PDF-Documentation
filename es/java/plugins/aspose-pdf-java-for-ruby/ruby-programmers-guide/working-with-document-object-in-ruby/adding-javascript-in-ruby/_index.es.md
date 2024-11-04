---
title: Adding JavaScript in Ruby
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Añadiendo JavaScript

Para agregar JavaScript en un documento Pdf usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **AddJavaScript**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Añadiendo JavaScript a nivel de documento

# Instanciar JavascriptAction con la declaración de JavaScript deseada

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Asignar objeto JavascriptAction a la acción deseada del documento

doc.setOpenAction(javaScript)

# Añadiendo JavaScript a nivel de página

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Guardar documento PDF

doc.save(data_dir + "JavaScript-Added.pdf")

puts "JavaScript añadido exitosamente, por favor revisa el archivo de salida."
```


## Descargar Código en Ejecución

Descargue **Adding JavaScript (Aspose.PDF)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)