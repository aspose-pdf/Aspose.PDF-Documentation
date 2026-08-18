---
title: Obtenha informações do arquivo PDF em Python
linktitle: Obtenha informações do arquivo PDF em Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: Explore como recuperar informações detalhadas de arquivos PDF, como metadados e propriedades em Python usando Aspose.PDF para gerenciamento de documentos.
lastmod: "2026-06-09"
---
Para obter informações do arquivo do documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **GetPdfFileInfo**.

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

**Baixar código em execução**

Baixe ** Obtenha informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
