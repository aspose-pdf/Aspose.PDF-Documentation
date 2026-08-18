---
title: Obtenha metadados XMP de arquivo PDF em Python
linktitle: Obtenha metadados XMP de arquivo PDF em Python
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: Descubra como recuperar metadados XMP de um arquivo PDF em Python usando Aspose.PDF, permitindo análise detalhada de conteúdo.
lastmod: "2026-06-09"
---
Para obter metadados XMP de um documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Baixar código em execução**

Baixe **Obtenha metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
