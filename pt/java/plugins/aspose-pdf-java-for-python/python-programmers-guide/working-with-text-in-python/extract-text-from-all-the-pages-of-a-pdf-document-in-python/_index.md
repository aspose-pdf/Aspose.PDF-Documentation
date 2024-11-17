---
title: Extrair Texto de Todas as Páginas de um Documento PDF em Python
type: docs
weight: 30
url: /pt/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
description: Explica como extrair texto das páginas de PDF em Python usando a API de formato de arquivo PDF.
---

## Extrair Texto de PDF usando Python

Para extrair texto de todas as páginas de um documento PDF usando **Aspose.PDF Java para Python**, simplesmente invoque o módulo **ExtractTextFromAllPages**.

```python

# Abra o documento alvo
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Texto extraído com sucesso. Verifique o arquivo de saída."

```

**Baixar Código em Execução**

Baixe **Extrair Texto de Todas as Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)