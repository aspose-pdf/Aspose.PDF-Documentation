---
title: Работа с векторной графикой в Python
linktitle: Работа с векторной графикой
type: docs
weight: 100
url: /python-net/working-with-vector-graphics/
description: Узнайте, как извлекать, перемещать, удалять и повторно использовать векторную графику в PDF‑файлах с помощью Python.
lastmod: "2026-04-17"
TechArticle: true 
AlternativeHeadline: Используйте GraphicsAbsorber для анализа и манипулирования векторной графикой PDF в Python.
Abstract: В этой статье объясняется, как работать с векторной графикой в Aspose.PDF for Python via .NET с использованием класса GraphicsAbsorber. Узнайте, как извлекать векторные элементы со страниц PDF, перемещать или удалять их, а также копировать графику между страницами, имея низкоуровневый контроль в рабочих процессах Python.
---

В этой главе мы исследуем, как использовать мощный `GraphicsAbsorber` класс для взаимодействия с векторной графикой в PDF‑документах. Независимо от того, нужно ли вам перемещать, удалять или добавлять графику, это руководство покажет, как эффективно выполнять эти задачи.

Используйте эту страницу, когда нужно проверить или изменить векторные графические элементы, уже присутствующие на странице PDF, такие как контуры, формы и переиспользуемые графические объекты.

## Введение

Векторная графика является важным компонентом многих PDF‑документов, используемым для представления изображений, фигур и других графических элементов. Aspose.PDF предоставляет `GraphicsAbsorber` класс, который позволяет разработчикам программно получать доступ к этим графикам и управлять ими. Используя `Visit` метод `GraphicsAbsorber`, вы можете извлекать векторную графику с указанной страницы и выполнять различные операции, такие как перемещение, удаление или копирование её на другие страницы.

## Общие задачи векторной графики

## Извлечение графики

Первый шаг в работе с векторной графикой — извлечь её из PDF‑документа. Вот как вы можете сделать это, используя `GraphicsAbsorber` класс:

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечь графику со страницы.
1. Перебрать и отобразить извлечённые элементы.

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

Класс GraphicsAbsorber является частью пространства имён aspose.pdf.vector и специально разработан для взаимодействия с векторной графикой в PDF‑документах.

## Движущаяся графика

После того как вы извлекли графику, вы можете переместить её в другое положение на той же странице. Вот как это сделать:

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов.
1. Приостановка обновлений для повышения производительности.
1. Изменение позиций графических элементов.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

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

Существуют сценарии, когда вы хотите удалить конкретные графические элементы со страницы. Aspose.PDF for Python предлагает два метода для достижения этой цели:

### Метод 1: Использование границы прямоугольника

В следующем примере показано, как удалить векторные графические элементы, расположенные в определённой прямоугольной области на первой странице PDF‑документа с использованием библиотеки Aspose.PDF for Python via .NET. Этот процесс включает идентификацию графических элементов внутри заданного прямоугольника и их удаление для очистки или изменения содержимого PDF.

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов.
1. Определение целевого прямоугольника.
1. Приостановка обновлений для повышения производительности.
1. Удаление графических элементов внутри прямоугольника.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

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

### Метод 2: Использование коллекции удалённых элементов

В следующем примере показано, как удалить векторные графические элементы, расположенные в определённой прямоугольной области на первой странице PDF‑документа с использованием библиотеки Aspose.PDF for Python via .NET. Этот процесс включает идентификацию графических элементов внутри заданного прямоугольника и их удаление для очистки или изменения содержимого PDF.

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Определение целевого прямоугольника.
1. Извлечение графических элементов.
1. Создание коллекции для удаления.
1. Определение элементов внутри прямоугольника.
1. Приостановка обновлений для повышения производительности.
1. Удаление графических элементов.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

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

Графика, поглощённая с одной страницы, может быть добавлена на другую страницу в том же документе.
Вот два способа достичь этого:

### Метод 1: Добавление графики по отдельности

Следующий пример копирует элементы векторной графики с первой страницы PDF‑документа и вставляет их на вторую страницу. Эта операция реализуется с помощью класса GraphicsAbsorber, который позволяет извлекать и управлять векторной графикой в PDF‑документах.

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов с первой страницы.
1. Приостановка обновлений на второй странице для повышения производительности.
1. Добавление извлечённых графических элементов на вторую страницу.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

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

### Метод 2: Добавление графики в виде коллекции

Следующий пример демонстрирует дублирование элементов векторной графики с первой страницы PDF‑документа и их размещение на второй странице. Это достигается с помощью класса GraphicsAbsorber, который облегчает извлечение и манипулирование векторной графикой в PDF‑документах.

1. Откройте PDF Document.
1. Инициализировать GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов с первой страницы.
1. Приостановка обновлений на второй странице для повышения производительности.
1. Добавление извлечённых графических элементов на вторую страницу.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

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