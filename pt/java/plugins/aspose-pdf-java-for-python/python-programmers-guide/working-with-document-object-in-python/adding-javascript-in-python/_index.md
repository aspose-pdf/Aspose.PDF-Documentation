---
title: Adicionar JavaScript em Python
linktitle: Adicionar JavaScript em Python
type: docs
weight: 10
url: /pt/java/adding-javascript-in-python/
description: Descubra como incorporar código JavaScript dentro de um documento PDF usando Python e Aspose.PDF para melhorar a interatividade.
lastmod: "2026-10-06"
---
Para anexar Add Javascript usando Aspose.PDF Java em Python, basta chamar o método AddJavascript() da classe Document.

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

**Download do Código em Execução**

Baixe **Add Javascript (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
