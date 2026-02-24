---
title: Работа с PDF-слоями с использованием Python
linktitle: Работа с PDF-слоями
type: docs
weight: 50
url: /ru/python-net/work-with-pdf-layers/
description: В этой статье объясняется, как заблокировать PDF-слой, извлечь элементы PDF-слоя, сгладить многослойный PDF и объединить все слои PDF в один.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как управлять, блокировать, извлекать, уплощать и объединять PDF-слои в Python
Abstract: В этой статье объясняется, как работать с PDF-слоями в Python, используя Aspose.PDF для .NET, включая блокировку слоёв, извлечение элементов слоя, уплощение многослойных PDF и объединение слоёв.
---

PDF-слои позволяют документу содержать несколько наборов содержимого, которые можно выборочно показывать или скрывать. Каждый слой может включать текст, изображения или графику, и пользователи могут включать их или отключать по необходимости. Слои особенно полезны в сложных документах, где контент необходимо организовать или разделить. Ниже приведены примеры, использующие API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и манипулирующие объектами [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) через коллекцию `layers` страницы.

## Блокировать PDF-слой

С помощью Aspose.PDF для Python через .NET вы можете открыть PDF (см. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), заблокировать конкретный [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) на первой [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), и сохранить документ с изменениями.

Доступные методы и свойства объекта [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/):

- `layer.lock()` – Блокирует слой. (see [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – Разблокирует слой. (see [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – Возвращает текущее состояние блокировки. (see [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Откройте PDF-документ (см. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Получите первую страницу, используя коллекцию [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) документа (см. [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Выберите [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) для блокировки из `page.layers`.
1. Вызовите `layer.lock()`, чтобы запретить пользователям переключать видимость слоя.
1. Сохраните обновлённый документ, используя [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Извлечь элементы PDF-слоя

Aspose.PDF позволяет извлекать каждый [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) из [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и сохранять его как отдельный PDF‑файл.

Чтобы создать новый PDF из слоя, можно использовать следующий фрагмент кода (коллекция `layers` доступна через `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

Вы также можете сохранять слои в поток:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Уплощение многослойного PDF

Уплощение делает [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) постоянным на странице, удаляя возможность переключения.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

Параметр `cleanup_content_stream` управляет тем, удаляются ли маркеры групп необязательного контента (OCG‑маркеры). Установка его в `False` ускоряет уплощение. См. метод [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) для получения деталей.

## Объединить все слои PDF в один

Вы можете объединить все слои (или отдельные) в один новый [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) (API объединения находится в объекте [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

Методы объекта [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/):

- `page.merge_layers(new_layer_name)` — объединяет все слои в новый слой с именем (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — объединяет, используя пользовательский идентификатор группы необязательного контента (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
