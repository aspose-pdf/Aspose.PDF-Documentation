---
title: Remova metadados de PDF em Python
linktitle: Remova metadados de PDF em Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: Descubra como remover metadados de documentos PDF em Python usando Aspose.PDF, garantindo privacidade e segurança de dados.
lastmod: "2026-06-09"
---
Para remover metadados de um documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **RemoveMetadata**.

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

**Baixar código em execução**

Baixe **Remover metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
