---
title: Insira uma página vazia em um arquivo PDF em Python
linktitle: Insira uma página vazia em um arquivo PDF em Python
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Aprenda como inserir uma página vazia em qualquer posição em um arquivo PDF usando Python e Aspose.PDF para estruturação flexível de documentos.
lastmod: "2026-06-09"
---
Para inserir uma página vazia em um documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Baixar código em execução**

Baixe **Insira uma página vazia (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
