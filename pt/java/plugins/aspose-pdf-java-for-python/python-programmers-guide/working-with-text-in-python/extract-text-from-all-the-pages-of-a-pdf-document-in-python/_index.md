---
title: Extraia texto de todas as páginas de um documento PDF em Python
linktitle: Extraia texto de todas as páginas de um documento PDF em Python
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: Explica como extrair texto de páginas PDF em Python usando API de formato de arquivo PDF.
---
## Extraia texto de PDF usando Python

Para extrair o documento PDF TextrFrom All the Pages usando **Aspose.PDF Java para Python**, basta invocar o módulo **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Baixar código em execução**

Baixe ** Extrair texto de todas as páginas (Aspose.PDF) ** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
