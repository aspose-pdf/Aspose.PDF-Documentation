---
title: Adicionar TOC a um PDF Existente em Python
type: docs
weight: 20
url: pt/python-java/add-toc-to-existing-pdf-in-python/
---

Para adicionar TOC em um documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **AddToc**.

```python

# Abrir um documento PDF.
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Acessar a primeira página do arquivo PDF
toc_page = doc.getPages().insert(1)

# Criar objeto para representar as informações do TOC
toc_info = self.TocInfo()
title = self.TextFragment("Índice")
title.getTextState().setFontSize(20)

# Definir o título para o TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Criar objetos string que serão usados como elementos do TOC
titles = ["Primeira página", "Segunda página"]

i = 0;
while (i < 2):

# Criar objeto Heading
heading2 = self.Heading(1)

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Especificar a página de destino para o objeto heading
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Página de destino
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Coordenada de destino
segment2.setText(titles[i])

# Adicionar heading à página contendo o TOC
toc_page.getParagraphs().add(heading2)

i += 1

# Salvar Documento PDF
doc.save(self.dataDir + "TOC.pdf")

print "TOC adicionado com sucesso, por favor verifique o arquivo de saída."
```


**Download Running Code**

Baixar **Adicionar TOC (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)