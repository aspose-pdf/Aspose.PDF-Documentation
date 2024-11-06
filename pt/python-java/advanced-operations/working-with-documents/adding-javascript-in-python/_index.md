---
title: Adicionando JavaScript em Python
type: docs
weight: 10
url: pt/python-java/adding-javascript-in-python/
---

Para adicionar JavaScript usando Aspose.PDF Java em Python, basta invocar o método AddJavascript() da classe Document.

**Código Python**

```python

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js = self.JavascriptAction("app.alert('página 2 foi aberta')")

# Adicionando JavaScript no Nível da Página
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('página 2 foi fechada')"))

# Salvar Documento PDF
doc.save(self.dataDir + "JavaScript-Adicionado.pdf")

print "JavaScript adicionado com sucesso, por favor, verifique o arquivo de saída."

```

**Baixar Código em Execução**

Baixe **Adicionar Javascript (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)