---
title: Converter PDF para formato SVG em Python
linktitle: Converter PDF para formato SVG em Python
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: Aprenda como converter documentos PDF para o formato SVG em Python usando Aspose.PDF para saída vetorial escalonável.
lastmod: "2026-06-09"
---
Para converter PDF para o formato SVG usando **Aspose.PDF Java para Python**, basta invocar o módulo **PdfToSvg**.

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

**Baixar código em execução**

Baixe **Converter PDF para formato SVG (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
