---
title: Adicionar Texto a um PDF Existente usando Python
type: docs
weight: 20
url: /pt/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
description: Exemplo de código de como adicionar ou escrever texto em um documento Pdf usando Python com a biblioteca PDF.
---

## Escrever ou Adicionar Texto em PDF usando Python

Para adicionar uma string de texto em um documento Pdf usando **Aspose.PDF Java for Python**, simplesmente invoque o módulo **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("texto principal")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Salvar arquivo PDF
doc.save(self.dataDir + "Text_Added.pdf")
print "Texto adicionado com sucesso"
```


**Baixar Código em Execução**

Baixar **Adicionar Texto (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)