---
title: Definir Informações do Arquivo PDF em Python
type: docs
weight: 90
url: pt/python-java/set-pdf-file-information-in-python/
---

<ins>Para atualizar as informações do documento Pdf usando **Aspose.PDF Java para Python**, basta invocar a classe **SetPdfFileInfo**.

**Código Python**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obter informações do documento
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF para java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Informações do PDF");
doc_info.setTitle("Definindo Informações do Documento PDF");

# salvar documento atualizado com novas informações

doc.save(self.dataDir + "Updated_Information.pdf")
print "Atualizar informações do documento, por favor verifique o arquivo de saída."
```

**Baixar Código em Execução**

Baixe **Definir Informações do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)