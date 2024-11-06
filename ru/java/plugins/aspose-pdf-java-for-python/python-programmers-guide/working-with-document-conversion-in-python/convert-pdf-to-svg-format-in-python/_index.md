---
title: Конвертировать PDF в SVG формат на Python
type: docs
weight: 30
url: ru/java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

Чтобы конвертировать PDF в SVG формат, используя **Aspose.PDF Java для Python**, просто вызовите модуль **PdfToSvg**.

```python

# Открыть целевой документ
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# создать экземпляр объекта SvgSaveOptions
save_options = self.SvgSaveOptions()

# не сжимать изображение SVG в Zip архив
save_options.CompressOutputToZipArchive = False;

# Сохранить результат в формате XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "Документ был успешно конвертирован"
```

**Скачать код для запуска**

Скачайте **Конвертировать PDF в SVG формат (Aspose.PDF)** с любого из указанных ниже социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)