---
title: Convertir PDF a formato SVG en Python
type: docs
weight: 30
url: es/java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

Para convertir PDF a formato SVG usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **PdfToSvg**.

```python

# Abrir el documento objetivo
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instanciar un objeto de SvgSaveOptions
save_options = self.SvgSaveOptions()

# no comprimir la imagen SVG en un archivo Zip
save_options.CompressOutputToZipArchive = False;

# Guardar la salida en formato XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "El documento ha sido convertido exitosamente"
```

**Descargar Código en Ejecución**

Descargar **Convertir PDF a formato SVG (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)