---
title: Использование Aspose.PDF для .NET с Python
linktitle: Интеграция с Python
type: docs
weight: 100
url: /net/python-net/
description: В этом учебнике вы узнаете о различных способах создания и модификации PDF-файлов в Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

Эта статья описывает краткие примеры создания PDF с использованием интеграции Aspose.PDF для .NET с Python.

## Предварительные условия

Для использования Aspose.PDF для .NET в Python, пожалуйста, используйте следующий `requirments.txt`:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

Также вы должны поместить `Aspose.PDF.dll` в нужную папку.

## Создание простого PDF с помощью Python

Для работы нам потребуется интегрировать [PythonNet](https://github.com/pythonnet/pythonnet) в наше приложение и выполнить некоторую настройку.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### Создание простого документа

Давайте создадим простой PDF с классическим текстом "Привет, мир". Для более подробного объяснения, пожалуйста, перейдите на [эту страницу](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self, licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Инициализация объекта документа
        document = Document()
        # Добавление страницы
        page = document.Pages.Add()
        # Добавление текста на новую страницу
        textFragment = TextFragment("Привет, мир!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Создание объекта TextBuilder
        textBuilder = TextBuilder(page)

        # Добавление текстового фрагмента на страницу PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Создание сложных PDF-документов с использованием Python

Следующие примеры показывают, как мы можем создать сложный PDF-документ с изображениями и таблицами. Этот пример основан на [следующей странице](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... пропущено ...

    # Создание сложного документа
    def run_complex(self):

        # Инициализация объекта документа
        document = Document()
        # Добавление страницы
        page = document.Pages.Add()

        # Добавление изображения
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Добавление заголовка
        header = TextFragment("Новые маршруты паромов осенью 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Добавление описания
        descriptionText = "Посетители должны покупать билеты онлайн, и количество билетов ограничено 5,000 в день. \
        Паромная служба работает с половинной загрузкой и по сокращенному расписанию. Ожидайте очередей."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # Добавление таблицы
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Город отправления")
        headerRow.Cells.Add("Остров отправления")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## Как запустить генерацию PDF-файлов в Windows

Этот фрагмент показывает, как запустить приведенные выше примеры на ПК с Windows. Предполагается, что `class HelloWorld` находится в файле `example_get_started.py`.
Если вы используете пробную версию Aspose.PDF для .NET, вы должны передать пустую строку в качестве `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
