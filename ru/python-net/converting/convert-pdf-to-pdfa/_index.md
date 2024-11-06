---
title: Преобразование PDF в форматы PDF/A на Python
linktitle: Преобразование PDF в форматы PDF/A
type: docs
weight: 100
url: ru/python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: Эта тема показывает, как Aspose.PDF для Python позволяет конвертировать PDF файл в файл PDF, соответствующий PDF/A. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF для Python** позволяет конвертировать PDF файл в файл PDF, соответствующий <abbr title="Portable Document Format / A">PDF/A</abbr>. Перед этим файл должен быть проверен. Эта тема объясняет, как это сделать.

{{% alert color="primary" %}}

Пожалуйста, обратите внимание, что мы следуем Adobe Preflight для проверки соответствия стандарту PDF/A. Все инструменты на рынке имеют свое собственное «представление» о соответствии PDF/A. Пожалуйста, ознакомьтесь с этой статьей о инструментах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF файлы, потому что Adobe является центром всего, что связано с PDF.

{{% /alert %}}

Преобразуйте файл, используя метод Convert класса Document.
 Before converting the PDF to PDF/A compliant file, validate the PDF using the Validate method. The validation result is stored in an XML file and then this result is also passed to the Convert method. You can also specify the action for the elements which cannot be converted using the ConvertErrorAction enumeration.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Конвертация PDF файла в PDF/A-1b

Следующий фрагмент кода показывает, как конвертировать PDF файлы в соответствующие стандарту PDF/A-1b.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # Открыть PDF документ
    document = ap.Document(input_pdf)
    # Конвертировать в документ, соответствующий стандарту PDF/A
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # Сохранить выходной документ
    document.save(output_pdf)
```