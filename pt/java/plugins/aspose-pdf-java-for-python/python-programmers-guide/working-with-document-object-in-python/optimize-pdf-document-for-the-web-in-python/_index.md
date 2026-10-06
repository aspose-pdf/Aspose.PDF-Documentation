---
title: Otimizar documento PDF para a web em Python
linktitle: Otimizar documento PDF para a web em Python
type: docs
weight: 60
url: /pt/java/optimize-pdf-document-for-the-web-in-python/
description: Aprenda como otimizar arquivos PDF para carregamento mais rápido na web em Python com Aspose.PDF, melhorando a experiência do usuário e o desempenho.
lastmod: "2026-10-06"
---
Para otimizar o documento PDF para a web usando **Aspose.PDF Java for Python**, basta invocar o método **optimize_web** da classe **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimize for web
doc.optimize();

#Save output document
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Optimized PDF for the Web, please check output file."
```

**Baixar Código em Execução**

Download **Optimize PDF for Web (Aspose.PDF)** de qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
