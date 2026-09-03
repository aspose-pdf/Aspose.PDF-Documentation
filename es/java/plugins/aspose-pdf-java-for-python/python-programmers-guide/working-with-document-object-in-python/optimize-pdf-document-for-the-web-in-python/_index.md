---
title: Optimice el documento PDF para la Web en Python
linktitle: Optimice el documento PDF para la Web en Python
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
description: Aprenda a optimizar archivos PDF para una carga web más rápida en Python con Aspose.PDF, mejorando la experiencia del usuario y el rendimiento.
lastmod: "2026-06-09"
---

Para optimizar un documento PDF para la web usando **Aspose.PDF Java para Python**, simplemente invoque el método **optimize_web** de la clase **Optimize**.


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


**Descargar código de ejecución**

Descargue **Optimice PDF para Web (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
