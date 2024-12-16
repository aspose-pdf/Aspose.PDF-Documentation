---
title: Concatenar Arquivos PDF em Python
type: docs
weight: 10
url: /pt/java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

Para concatenar arquivos PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Abra o documento de origem
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Adicione as páginas do documento de origem ao documento de destino
pdf1.getPages().add(pdf1.getPages())

# Salve o arquivo de saída concatenado (o documento de destino)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "O novo documento foi salvo, por favor verifique o arquivo de saída"
```

**Baixar Código em Execução**

Baixe **Concatenar Arquivos PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)