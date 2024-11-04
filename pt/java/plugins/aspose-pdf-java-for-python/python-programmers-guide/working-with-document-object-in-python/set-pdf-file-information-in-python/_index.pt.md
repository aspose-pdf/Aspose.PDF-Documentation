---
title: Definir Informações do Arquivo PDF em Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Para atualizar as informações do documento Pdf usando **Aspose.PDF Java for Python**, simplesmente invoque a classe **SetPdfFileInfo**.

```python
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
print "Atualize as informações do documento, por favor verifique o arquivo de saída."
```

**Baixar Código em Execução**

Baixe **Set PDF File Information (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)