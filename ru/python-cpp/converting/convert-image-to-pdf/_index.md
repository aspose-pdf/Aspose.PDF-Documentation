---
title: Преобразование изображения в PDF на Python
linktitle: Преобразование изображения в файл PDF
type: docs
weight: 10
url: ru/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: Эта тема показывает, как преобразовать изображение в PDF, используя библиотеку Aspose.PDF для Python через C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Наша библиотека демонстрирует фрагменты кода для преобразования самых популярных форматов изображений - JPEG. Вы можете очень легко преобразовать изображения JPG в PDF с помощью Aspose.PDF для Python через C++, следуя шагам:

## Преобразование изображения в PDF

Вы можете очень легко преобразовать изображения JPG в PDF с помощью Aspose.PDF для C++, следуя шагам:

1. Откройте входной файл изображения, используя библиотеку PIL
1. Получите ширину и высоту изображения
1. Создайте новый экземпляр документа, используя библиотеку AsposePDFPythonWrappers
1. Установите фиксированную высоту и ширину изображения 
1. Добавьте новую страницу в документ
1. Добавьте изображение на страницу
1. Сохраните выходной PDF с помощью метода 'document.save'.

Фрагмент кода ниже показывает, как преобразовать изображение JPG в PDF, используя Python через C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Установить путь к каталогу для файлов данных
dataDir = os.path.join(os.getcwd(), "samples")

# Установить путь к входному файлу
input_file = os.path.join(dataDir, "sample.jpg")

# Установить путь к выходному файлу
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Открыть входной файл изображения с помощью библиотеки PIL
pil_img = Image.open(input_file)

# Получить ширину и высоту изображения
width, height = pil_img.size

# Создать новый экземпляр Document, используя библиотеку AsposePDFPythonWrappers
document = apw.Document()

# Создать новый экземпляр Image, используя библиотеку AsposePDFPythonWrappers
image = apw.Image()

# Установить путь к файлу изображения
image.file = input_file

# Установить фиксированную высоту и ширину изображения
image.fix_height = height
image.fix_width = width

# Добавить новую страницу в документ
page = document.pages.add()

# Добавить изображение на страницу
page.paragraphs.add(image)

# Сохранить документ по пути к выходному файлу
document.save(output_file)
```