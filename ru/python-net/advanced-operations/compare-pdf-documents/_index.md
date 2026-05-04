---
title: Сравнение PDF-документов в Python
linktitle: Сравнить PDF
type: docs
weight: 130
url: /python-net/compare-pdf-documents/
description: Узнайте, как сравнивать PDF-документы в Python, используя вывод различий бок о бок и графический вывод с Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Сравните страницы PDF и полные документы с визуальным выводом различий в Python
Abstract: В этой статье объясняется, как сравнивать PDF‑документы в Aspose.PDF for Python via .NET. Узнайте, как сравнивать отдельные страницы или целые PDF‑файлы с выводом рядом, а также как использовать графические методы сравнения для создания отчетов о различиях в виде изображений или PDF‑документов.
---

## Способы сравнения PDF‑документов

При работе с PDF‑документами бывают ситуации, когда необходимо сравнить содержимое двух документов, чтобы выявить различия. Библиотека Aspose.PDF for Python via .NET предоставляет мощный набор инструментов для этой цели. В этой статье мы рассмотрим, как сравнивать PDF‑документы, используя пару простых фрагментов кода.

Используйте сравнение рядом, когда вам нужен PDF‑вывод, который выделяет изменения текста и макета на разных страницах. Используйте графическое сравнение, когда требуется обнаружение различий на основе изображений для визуальных рабочих процессов, проверок регрессии или отчетов о сравнении PDF.

Функциональность сравнения в Aspose.PDF позволяет сравнивать два PDF‑документа постранично. Вы можете выбрать сравнение либо конкретных страниц, либо целых документов. Полученный документ сравнения выделяет различия, облегчая выявление изменений между двумя файлами.

Вот список возможных способов сравнения PDF‑документов с использованием библиотеки Aspose.PDF for Python via .NET:

1. **Comparing Specific Pages** - Сравните первые страницы двух PDF‑документов.
1. **Сравнение всех документов** - Сравните полное содержимое двух PDF-документов.
1. **Сравнение PDF-документов графически**:

- Сравните PDF с методом 'comparer.get_difference' - отдельные изображения, где изменения помечены.
- Сравните PDF с методом 'comparer.compare_documents_to_pdf' - PDF-документ с изображениями, где изменения помечены.

## Сравнение конкретных страниц

Первый фрагмент кода демонстрирует, как сравнить первые страницы двух PDF‑документов с использованием класса SideBySidePdfComparer.

1. Инициализация документа.
1. Создайте функцию для выполнения сравнения.
1. Процесс сравнения:

- document1.pages[1] и document2.pages[1]: - они указывают первую страницу каждого документа для сравнения. Обратите внимание, что нумерация страниц начинается с 1 в Aspose.PDF.
- SideBySideComparisonOptions - этот класс позволяет настраивать поведение сравнения.
- additional_change_marks = True - включает отображение дополнительных маркеров изменений, выделяя различия, которые могут присутствовать на других страницах, даже если они отсутствуют на текущей сравниваемой странице.
- comparison_mode = ComparisonMode.IgnoreSpaces - устанавливает режим сравнения, игнорирующий пробелы в тексте, фокусируясь только на изменениях внутри слов.

1. Результат сравнения сохраняется в новом PDF‑файле с именем ComparingSpecificPages_out.pdf в указанном каталоге data_dir.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Сравнение целых документов

Во втором фрагменте кода расширяется область сравнения, чтобы сравнить всё содержимое двух PDF‑документов.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

Предоставленный код демонстрирует сравнение двух PDF‑документов с использованием Aspose.PDF for Python via .NET. Он использует класс SideBySidePdfComparer для выполнения постраничного сравнения, создавая новый PDF, который отображает различия рядом. Сравнение настраивается с помощью SideBySideComparisonOptions, где параметр additional_change_marks установлен в True, чтобы выделять изменения не только на текущей странице, но и на других страницах, а параметр comparison_mode установлен в IgnoreSpaces, чтобы сосредоточиться на значимых различиях содержания, игнорируя вариации пробелов.

## Сравнение с использованием GraphicalPdfComparer

При совместной работе над документами, особенно в профессиональных средах, часто оказывается, что существует несколько версий одного и того же файла.
Предоставленный код демонстрирует, как визуально сравнивать конкретные страницы двух PDF‑документов с использованием Aspose.PDF for Python via .NET. Используя `GraphicalPdfComparer` класс, он выделяет различия между первыми страницами двух PDF‑файлов и генерирует соответствующие изображения, чтобы представить эти различия.

Вы можете установить следующие свойства класса:

- Resolution — разрешение в единицах DPI для выходных изображений, а также для изображений, генерируемых во время сравнения.
- Color — цвет меток изменений.
- Порог - измените порог в процентах. Значение по умолчанию равно нулю. Установка значения, отличного от нуля, позволяет игнорировать графические изменения, которые для вас несущественны.

С помощью Aspose.PDF for Python via .NET можно сравнивать документы и страницы и выводить результат сравнения в PDF‑документ или файл изображения.

Эта `GraphicalPdfComparer` класс имеет метод, который позволяет получить различия изображений страниц в формате, подходящем для дальнейшей обработки: `get_difference(document1.pages[1], document2.pages[1])`.

Этот метод возвращает объект `images_difference` тип, который содержит изображение первой сравниваемой страницы и массив различий.

Эта `images_difference` объект позволяет генерировать другое изображение и получить изображение второй страницы, сравниваемой путем применения массива различий к оригинальному изображению. Для этого используйте `difference_to_image` и `get_destination_image` методы.

### Сравнение PDF с помощью метода Get Difference

Предоставленный код определяет метод `get_difference` который сравнивает два PDF‑документа и создает визуальные представления различий между ними.

Этот метод сравнивает первые страницы двух PDF‑файлов и генерирует два PNG‑изображения:

- Одно изображение выделяет различия между страницами красным.
- Другое изображение представляет собой визуальное отображение целевой (второй) страницы PDF.

Этот процесс может быть полезен для визуального сравнения изменений или различий между двумя версиями документа.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### Сравнение PDF с методом CompareDocumentsToPdf

Предоставленный фрагмент кода использует `compare_documents_to_pdf` метод, который сравнивает два документа и генерирует PDF‑отчет о результатах сравнения.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Этот пример демонстрирует, как выполнить графическое сравнение двух полных PDF-документов с помощью Aspose.PDF for Python via .NET. Используя `GraphicalPdfComparer` класс, он генерирует новый PDF‑файл, который визуально выделяет различия между документами.

- Свойство порога установлено в 3.0, что означает, что незначительные различия ниже этого процента игнорируются при сравнении, сосредотачивая внимание на более значимых изменениях.
- Различия отмечены синим цветом путем установки свойства color в ap.Color.blue, что обеспечивает чёткое визуальное различие.
- Сравнение выполняется при разрешении 300 DPI путем установки свойства разрешения, обеспечивая детализированный и чёткий вывод.

Эта `compare_documents_to_pdf` метод сравнивает все страницы обоих документов и выводит результат в новый PDF‑файл compareDocumentsToPdf_out.pdf, с визуально подсвеченными различиями.

## Связанные темы

- [Продвинутые операции с PDF в Python](/pdf/ru/python-net/advanced-operations/)
- [Работа с PDF‑документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Работа со страницами PDF в Python](/pdf/ru/python-net/working-with-pages/)
- [Работа с текстом PDF в Python](/pdf/ru/python-net/working-with-text/)
