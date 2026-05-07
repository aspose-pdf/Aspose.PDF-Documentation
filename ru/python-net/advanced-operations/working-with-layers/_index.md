---
title: Работа с PDF-слоями с помощью Python
linktitle: Работа с PDF-слоями
type: docs
weight: 50
url: /ru/python-net/working-with-pdf-layers/
description: Узнайте, как добавлять, блокировать, извлекать, уплощать и объединять слои PDF в Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управляйте слоями PDF с помощью Python.
Abstract: В этой статье объясняется, как работать с PDF layers (Optional Content Groups), используя Aspose.PDF for Python via .NET. Узнайте, как добавлять слои, заблокировать видимость слоев, извлекать содержимое слоя, уплощать слоистое содержимое и объединять слои в один.
---

Слои PDF, также называемые опциональными группами содержимого (OCG), позволяют организовывать контент в отдельные визуальные группы, которые можно показывать или скрывать в совместимых PDF‑просмотрщиках. В Aspose.PDF операции с уровнями построены вокруг [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

С Aspose.PDF for Python via .NET вы можете:

- Добавьте несколько слоёв на страницу.
- Блокируйте и разблокировать слои, чтобы контролировать поведение видимости.
- Извлеките слои в отдельные файлы или потоки.
- Сведите многослойное содержимое в страницу.
- Объедините несколько слоёв в один слой.

## Добавить слои в PDF

Этот пример создает PDF с тремя уровнями. Он использует [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), добавляет a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), и добавляет [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) объекты к этой странице.

1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и добавьте a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создайте и добавьте красный слой.
1. Создайте и добавьте зеленый слой.
1. Создайте и добавьте синий слой.
1. Сохраните PDF‑документ.

Полученный PDF будет содержать три отдельных слоя: красную линию, зеленую линию и синюю линию. Каждый из них можно включать и выключать в PDF‑просмотрщиках, поддерживающих многослойный контент.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## Заблокировать слой PDF

В этом примере открывается PDF, блокируется конкретный слой на первой странице и сохраняется обновлённый файл.

Блокировка слоя предотвращает изменение пользователями состояния видимости этого слоя в поддерживаемых PDF‑просмотрщиках. Слои доступны из страницы и управляются через коллекцию слоёв страницы.

Доступные методы и свойства:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) блокирует слой.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) разблокирует слой.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) возвращает текущее состояние блокировки.

1. Откройте PDF-документ.
1. Получите доступ к первой странице PDF.
1. Проверьте, есть ли у страницы слои.
1. Получите первый слой и заблокируйте его.
1. Сохраните обновлённый PDF.

Если PDF содержит слои, первый слой будет заблокирован, обеспечивая невозможность изменения его состояния видимости пользователем. Если слои не найдены, вместо этого выводится сообщение.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Извлечь элементы слоя PDF

В этом примере используется библиотека Aspose.PDF for Python via .NET для извлечения отдельных слоёв с первой страницы PDF‑документа и сохранения каждого слоя в отдельный PDF‑файл с помощью [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Чтобы создать новый PDF из слоя, можно использовать следующий фрагмент кода:

1. Загрузите PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Получите доступ к слоям на странице 1 через [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Проверьте, существуют ли слои.
1. Переберите слои и сохраните каждый из них.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

Можно извлечь элементы слоя PDF и сохранить их в новый поток файла PDF:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Уплощить многослойный PDF

Этот скрипт использует Aspose.PDF for Python via .NET для уплощения всех слоёв на первой странице PDF‑документа. Уплощение объединяет визуальное содержимое каждого слоя в один единый слой, что упрощает печать, совместное использование или архивирование без потери визуального качества или данных, специфичных для слоёв. Операция выполняется с [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Загрузите PDF-документ.
1. Доступ к слоям на странице 1.
1. Проверьте, существуют ли слои.
1. Сведите каждый слой с помощью `layer.flatten(True)`.
1. Сохраните измененный документ.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Объединить все слои в PDF в один

Этот фрагмент кода использует Aspose.PDF для объединения всех слоёв на первой странице PDF в один единый слой с пользовательским именем, используя [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Загрузите PDF-документ.
1. Получите доступ к странице 1 и извлеките её слои.
1. Проверьте, существуют ли слои.
1. Определите новое имя слоя.
1. Объедините слои в один.
1. Сохраните документ.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Связанные темы слоя

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Добавить страницы PDF в Python](/pdf/ru/python-net/add-pages/)
