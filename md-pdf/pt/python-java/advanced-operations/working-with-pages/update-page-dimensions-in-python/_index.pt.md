---
title: Atualizar Dimensões da Página em Python
type: docs
weight: 90
url: /python-java/update-page-dimensions-in-python/
---

<ins>Para atualizar as dimensões da página usando **Aspose.PDF Java para Python**, basta invocar a classe **UpdatePageDimensions**.

**Código Python**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obter coleção de páginas
page_collection = pdf.getPages()

# obter página específica
pdf_page = page_collection.get_Item(1)

# definir o tamanho da página como A4 (11,7 x 8,3 pol) e no Aspose.PDF, 1 polegada = 72 pontos
# portanto, as dimensões A4 em pontos serão (842,4, 597,6)
pdf_page.setPageSize(597.6,842.4)

# salvar o arquivo PDF recém-gerado
pdf.save(self.dataDir + "output.pdf")

print "Dimensões atualizadas com sucesso!"

```

**Baixar Código em Execução**

Baixe **Atualizar Dimensões da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)