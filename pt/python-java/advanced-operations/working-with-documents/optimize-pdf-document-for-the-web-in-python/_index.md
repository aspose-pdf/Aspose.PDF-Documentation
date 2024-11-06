---
title: Otimizar Documento PDF para a Web em Python
type: docs
weight: 60
url: pt/python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>Para otimizar o documento PDF para a web usando **Aspose.PDF Java para Python**, basta invocar o método **optimize_web** da classe **Optimize**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Otimizar para a web
doc.optimize();

#Salvar documento de saída
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF otimizado para a Web, por favor verifique o arquivo de saída."
```


**Baixar Código em Execução**

Baixe **Otimizar PDF para Web (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)