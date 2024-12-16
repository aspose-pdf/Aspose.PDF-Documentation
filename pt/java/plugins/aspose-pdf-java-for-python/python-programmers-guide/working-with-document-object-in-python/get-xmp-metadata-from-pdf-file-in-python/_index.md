---
title: Obter Metadados XMP de Arquivo PDF em Python
type: docs
weight: 50
url: /pt/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para obter Metadados XMP de um documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obter propriedades
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Baixar Código em Execução**

Baixe **Obter Metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)