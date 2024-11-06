---
title: Inserir uma Página Vazia no Final do Arquivo PDF em Python
type: docs
weight: 60
url: pt/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para inserir uma página vazia no final de um documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insira uma página vazia em um PDF
pdf_document.getPages().add();

# Salve o arquivo de saída concatenado (o documento de destino)
pdf_document.save(self.dataDir + "output.pdf")

print "Página vazia adicionada com sucesso!"

```

**Baixar Código em Execução**

Baixe **Inserir uma Página Vazia no Final do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)