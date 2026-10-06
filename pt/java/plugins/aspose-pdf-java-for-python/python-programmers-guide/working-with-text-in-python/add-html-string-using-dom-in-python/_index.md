---
title: Adicionar string HTML usando DOM em Python
linktitle: Adicionar string HTML usando DOM em Python
type: docs
weight: 10
url: /pt/java/add-html-string-using-dom-in-python/
lastmod: "2026-10-06"
description: Explica como adicionar uma string HTML no DOM usando Python com a biblioteca de formato de arquivo PDF
---
## Adicionar string HTML no DOM PDF usando Python

Para adicionar uma string HTML em um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar o módulo **AddHtml**.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**Baixar Código em Execução**

Baixar **Adicionar HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
