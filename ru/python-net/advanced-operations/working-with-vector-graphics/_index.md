---
title: Работа с векторной графикой в Python
linktitle: Работа с векторной графикой
type: docs
weight: 100
url: /ru/python-net/working-with-vector-graphics/
description: Узнайте, как извлекать, перемещать, удалять и копировать векторную графику между страницами PDF с помощью GraphicsAbsorber в Python.
lastmod: "2026-05-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Используйте GraphicsAbsorber для проверки и управления векторной графикой PDF в Python
Abstract: В этой статье объясняется, как работать с векторной графикой в Aspose.PDF for Python via .NET с помощью класса GraphicsAbsorber. Узнайте, как извлекать векторные элементы со страниц PDF, перемещать или удалять их, а также копировать графику между страницами с низкоуровневым контролем в рабочих процессах Python.
---

[Aspose.PDF for Python via .NET](/pdf/ru/python-net/) предоставляет класс [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) для доступа к векторной графике, уже присутствующей на странице PDF, и управления ею. Вызовите его метод `visit` для любой страницы, чтобы извлечь контуры, фигуры и другие графические операторы, а затем при необходимости переместить, удалить или скопировать эти элементы.

Используйте эту страницу, когда нужно проверить или изменить векторные элементы рисования, встроенные в существующий PDF, а не рисовать новые фигуры с нуля.

## Извлечение графики

Извлечение является начальной точкой для всех задач с векторной графикой. `GraphicsAbsorber` считывает поток содержимого страницы и предоставляет каждый графический элемент вместе со ссылкой на страницу, позицией и исходными операторами.

1. Откройте PDF-документ.
1. Создайте экземпляр [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/).
1. Вызовите `visit` для целевой страницы, чтобы заполнить `elements`.
1. Переберите `elements`, чтобы проверить позицию и количество операторов.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` является частью пространства имен `aspose.pdf.vector` и специально предназначен для взаимодействия с векторной графикой в потоках содержимого PDF.

## Перемещение графики

После извлечения задайте новое значение `position` для каждого элемента, чтобы переместить его на той же странице. Оберните обновления в вызовы `suppress_update` / `resume_update`, чтобы объединить запись в поток содержимого в одну операцию и избежать лишней перерисовки.

1. Откройте PDF-документ.
1. Создайте `GraphicsAbsorber` и вызовите `visit` для целевой страницы.
1. Вызовите `suppress_update`, чтобы приостановить запись в поток содержимого.
1. Обновите `position` каждого элемента.
1. Вызовите `resume_update`, чтобы применить все изменения сразу.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Удаление графики

Чтобы удалить определенные векторные элементы со страницы, отфильтруйте их по позиции или ограничивающему прямоугольнику, а затем удалите. Aspose.PDF for Python предоставляет два подхода в зависимости от того, нужно ли удалять элементы прямо в цикле или сначала собрать их.

### Метод 1: Удаление в цикле с помощью границы прямоугольника

Этот подход проверяет позицию каждого элемента относительно прямоугольника и вызывает `element.remove()` непосредственно внутри цикла. Используйте его, когда нужен краткий код и не требуется дополнительно проверять набор удаленных элементов.

1. Откройте PDF-документ.
1. Создайте `GraphicsAbsorber` и вызовите `visit` для целевой страницы.
1. Задайте целевой [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Вызовите `suppress_update`, чтобы приостановить запись в поток содержимого.
1. Переберите `elements`, вызывая `remove()` для каждого элемента, позиция которого находится внутри прямоугольника.
1. Вызовите `resume_update`, чтобы применить удаления.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Метод 2: Сбор элементов перед удалением

Этот подход собирает подходящие элементы в [GraphicElementCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) и передает коллекцию в `page.delete_graphics`. Используйте его, когда нужно просмотреть или записать в журнал элементы, которые будут удалены, перед применением удаления.

1. Откройте PDF-документ.
1. Создайте `GraphicsAbsorber` и вызовите `visit` для целевой страницы.
1. Задайте целевой прямоугольник.
1. Переберите `elements` и добавьте подходящие элементы в `GraphicElementCollection`.
1. Вызовите `page.contents.suppress_update`, чтобы приостановить запись в поток содержимого.
1. Вызовите `page.delete_graphics` с коллекцией.
1. Вызовите `page.contents.resume_update`, чтобы применить удаления.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Добавление графики на другую страницу

Векторные элементы, извлеченные с одной страницы, можно разместить на любой другой странице того же документа. Доступны два метода: добавление элементов по одному или передача всей коллекции одним вызовом.

### Метод 1: Добавление элементов по отдельности

Используйте этот метод, когда нужен контроль над каждым элементом, например фильтрация или преобразование отдельных элементов перед размещением на целевой странице.

1. Откройте PDF-документ.
1. Создайте `GraphicsAbsorber` и вызовите `visit` для исходной страницы.
1. Добавьте новую целевую страницу в документ.
1. Вызовите `page_2.contents.suppress_update`, чтобы приостановить запись в поток содержимого.
1. Вызовите `element.add_on_page(page_2)` для каждого элемента.
1. Вызовите `page_2.contents.resume_update`, чтобы применить все добавления.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Метод 2: Добавление всей коллекции сразу

Используйте этот метод, когда нужно скопировать все извлеченные элементы на страницу одной операцией без ручного перебора.

1. Откройте PDF-документ.
1. Создайте `GraphicsAbsorber` и вызовите `visit` для исходной страницы.
1. Добавьте новую целевую страницу в документ.
1. Вызовите `page_2.contents.suppress_update`, чтобы приостановить запись в поток содержимого.
1. Вызовите `page_2.add_graphics` со всей коллекцией `elements`.
1. Вызовите `page_2.contents.resume_update`, чтобы применить все добавления.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Связанные темы

- [Продвинутые операции с PDF в Python](/pdf/ru/python-net/advanced-operations/)
- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Работа с операторами PDF в Python](/pdf/ru/python-net/working-with-operators/)
- [Работа со страницами PDF в Python](/pdf/ru/python-net/working-with-pages/)
