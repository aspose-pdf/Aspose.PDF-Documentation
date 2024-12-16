---
title: Dividir Arquivo PDF em Páginas Individuais em Python
type: docs
weight: 80
url: /pt/python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **SplitAllPages**.

**Código Python**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop através de todas as páginas
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# criar um novo objeto Document
new_document = self.Document();

# obter a página em um índice particular da Coleção de Páginas
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# salvar o arquivo PDF recém-gerado
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Processo de divisão concluído com sucesso!";
```


**Baixar Código em Execução**

Baixe **Dividir Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)