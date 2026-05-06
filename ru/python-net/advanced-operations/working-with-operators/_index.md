---
title: Работа с PDF-операторами в Python
linktitle: Работа с операторами
type: docs
weight: 90
url: /ru/python-net/working-with-operators/
description: Узнайте, как использовать низкоуровневые PDF-операторы в Python для точного управления потоком содержимого и графикой.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Используйте низкоуровневые PDF-операторы для управления потоком содержимого в Python
Abstract: В этой статье объясняется, как работать с низкоуровневыми операторами PDF в Aspose.PDF for Python via .NET. Узнайте, как напрямую манипулировать потоками содержимого, точно позиционировать графику с помощью классов операторов и удалять нарисованные объекты со страниц PDF в Python‑рабочих процессах.
---

## Введение в операторы PDF и их использование

Оператор — это ключевое слово PDF, определяющее действие, которое должно быть выполнено, например, рисование графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа косой черты (2Fh). Операторы имеют смысл только внутри потока содержимого.

Поток содержимого — это объект PDF‑потока, данные которого состоят из инструкций, описывающих графические элементы, которые будут отрисованы на странице. Более подробная информация об операторах PDF доступна в [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Используйте эту страницу, когда вам нужен прямой контроль над потоками содержимого PDF в Python, например размещение графики в точных координатах, оборачивание изменений состояния графики или удаление конкретных операторов рисования со страницы.

## Добавить изображения с Operator Classes

Используйте низкоуровневые классы операторов, когда необходимо разместить графическое содержимое изображения с высокой точностью в потоке страницы PDF, не полагаясь на высокоуровневые абстракции макета.

Этот метод предоставляет тонко настроенный контроль над размещением изображений в PDF путем прямой манипуляции потоком содержимого с использованием низкоуровневых графических операторов. Он особенно полезен, когда требуется точное позиционирование и преобразование изображений, например:

- добавление водяных знаков или логотипов в определённых местах.
- наложение изображений на существующее содержимое с точным выравниванием.
- реализация пользовательских макетов, недоступных при использовании более высокоуровневых абстракций.

Используя такие операторы, как GSave, ConcatenateMatrix, Do и GRestore, разработчики могут гарантировать точное отображение изображений без нежелательных побочных эффектов для другого содержимого страницы.

- The [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) оператор сохраняет текущее графическое состояние PDF.
- The [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concatenate matrix) оператор используется для определения того, как изображение должно быть размещено на странице PDF.
- The [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) оператор рисует изображение на странице.
- The [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) оператор восстанавливает графическое состояние.

Чтобы добавить изображение в PDF‑файл:

1. Откройте PDF‑документ
1. Определите координаты размещения изображения
1. Получите доступ к целевой странице
1. Загрузите изображение в поток
1. Сохраните текущее графическое состояние
1. Создайте прямоугольник и матрицу преобразования
1. Примените матрицу преобразования
1. Нарисуйте изображение
1. Восстановить предыдущее графическое состояние
1. Сохраните изменённый PDF документ

Следующий фрагмент кода показывает, как использовать PDF-операторы:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Отрисовать XForm на Page, используя Operators

В этом примере использована мощь XForms и графических операторов для эффективного повторного использования графического контента внутри PDF. Инкапсулируя изображение в XForm, его можно отрисовывать несколько раз без дублирования данных изображения, что приводит к меньшему размеру файлов и повышенной производительности. Этот подход особенно полезен, когда:

- одно и то же изображение или графика должны появляться несколько раз в документе.

- Требуется точный контроль над размещением и преобразованием графики.

- Оптимизация PDF для производительности и размера является приоритетом.

Управляя графическим состоянием с помощью GSave и GRestore и используя трансформационные матрицы с ConcatenateMatrix, этот метод гарантирует, что каждый графический объект будет отрисован корректно и независимо.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Удаление графических объектов с помощью классов операторов

Следующий фрагмент кода показывает, как удалить графику. Обратите внимание, что если PDF‑файл содержит текстовые подписи к графике, они могут оставаться в PDF‑файле при использовании этого подхода. Поэтому ищите операторы графики для альтернативного метода удаления таких изображений.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Связанные темы

- [Продвинутые операции с PDF в Python](/pdf/ru/python-net/advanced-operations/)
- [Работа со страницами PDF в Python](/pdf/ru/python-net/working-with-pages/)
- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)

