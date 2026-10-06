---
title: Remover Metadados de PDF em Python
linktitle: Remover Metadados de PDF em Python
type: docs
weight: 70
url: /pt/java/remove-metadata-from-pdf-in-python/
description: Descubra como remover metadados de documentos PDF em Python usando Aspose.PDF, garantindo privacidade e segurança dos dados.
lastmod: "2026-10-06"
---
Para remover Metadados de um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar a classe **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```

**Baixar Código Executável**

BaixeВ **Remove Metadata (Aspose.PDF)**В deВ qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
