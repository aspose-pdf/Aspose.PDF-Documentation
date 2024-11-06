---
title: Añadiendo JavaScript en Python
type: docs
weight: 10
url: es/python-java/adding-javascript-in-python/
---

Para añadir JavaScript usando Aspose.PDF Java en Python, simplemente invoca el método AddJavascript() de la clase Document.

**Código Python**

```python

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js = self.JavascriptAction("app.alert('se abrió la página 2')")

# Añadiendo JavaScript a nivel de página
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('se cerró la página 2')"))

# Guardar documento PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript añadido con éxito, por favor verifica el archivo de salida."

```

**Descargar Código en Ejecución**

Descargar **Añadir Javascript (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)