---
title: Сравнение PDF документов
linktitle: Сравнить PDF
type: docs
weight: 130
url: /ru/python-net/compare-pdf-documents/
description: Можно сравнить содержимое PDF документов с помощью отметок аннотаций и вывода бок о бок.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Способы сравнения PDF документов

При работе с PDF документами иногда требуется сравнить содержимое двух документов, чтобы выявить различия. Библиотека Aspose.PDF для Python через .NET предоставляет мощный набор инструментов для этой задачи. В этой статье мы рассмотрим, как сравнивать PDF документы, используя несколько простых фрагментов кода.

Функция сравнения в Aspose.PDF позволяет сравнивать два PDF документа постранично. Вы можете выбрать сравнение отдельных страниц или целых документов. Полученный документ сравнения выделяет различия, упрощая обнаружение изменений между двумя файлами.

Вот список возможных способов сравнения PDF документов с использованием библиотеки Aspose.PDF для Python через .NET:

1. **Сравнение конкретных страниц** - Сравнение первых страниц двух PDF документов.
1. **Сравнение целых документов** - Сравнение полного содержимого двух PDF документов.
1. **Графическое сравнение PDF документов**:

- Сравнение PDF с помощью метода 'comparer.get_difference' — отдельные изображения, где отмечены изменения.
- Сравнение PDF с помощью метода 'comparer.compare_documents_to_pdf' — PDF документ с изображениями, где отмечены изменения.

## Сравнение конкретных страниц

Первый фрагмент кода демонстрирует, как сравнить первые страницы двух PDF документов с использованием класса SideBySidePdfComparer.

1. Инициализация документа.
1. Создание функции для выполнения сравнения.
1. Процесс сравнения:

- document1.pages[1] и document2.pages[1]: - указывают первую страницу каждого документа для сравнения. Обратите внимание, что нумерация страниц в Aspose.PDF начинается с 1.
- SideBySideComparisonOptions — этот класс позволяет настроить поведение сравнения.
- additional_change_marks = True — включает отображение дополнительных маркеров изменений, выделяя различия, которые могут присутствовать на других страницах, даже если их нет на текущей сравниваемой странице.
- comparison_mode = ComparisonMode.IgnoreSpaces — задаёт режим сравнения игнорировать пробелы в тексте, сосредотачивая внимание только на изменениях внутри слов.

1. Результат сравнения сохраняется в новый PDF файл с именем ComparingSpecificPages_out.pdf в указанном каталоге data_dir.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Сравнение целых документов

Второй фрагмент кода расширяет область сравнения, позволяя сравнить полное содержимое двух PDF документов.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

Приведённый код демонстрирует сравнение двух PDF документов с использованием Aspose.PDF для Python через .NET. Он использует класс SideBySidePdfComparer для постраничного сравнения, создавая новый PDF, в котором различия отображаются рядом. Сравнение настроено с помощью SideBySideComparisonOptions, где параметр additional_change_marks установлен в True для выделения изменений не только на текущей странице, но и на других, а параметр comparison_mode установлен в IgnoreSpaces, чтобы сосредоточиться на значимых различиях в содержимом, игнорируя пробельные вариации.

## Сравнение с использованием GraphicalPdfComparer

При совместной работе над документами, особенно в профессиональной сфере, часто возникает несколько версий одного и того же файла.
Приведённый код демонстрирует, как визуально сравнивать конкретные страницы двух PDF документов с использованием Aspose.PDF для Python через .NET. При помощи класса `GraphicalPdfComparer` он выделяет различия между первыми страницами двух PDF и генерирует соответствующие изображения, представляющие эти различия.

Вы можете установить следующие свойства класса:

- Resolution — разрешение в DPI для выходных изображений, а также для изображений, генерируемых во время сравнения.
- Color — цвет отметок изменений.
- Threshold — порог изменения в процентах. Значение по умолчанию равно нулю. Установка отличного от нуля значения позволяет игнорировать графические изменения, не имеющие значения для вас.

С помощью Aspose.PDF для Python через .NET можно сравнивать документы и страницы и выводить результат сравнения в PDF документ или файл изображения.

Класс `GraphicalPdfComparer` имеет метод, позволяющий получить различия изображений страниц в виде, пригодном для дальнейшей обработки: `get_difference(document1.pages[1], document2.pages[1])`.

Этот метод возвращает объект типа `images_difference`, который содержит изображение первой сравниваемой страницы и массив различий.

Объект `images_difference` позволяет создать другое изображение и получить изображение второй сравниваемой страницы, применив массив различий к оригинальному изображению. Для этого используйте методы `difference_to_image` и `get_destination_image`.

### Сравнение PDF методом Get Difference

Приведённый код определяет метод `get_difference`, который сравнивает два PDF документа и создаёт визуальные представления различий между ними.

Этот метод сравнивает первые страницы двух PDF файлов и генерирует два PNG изображения:

- Одно изображение выделяет различия между страницами красным цветом.
- Другое изображение представляет собой визуальное представление целевой (второй) страницы PDF.

Этот процесс может быть полезен для визуального сравнения изменений или различий между двумя версиями документа.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Сравнение PDF с методом CompareDocumentsToPdf

Предоставленный фрагмент кода использует метод `compare_documents_to_pdf`, который сравнивает два документа и создает PDF‑отчет о результатах сравнения.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

В этом примере показано, как выполнить графическое сравнение двух полных PDF‑документов с помощью Aspose.PDF для Python через .NET. Используя класс `GraphicalPdfComparer`, он создает новый PDF‑файл, визуально выделяющий различия между документами.

- Свойство порога установлено в 3.0, что означает, что незначительные различия ниже этого процентного значения игнорируются при сравнении, фокусируясь на более существенных изменениях.
- Различия помечаются синим цветом путем установки свойства цвета в ap.Color.blue, обеспечивая четкое визуальное различие.
- Сравнение выполняется с разрешением 300 DPI путем установки свойства разрешения, обеспечивая детальный и четкий вывод.

Метод `compare_documents_to_pdf` сравнивает все страницы обоих документов и выводит результат в новый PDF‑файл compareDocumentsToPdf_out.pdf, с визуально выделенными различиями.

