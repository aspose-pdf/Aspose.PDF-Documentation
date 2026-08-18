---
title: Definir informações do arquivo PDF em Python
linktitle: Definir informações do arquivo PDF em Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: Aprenda como definir informações de arquivos PDF, como autor, título e muito mais em Python usando Aspose.PDF para organizar documentos.
lastmod: "2026-06-09"
---
Para atualizar as informações do documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**Baixar código em execução**

Baixe **Definir informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
