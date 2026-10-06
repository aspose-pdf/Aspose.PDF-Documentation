---
title: Converter PDF para o formato SVG em Python
linktitle: Converter PDF para o formato SVG em Python
type: docs
weight: 30
url: /pt/java/convert-pdf-to-svg-format-in-python/
description: Aprenda como converter documentos PDF para o formato SVG em Python usando Aspose.PDF para saída vetorial escalável.
lastmod: "2026-10-06"
---
Para converter PDF para o formato SVG usando **Aspose.PDF Java for Python**, basta invocar o módulo **PdfToSvg**.

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

**Baixar Código em Execução**

DownloadВ **Converter PDF para Formato SVG (Aspose.PDF)**В deВ qualquer dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
