---
title: Definir expiração de PDF em Python
linktitle: Definir expiração de PDF em Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: Aprenda como definir uma data de expiração para um arquivo PDF em Python usando Aspose.PDF para acesso a documentos urgentes.
lastmod: "2026-06-09"
---
Para definir a expiração do documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```

**Baixar código em execução**

Baixe **Definir expiração de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
