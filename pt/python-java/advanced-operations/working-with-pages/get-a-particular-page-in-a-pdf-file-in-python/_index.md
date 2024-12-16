---
title: Obter uma Página Específica em um Arquivo PDF em Python
type: docs
weight: 30
url: /pt/python-java/get-a-particular-page-in-a-pdf-file-in-python/
---

Para obter uma Página Específica em um documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obter a página em um índice específico da Coleção de Páginas
pdf_page = pdf.getPages().get_Item(1)

# criar um novo objeto Document
new_document = self.Document()

# adicionar página à coleção de páginas do novo objeto de documento
new_document.getPages().add(pdf_page)

# salvar o arquivo PDF recém-gerado
new_document.save(self.dataDir + "output.pdf")

print "Processo concluído com sucesso!

```

**Baixar Código em Execução**

Baixe **Get Page (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)