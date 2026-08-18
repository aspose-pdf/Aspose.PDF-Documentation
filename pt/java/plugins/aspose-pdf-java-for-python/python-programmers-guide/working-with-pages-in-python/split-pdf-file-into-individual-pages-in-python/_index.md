---
title: Divida o arquivo PDF em páginas individuais em Python
linktitle: Divida o arquivo PDF em páginas individuais em Python
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: Explore como dividir um PDF em páginas individuais em Python usando Aspose.PDF, permitindo fácil extração e gerenciamento de páginas.
lastmod: "2026-06-09"
---
Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java para PHP**, basta invocar a classe **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**Baixar código em execução**

Baixe **Split Pages (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
