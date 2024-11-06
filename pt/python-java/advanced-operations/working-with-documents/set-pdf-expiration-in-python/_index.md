---
title: Definir Expiração de PDF em Python
type: docs
weight: 80
url: pt/python-java/set-pdf-expiration-in-python/
---

<ins>Para definir a expiração de um documento Pdf usando **Aspose.PDF Java for Python**, basta invocar a classe **SetExpiration**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('O arquivo está expirado. Você precisa de um novo.');");

doc.setOpenAction(javascript);

# salvar documento atualizado com novas informações
doc.save(self.dataDir + "set_expiration.pdf");

print "Atualizar informações do documento, por favor verifique o arquivo de saída."
```

**Baixar Código em Execução**

Baixe **Definir Expiração de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
 - [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)