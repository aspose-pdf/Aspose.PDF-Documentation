---
title: Преобразование PDF в формат SVG на Python
linktitle: Преобразование PDF в формат SVG на Python
type: docs
weight: 30
url: /ru/java/convert-pdf-to-svg-format-in-python/
description: Узнайте, как преобразовать PDF‑документы в формат SVG на Python с помощью Aspose.PDF для масштабируемого векторного вывода.
lastmod: "2026-09-17"
---
Для преобразования PDF в формат SVG с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **PdfToSvg**.

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

**Скачать исполняемый код**

Скачайте **Конвертировать PDF в формат SVG (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)


