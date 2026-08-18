---
title: Insira uma página vazia no final do arquivo PDF em Python
linktitle: Insira uma página vazia no final do arquivo PDF em Python
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Descubra como inserir uma página vazia no final de um documento PDF em Python com Aspose.PDF para facilitar a expansão do documento.
lastmod: "2026-06-09"
---
Para inserir uma página vazia no final do documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Baixar código em execução**

Baixe **Inserir uma página vazia no final do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
