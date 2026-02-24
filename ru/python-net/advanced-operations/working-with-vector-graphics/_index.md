---
title: Работа с векторной графикой с использованием Python
linktitle: Работа с векторной графикой
type: docs
weight: 100
url: /ru/python-net/working-with-vector-graphics/
description: В этой статье описаны возможности работы с инструментом GraphicsAbsorber с использованием Python.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Используйте инструмент GraphicsAbsorber в PDF с Python
Abstract: Документация Aspose.PDF for Python via .NET по статье «Работа с векторной графикой» предоставляет всестороннее руководство для разработчиков, стремящихся манипулировать векторной графикой в PDF‑документах с помощью класса GraphicsAbsorber. Этот класс облегчает извлечение, перемещение, удаление и дублирование элементов векторной графики на страницах PDF.
---

В этой главе мы исследуем, как использовать мощный класс `GraphicsAbsorber` для взаимодействия с векторной графикой в PDF‑документах. Независимо от того, нужно ли вам перемещать, удалять или добавлять графику, это руководство покажет, как эффективно выполнять эти задачи.

## Введение

Векторная графика является важным компонентом многих PDF‑документов, используемым для представления изображений, фигур и других графических элементов. Aspose.PDF предоставляет класс `GraphicsAbsorber`, который позволяет разработчикам программно получать доступ к этой графике и управлять ею. Используя метод `Visit` класса `GraphicsAbsorber`, вы можете извлекать векторную графику с указанной страницы и выполнять различные операции, такие как перемещение, удаление или копирование её на другие страницы.

## Извлечение графики

Первым шагом в работе с векторной графикой является её извлечение из PDF‑документа. Вот как можно сделать это с помощью класса `GraphicsAbsorber`:

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлеките графику со страницы.
1. Итеративно пройдитесь и отобразите извлечённые элементы.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

Класс GraphicsAbsorber входит в пространство имён aspose.pdf.vector и специально разработан для взаимодействия с векторной графикой в PDF‑документах.

## Перемещение графики

После извлечения графики вы можете переместить её в другое положение на той же странице. Вот как это можно сделать:

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов.
1. Приостановка обновлений для повышения производительности.
1. Изменение позиций графических элементов.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновлённого документа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Удаление графики

Существует ситуации, когда вам может потребоваться удалить определённую графику со страницы. Aspose.PDF for Python предлагает два метода для этого:

### Метод 1: Использование прямоугольной границы

Следующий пример демонстрирует, как удалить элементы векторной графики, расположенные в определённой прямоугольной области на первой странице PDF‑документа, используя библиотеку Aspose.PDF for Python via .NET. Этот процесс включает идентификацию графических элементов внутри заданного прямоугольника и их удаление для очистки или изменения содержимого PDF.

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов.
1. Определение целевого прямоугольника.
1. Приостановка обновлений для повышения производительности.
1. Удаление графических элементов внутри прямоугольника.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновлённого документа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Метод 2: Использование коллекции удалённых элементов

Следующий пример демонстрирует, как удалить элементы векторной графики, расположенные в определённой прямоугольной области на первой странице PDF‑документа, используя библиотеку Aspose.PDF for Python via .NET. Этот процесс включает идентификацию графических элементов внутри заданного прямоугольника и их удаление для очистки или изменения содержимого PDF.

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Определение целевого прямоугольника.
1. Извлечение графических элементов.
1. Создание коллекции для удаления.
1. Идентификация элементов внутри прямоугольника.
1. Приостановка обновлений для повышения производительности.
1. Удаление графических элементов.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Добавление графики на другую страницу

Графика, поглощенная с одной страницы, может быть добавлена на другую страницу в том же документе.
Вот два метода, которые позволяют это сделать:

### Метод 1: Добавление графики по отдельности

Следующий пример копирует векторные графические элементы с первой страницы PDF‑документа и вставляет их на вторую страницу. Эта операция осуществляется с помощью класса GraphicsAbsorber, который позволяет извлекать и манипулировать векторной графикой в PDF‑документах.

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов с первой страницы.
1. Приостановка обновлений на второй странице для повышения производительности.
1. Добавление извлеченных графических элементов на вторую страницу.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Метод 2: Добавление графики как коллекции

Следующий пример дублирует векторные графические элементы с первой страницы PDF‑документа и помещает их во вторую страницу. Это достигается с использованием класса GraphicsAbsorber, который облегчает извлечение и манипулирование векторной графикой в PDF‑документах.

1. Откройте PDF‑документ.
1. Инициализируйте GraphicsAbsorber.
1. Выберите целевую страницу.
1. Извлечение графических элементов с первой страницы.
1. Приостановка обновлений на второй странице для повышения производительности.
1. Добавление извлеченных графических элементов на вторую страницу.
1. Возобновление обновлений и применение изменений.
1. Сохранение обновленного документа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
