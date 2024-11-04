---
title: Inserir uma Página Vazia em um Arquivo PDF em Python
type: docs
weight: 70
url: /python-java/inserir-uma-pagina-vazia-em-um-arquivo-pdf-em-python/
---

<ins>Para inserir uma página vazia em um documento Pdf usando **Aspose.PDF Java para Python**, basta invocar a classe **InsertEmptyPage**.

**Código Python**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insere uma página vazia em um PDF
pdf_document.getPages().insert(1)

# Salvar o arquivo de saída concatenado (o documento de destino)
pdf_document.save(self.dataDir + "output.pdf")

print "Página vazia adicionada com sucesso!"

```

**Download do Código em Execução**

Baixe **Inserir uma Página Vazia (Aspose.PDF)** em qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)