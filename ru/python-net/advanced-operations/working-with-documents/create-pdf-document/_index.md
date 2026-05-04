---
title: Создание PDF файлов в Python
linktitle: Создать PDF Document
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Узнайте, как создавать PDF файлы и создавать поисковые PDF в Python, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Создать PDF файл с Python
Abstract: Aspose.PDF for Python via .NET — это универсальный API, предназначенный для разработчиков, позволяющий манипулировать PDF‑файлами в Python‑приложениях, ориентированных на платформу .NET. Он позволяет пользователям легко создавать, загружать, изменять и конвертировать PDF‑документы. В этой статье представлено пошаговое руководство по созданию простого PDF‑файла с помощью Aspose.PDF. Процесс включает инициализацию объекта `Document`, добавление `Page` в документ, вставку `TextFragment` в абзацы страницы и сохранение файла в формате PDF. Включённый фрагмент кода на Python демонстрирует эти шаги, создавая PDF‑документ, содержащий текст "Hello World!". Этот API упрощает работу с PDF при минимальном количестве кода, повышая производительность разработчиков, работающих с PDF в среде .NET.
---

**Aspose.PDF for Python via .NET** — это API для работы с PDF, позволяющее разработчикам создавать, загружать, изменять и конвертировать PDF‑файлы напрямую из Python для приложений .NET, используя всего несколько строк кода.

Используйте эти примеры, когда вам нужно создать новые PDF-файлы с нуля или преобразовать вывод OCR в поисковые PDF-документы на Python.

## Как создать простой PDF-файл

Чтобы создать PDF с помощью Python via .NET и Aspose.PDF, вы можете выполнить следующие шаги:

1. Создайте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс
1. Добавить [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объект к [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) коллекция объекта Document
1. Добавить [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) в [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) коллекция страницы
1. Сохранить полученный PDF документ

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## Как создать поисковый PDF‑документ

Aspose.PDF for Python via .NET позволяет создавать и изменять существующие PDF‑документы. При добавлении текстовых элементов в PDF‑файл полученный PDF становится поисковым. Однако при преобразовании изображения, содержащего текст, в PDF‑файл содержимое получаемого PDF не является поисковым. В качестве обходного решения мы можем применить OCR к полученному файлу, чтобы он стал поисковым.

Ниже приведён полный код для выполнения этого требования:

1. Загрузите PDF с помощью 'ap.Document'.
1. Настройте разрешение рендеринга.
1. Используйте 'PngDevice.process' для преобразования выбранной страницы PDF в изображение.
1. Выполните OCR на полученном изображении.
1. Создайте новый PDF из вывода OCR.
1. Сохраните поисковый PDF.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Форматировать PDF документы в Python](/pdf/ru/python-net/formatting-pdf-document/)
- [Манипулировать PDF документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)
- [Оптимизировать PDF файлы в Python](/pdf/ru/python-net/optimize-pdf/)

