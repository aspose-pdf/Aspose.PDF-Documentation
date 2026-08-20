---
title: Agregar JavaScript en Python
linktitle: Agregar JavaScript en Python
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: Descubra cómo incrustar código JavaScript en un documento PDF utilizando Python y Aspose.PDF para mejorar la interactividad.
lastmod: "2026-06-09"
---

Para agregar Agregar Javascript usando Aspose.PDF Java en Python, simplemente invoque el método AddJavascript() de la clase Documento.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```


**Descargar código de ejecución**

Descargue **Agregar Javascript (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
