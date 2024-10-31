---
title: Obter Informações de Arquivo PDF em Python
type: docs
weight: 40
url: /python-java/get-pdf-file-information-in-python/
---

<ins>Para obter informações de arquivo de um documento PDF usando **Aspose.PDF Java para Python**, simplesmente invoque a classe **GetPdfFileInfo**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obter informações do documento
doc_info = doc.getInfo();

# Mostrar informações do documento
print "Autor:-" + str(doc_info.getAuthor())
print "Data de Criação:-" + str(doc_info.getCreationDate())
print "Palavras-chave:-" + str(doc_info.getKeywords())
print "Data de Modificação:-" + str(doc_info.getModDate())
print "Assunto:-" + str(doc_info.getSubject())
print "Título:-" + str(doc_info.getTitle())
```

**Baixar Código em Execução**

Baixe **Obter Informações de Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)