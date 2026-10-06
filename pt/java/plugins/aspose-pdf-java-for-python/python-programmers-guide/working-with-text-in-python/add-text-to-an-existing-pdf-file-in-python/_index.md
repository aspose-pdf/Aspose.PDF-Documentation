---
title: Adicionar texto a um PDF existente usando Python
linktitle: Adicionar texto a um PDF existente usando Python
type: docs
weight: 20
url: /pt/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-10-06"
description: Exemplo de código sobre como adicionar ou escrever texto em um documento PDF usando Python com biblioteca PDF.
---
## Escrever ou adicionar texto em PDF usando Python

Para adicionar uma string de Texto em um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar o módulo **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**Baixar Código em Execução**

BaixarВ **Add Text (Aspose.PDF)**В deВ qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
