---
title: Insertar una Página Vacía en un Archivo PDF en Python
type: docs
weight: 70
url: /python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>Para Insertar una Página Vacía en un documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoca la clase **InsertEmptyPage**.

**Código Python**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insertar una página vacía en un PDF
pdf_document.getPages().insert(1)

# Guardar el archivo de salida concatenado (el documento objetivo)
pdf_document.save(self.dataDir + "output.pdf")

print "¡Página vacía añadida con éxito!"

```

**Descargar Código en Ejecución**

Descargar **Insertar una Página Vacía (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)