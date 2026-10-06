---
title: Concatenar Arquivos PDF em Python
linktitle: Concatenar Arquivos PDF em Python
type: docs
weight: 10
url: /pt/java/concatenate-pdf-files-in-python/
description: Aprenda como concatenar vários arquivos PDF em um único documento PDF em Python usando Aspose.PDF, simplificando o gerenciamento de documentos.
lastmod: "2026-10-06"
---
Para concatenar arquivos PDF usando **Aspose.PDF Java for Python**, simplesmente invoque a classe **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

**Baixar Código em Execução**

DownloadВ **Concatenate PDF Files (Aspose.PDF)**В deВ qualquer dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
