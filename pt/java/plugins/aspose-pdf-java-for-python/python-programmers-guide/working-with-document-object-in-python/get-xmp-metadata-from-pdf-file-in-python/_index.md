---
title: Obter Metadados XMP de Arquivo PDF em Python
linktitle: Obter Metadados XMP de Arquivo PDF em Python
type: docs
weight: 50
url: /pt/java/get-xmp-metadata-from-pdf-file-in-python/
description: Descubra como recuperar metadados XMP de um arquivo PDF em Python usando Aspose.PDF, permitindo uma análise detalhada do conteúdo.
lastmod: "2026-10-06"
---
Para obter Metadados XMP de um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar a classe **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Baixar Código em Execução**

DownloadВ **Get XMP Metadata (Aspose.PDF)**В deВ qualquer um dos sites de código social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
