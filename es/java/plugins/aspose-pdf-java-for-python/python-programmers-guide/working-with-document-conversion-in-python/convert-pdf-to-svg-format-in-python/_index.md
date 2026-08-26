---
title: Convertir PDF a formato SVG en Python
linktitle: Convert PDF to SVG Format in Python
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: Learn how to convert PDF documents to SVG format in Python using Aspose.PDF for scalable vector output.
lastmod: "2026-06-09"
---
Para convertir PDF a formato SVG usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **PdfToSvg**.

```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```

**Descargar código de ejecución**

DownloadВ **Convert PDF to SVG Format (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
