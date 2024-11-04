---
title: Optimizar Documento PDF para la Web en Python
type: docs
weight: 60
url: /python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>Para optimizar un documento PDF para la web usando **Aspose.PDF Java para Python**, simplemente invoque el método **optimize_web** de la clase **Optimize**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimizar para la web
doc.optimize();

# Guardar documento de salida
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF optimizado para la Web, por favor revise el archivo de salida."
```


**Descargar Código en Ejecución**

Descargue **Optimizar PDF para la Web (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)