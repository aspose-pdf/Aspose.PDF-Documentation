---
title: Atualizar dimensões da página no Python
linktitle: Atualizar dimensões da página no Python
type: docs
weight: 90
url: /pt/java/update-page-dimensions-in-python/
description: Entenda como atualizar as dimensões da página em um documento PDF em Python usando Aspose.PDF para melhor controle do layout do documento.
lastmod: "2026-10-06"
---
Para atualizar as dimensões da página usando **Aspose.PDF Java for Python**, basta invocar a classe **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**Baixar Código em Execução**

Download **Atualizar Dimensões da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
