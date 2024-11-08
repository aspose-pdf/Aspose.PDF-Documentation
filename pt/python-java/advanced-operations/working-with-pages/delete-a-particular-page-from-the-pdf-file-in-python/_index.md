---
title: Excluir uma Página Específica do Arquivo PDF em Python
type: docs
weight: 20
url: /pt/python-java/excluir-uma-pagina-especifica-do-arquivo-pdf-em-python/
---

Para excluir uma página específica do documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **DeletePage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# excluir uma página específica
pdf.getPages().delete(2)

# salvar o arquivo PDF recém-gerado
doc.save(self.dataDir + "output.pdf")

print "Página excluída com sucesso!"

```

**Baixar Código em Execução**

Baixe **Excluir Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)