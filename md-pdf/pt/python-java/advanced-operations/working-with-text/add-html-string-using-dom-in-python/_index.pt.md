---
title: Adicionar String HTML usando DOM em Python
type: docs
weight: 10
url: /python-java/add-html-string-using-dom-in-python/
---

Para adicionar uma string HTML em um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar o módulo **AddHtml**.

```python

# Instanciar objeto Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Tabela</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Definir informações de margem
title.setMargin(margin)

# Adicionar Fragmento HTML à coleção de parágrafos da página
page.getParagraphs().add(title)

# Salvar arquivo PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML adicionado com sucesso"
```

**Baixar Código em Execução**

Baixe **Adicionar HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)