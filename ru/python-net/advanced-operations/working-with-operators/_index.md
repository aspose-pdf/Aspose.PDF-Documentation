---
title: Работа с операторами с использованием Python
linktitle: Работа с операторами
type: docs
weight: 90
url: /ru/python-net/working-with-operators/
description: Эта тема объясняет, как использовать операторы с Aspose.PDF для Python через .NET. Классы операторов предоставляют отличные возможности для работы с PDF.
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Использование операторов в PDF с Aspose.PDF для Python через .NET
Abstract: Статья представляет собой подробное изучение операторов PDF и их применения при манипуляции потоками содержимого PDF. Операторы — это специализированные ключевые слова в PDF, которые задают определённые действия, такие как отрисовка графических элементов на странице, и действуют только внутри потоков содержимого. В статье описывается метод точного контроля размещения изображений в PDF путем прямой манипуляции потоками содержимого с использованием низкоуровневых графических операторов. Такой подход полезен для задач, требующих точного позиционирования изображений, таких как добавление водяных знаков, выравнивание наложений и создание пользовательских макетов. Особое внимание уделяется отдельным операторам, таким как GSave, ConcatenateMatrix, Do и GRestore, за их роль в управлении графическими состояниями и трансформациями, обеспечивая точную отрисовку без влияния на остальное содержимое страницы.
---

## Введение в операторы PDF и их использование

Оператор — это ключевое слово PDF, определяющее действие, которое должно быть выполнено, например, отрисовка графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа слеша (2Fh). Операторы имеют смысл только внутри потока содержимого.

Поток содержимого — это объект потока PDF, данные которого состоят из инструкций, описывающих графические элементы, которые должны быть отрисованы на странице. Дополнительные сведения об операторах PDF можно найти в [спецификация PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Подробности реализации

Этот метод обеспечивает детальное управление размещением изображений в PDF путем прямой манипуляции потоком содержимого с помощью низкоуровневых графических операторов. Он особенно полезен, когда требуется точное позиционирование и трансформация изображений, например:

- добавление водяных знаков или логотипов в определённых местах.

- наложение изображений на существующее содержимое с точным выравниванием.

- реализация пользовательских макетов, недоступных через высокоуровневые абстракции.

Используя такие операторы, как GSave, ConcatenateMatrix, Do и GRestore, разработчики могут гарантировать точную отрисовку изображений без непреднамерённых побочных эффектов на другое содержимое страницы.

- The [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) оператор сохраняет текущее графическое состояние PDF.
- The [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concatenate matrix) оператор используется для определения того, как изображение должно быть размещено на странице PDF.
- The [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) оператор рисует изображение на странице.
- The [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) оператор восстанавливает графическое состояние.

Чтобы добавить изображение в файл PDF:

1. Откройте документ PDF
1. Определите координаты размещения изображения
1. Получите доступ к целевой странице
1. Загрузите изображение в поток
1. Сохраните текущее графическое состояние
1. Создайте прямоугольник и матрицу трансформации
1. Примените матрицу трансформации
1. Нарисуйте изображение
1. Восстановите предыдущее графическое состояние
1. Сохраните изменённый документ PDF

Следующий фрагмент кода демонстрирует, как использовать операторы PDF:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Рисование XForm на странице с помощью операторов

В этом примере использована мощность XForm и графических операторов для эффективного повторного использования графического содержимого в PDF. Инкапсулируя изображение в XForm, его можно рисовать многократно без дублирования данных изображения, что приводит к уменьшенному размеру файлов и повышенной производительности. Такой подход особенно полезен, когда:

- одно и то же изображение или графика должны появляться в документе несколько раз.

- требуется точный контроль над размещением и трансформацией графики.

- оптимизация PDF по производительности и размеру является приоритетом.

Управляя графическим состоянием с помощью GSave и GRestore, а также используя матрицы трансформации с ConcatenateMatrix, эта техника обеспечивает корректную и независимую отрисовку каждого графического объекта.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Удаление графических объектов с помощью классов операторов

Следующий фрагмент кода демонстрирует, как удалить графику. Обратите внимание, что если в файле PDF есть текстовые метки для графики, они могут оставаться в файле PDF при использовании этого подхода. Поэтому ищите альтернативный метод удаления таких изображений через графические операторы.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


