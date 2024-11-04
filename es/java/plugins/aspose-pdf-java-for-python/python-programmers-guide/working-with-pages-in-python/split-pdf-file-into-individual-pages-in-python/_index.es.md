---
title: Dividir archivo PDF en páginas individuales en Python
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

Para dividir un documento PDF en páginas individuales utilizando **Aspose.PDF Java para PHP**, simplemente invoca la clase **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# recorrer todas las páginas
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# crear un nuevo objeto Document
new_document = self.Document();

# obtener la página en el índice particular de la Colección de Páginas
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# guardar el archivo PDF recién generado
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "¡Proceso de división completado con éxito!";
```

**Descargar Código en Ejecución**

Descarga **Split Pages (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)