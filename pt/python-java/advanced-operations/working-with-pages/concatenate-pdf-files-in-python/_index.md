---
title: Concatenar Arquivos PDF em Python
type: docs
weight: 10
url: /pt/python-java/concatenate-pdf-files-in-python/
---

Para concatenar arquivos PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Abrir o documento de origem
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Adicionar as páginas do documento de origem ao documento alvo
pdf1.getPages().add(pdf1.getPages())

# Salvar o arquivo de saída concatenado (o documento alvo)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "Novo documento foi salvo, por favor verifique o arquivo de saída"
```

**Baixar Código em Execução**

Baixe **Concatenar Arquivos PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)