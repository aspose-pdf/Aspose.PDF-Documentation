---
title: Obter informações de arquivo PDF em Python
linktitle: Obter informações de arquivo PDF em Python
type: docs
weight: 40
url: /pt/java/get-pdf-file-information-in-python/
description: Explore como recuperar informações detalhadas de arquivo PDF, como metadados e propriedades, em Python usando Aspose.PDF para gerenciamento de documentos.
lastmod: "2026-10-06"
---
Para obter informações de arquivo de documento Pdf usando **Aspose.PDF Java for Python**, basta invocar a classe **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**Download do Código em Execução**

Download **Obter Informações do Arquivo PDF (Aspose.PDF)** de  qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
