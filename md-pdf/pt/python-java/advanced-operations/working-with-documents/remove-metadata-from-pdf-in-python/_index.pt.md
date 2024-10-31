---
title: Remover Metadados de PDF em Python
type: docs
weight: 70
url: /python-java/remove-metadata-from-pdf-in-python/
---

<ins>Para remover Metadados de um documento Pdf usando **Aspose.PDF Java para Python**, simplesmente invoque a classe **RemoveMetadata**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# salvar documento atualizado com novas informações
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Metadados removidos com sucesso, por favor verifique o arquivo de saída."
```


**Baixar Código em Execução**

Baixe **Remover Metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)