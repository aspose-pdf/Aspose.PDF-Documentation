---
title: Adicionar string HTML usando DOM em Python
linktitle: Adicionar string HTML usando DOM em Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: Explica como adicionar string HTML no DOM usando Python com biblioteca de formato de arquivo PDF
---
## Adicionar string HTML em PDF DOM usando Python

Para adicionar uma string HTML em um documento PDF usando **Aspose.PDF Java para Python**, basta invocar o módulo **AddHtml**.

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

**Baixar código em execução**

Baixe **Adicione HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
