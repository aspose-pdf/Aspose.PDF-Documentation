---
title: Exclua uma página específica do arquivo PDF em Python
linktitle: Exclua uma página específica do arquivo PDF em Python
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Aprenda como remover uma página específica de um documento PDF em Python usando Aspose.PDF, proporcionando edição eficiente de documentos.
lastmod: "2026-06-09"
---
Para excluir uma página específica do documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**Baixar código em execução**

Baixe **Excluir página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
