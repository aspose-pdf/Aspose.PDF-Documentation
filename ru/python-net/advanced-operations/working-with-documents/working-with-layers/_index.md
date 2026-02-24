---
title: Работа с PDF‑слоями с помощью Python
linktitle: Работа с PDF‑слоями
type: docs
weight: 50
url: /ru/python-net/working-with-pdf-layers/
description: Следующее задание объясняет, как заблокировать слой PDF, извлечь элементы слоёв PDF, сплющить многослойный PDF и объединить все слои в PDF в один.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление PDF‑слоями
Abstract: Это руководство предоставляет всесторонний обзор управления и манипулирования PDF‑слоями с помощью библиотеки Aspose.PDF for Python via .NET. PDF‑слои, также известные как группы дополнительного содержания (OCG), позволяют организовывать содержимое в отдельные визуальные компоненты, которые можно включать и отключать.
---

PDF‑слои — мощный способ гибко организовать и представить содержимое внутри одного PDF‑файла, позволяя пользователям показывать или скрывать разные части в зависимости от их потребностей.

С **Aspose.PDF for Python via .NET** вы можете:

- Блокировать/разблокировать слои для управления их видимостью.
- Извлекать слои в отдельные файлы или потоки.
- Сплющивать слои, делая их постоянными.
- Объединять слои в единый слой.

## Добавление слоёв в PDF

В этом примере показано, как создать и добавить несколько слоёв в PDF‑документ с помощью Aspose.PDF for Python via .NET. Каждый слой содержит отдельное графическое содержимое, например цветные линии, которые можно включать или отключать в PDF‑просмотрщиках, поддерживающих слои.

1. Создать новый PDF‑документ и добавить страницу.
1. Создать и добавить красный слой.
1. Создать и добавить зелёный слой.
1. Создать и добавить синий слой.
1. Сохранить PDF‑документ.

Полученный PDF будет содержать три отдельных слоя: красную линию, зелёную линию и синюю линию. Каждый из них можно включать или отключать в PDF‑просмотрщиках, поддерживающих слоистое содержимое.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Блокировка PDF‑слоя

С помощью Aspose.PDF for Python via .NET вы можете открыть PDF, заблокировать определённый слой на первой странице и сохранить документ с изменениями.

В этом примере показано, как заблокировать слой (Optional Content Group, OCG) в PDF‑документе с помощью Aspose.PDF for Python via .NET. Блокировка не позволяет пользователям изменять видимость слоя в PDF‑просмотрщике, обеспечивая, что содержимое всегда остаётся видимым (или скрытым) в соответствии с определениями документа.

Доступные методы и свойства:

- layer.lock() – Блокирует слой.
- layer.unlock() – Разблокирует слой.
- layer.locked – Возвращает текущее состояние блокировки.

1. Открыть PDF‑документ.
1. Получить доступ к первой странице PDF.
1. Проверить, есть ли слои на странице.
1. Получить первый слой и заблокировать его.
1. Сохранить обновлённый PDF.

Если PDF содержит слои, первый слой будет заблокирован, гарантируя, что его состояние видимости нельзя изменить пользователем. Если слои не найдены, будет выведено сообщение.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Извлечение элементов PDF‑слоя

В этом примере используется библиотека Aspose.PDF for Python via .NET для извлечения отдельных слоёв с первой страницы PDF‑документа и сохранения каждого слоя в отдельный PDF‑файл.

Для создания нового PDF из слоя можно использовать следующий фрагмент кода:

1. Загрузить PDF‑документ. Входной PDF загружается в объект Aspose.PDF.Document.
1. Получить доступ к слоям на странице 1. Скрипт извлекает все слои с первой страницы, используя document.pages[1].layers.
1. Проверить наличие слоёв. Если слои не найдены, выводится сообщение и функция завершается.
1. Итерация и сохранение каждого слоя.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

Можно извлечь элементы PDF‑слоя и сохранить их в новый поток PDF‑файла:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Сплющивание многослойного PDF

Этот скрипт использует Aspose.PDF for Python via .NET для сплющивания всех слоёв на первой странице PDF‑документа. Сплющивание объединяет визуальное содержимое каждого слоя в один единый слой, упрощая печать, обмен или архивирование без потери визуального качества или данных, специфичных для слоёв.

1. Загрузить PDF‑документ. Входной PDF загружается в объект Aspose.PDF.Document.
1. Доступ к слоям на странице 1. Скрипт получает все слои с первой страницы, используя document.pages[1].layers.
1. Проверка наличия слоев. Если слои не найдены, выводится сообщение, и функция завершается.
1. Свести каждый слой. Каждый слой сворачивается с помощью layer.flatten(True), что объединяет его содержимое со страницей.
1. Сохранить изменённый документ.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Объединить все слои внутри PDF в один

Этот фрагмент кода использует Aspose.PDF для объединения всех слоев на первой странице PDF в один унифицированный слой с пользовательским именем.

1. Загрузить PDF‑документ. PDF загружается в объект Aspose.PDF.Document.
1. Доступ к странице и её слоям. Выбирается первая страница, и её слои извлекаются.
1. Проверка наличия слоев. Если слоёв нет, выводится сообщение, и процесс завершается.
1. Определить новое имя слоя. Для результата объединения задаётся новое имя слоя ("LayerNew").
1. Объединить слои. Если указан идентификатор группы дополнительного содержимого, он используется при объединении. В противном случае слои объединяются, используя только новое имя.
1. Сохранить документ

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
