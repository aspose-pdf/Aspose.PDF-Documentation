---
title: Obter uma página específica em um arquivo PDF em Python
linktitle: Obter uma página específica em um arquivo PDF em Python
type: docs
weight: 30
url: /pt/java/get-a-particular-page-in-a-pdf-file-in-python/
description: Explore como extrair uma página específica de um arquivo PDF em Python usando Aspose.PDF para manipulação detalhada de documentos.
lastmod: "2026-10-06"
---
Para obter uma página específica em um documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **Baixar Código em Execução**

Baixar **Obter Página (Aspose.PDF)** de qualquer dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
