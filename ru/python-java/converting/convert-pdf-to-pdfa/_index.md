---
title: Convert PDF to PDF/A formats in Python
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: /ru/python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: Эта тема показывает, как Aspose.PDF for Python через Python позволяет преобразовать PDF файл в PDF/A совместимый PDF файл.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python** позволяет вам преобразовать PDF файл в <abbr title="Portable Document Format / A">PDF/A</abbr> совместимый PDF файл. Перед этим файл должен быть проверен. В этой теме объясняется, как это сделать.

{{% alert color="primary" %}}

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют свою собственную «репрезентацию» соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о средствах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF файлы, потому что Adobe находится в центре всего, что связано с PDF.

{{% /alert %}}

Преобразуйте файл, используя метод Convert класса Document.
 Перед преобразованием PDF в файл, соответствующий PDF/A, проверьте PDF, используя метод Validate. Результат проверки сохраняется в XML-файле, и этот результат также передается в метод Convert. Вы также можете указать действие для элементов, которые не могут быть преобразованы, используя перечисление ConvertErrorAction.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PDF/A онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Преобразование файла PDF в PDF/A-1b

Следующий фрагмент кода показывает, как преобразовать файлы PDF в PDF, соответствующий PDF/A-1b.

```python
from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# Открыть PDF документ
document = Api.Document(input_pdf)
# Преобразовать в документ, соответствующий PDF/A
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# Сохранить выходной документ
document.save(output_pdf)
```