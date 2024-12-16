---
title: Añadiendo JavaScript en Python
type: docs
weight: 10
url: /es/java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

Para agregar JavaScript usando Aspose.PDF Java en Python, simplemente invoque el método AddJavascript() de la clase Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Añadiendo JavaScript a Nivel de Página
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Guardar Documento PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript añadido con éxito, por favor revise el archivo de salida."

```

**Descargar Código en Ejecución**

Descargue **Add Javascript (Aspose.PDF)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)