---
title: Inserir uma Página Vazia em um Arquivo PDF em Python
type: docs
weight: 70
url: pt/java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para inserir uma página vazia em um documento PDF usando **Aspose.PDF Java for Python**, basta chamar a classe **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insere uma página vazia em um PDF
pdf_document.getPages().insert(1)

# Salvar o arquivo de saída concatenado (o documento de destino)
pdf_document.save(self.dataDir + "output.pdf")

print "Página vazia adicionada com sucesso!"

```

**Baixar Código em Execução**

Baixe **Inserir uma Página Vazia (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)