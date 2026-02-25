---
title: Добавить изображение в PDF с помощью Python
linktitle: Добавить изображение
type: docs
weight: 10
url: /ru/python-net/add-image-to-existing-pdf-file/
description: В этом разделе описывается, как добавить изображение в существующий PDF-файл с помощью библиотеки Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Как добавить изображения в PDF с помощью Python
Abstract: В этой статье предоставляются рекомендации по добавлению изображений в существующие PDF‑файлы с помощью Python и библиотеки Aspose.PDF. Описываются два метода достижения этой цели. Первый метод использует класс `Document` из Aspose.PDF, где пользователь загружает PDF, указывает номер страницы и использует метод `add_image` класса `Page` для размещения изображения. Затем документ сохраняется с помощью метода `save()`. Второй метод использует класс `PdfFileMend` из пространства имён Aspose.PDF.Facades, который предлагает более простой интерфейс. Здесь вызывается метод `add_image()`, чтобы добавить изображение на указанную страницу и координаты, после чего сохраняется обновлённый PDF и закрывается объект `PdfFileMend`. Для обоих методов представлены фрагменты кода, демонстрирующие процесс.
---

## Добавление изображения в существующий PDF‑файл

Этот пример демонстрирует, как вставить изображение в определённую позицию на странице PDF с использованием Aspose.PDF для Python через .NET.

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Выберите целевую страницу '(document.pages[1]' — первая страница.
1. Используйте 'page.add_image()', чтобы разместить изображение:
- Путь к файлу изображения.
- Объект 'Rectangle', определяющий координаты изображения (left=20, bottom=730, right=120, top=830).
1. Сохраните обновлённый PDF.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## Добавление изображения с помощью операторов

Следующий фрагмент кода демонстрирует низкоуровневый подход к добавлению изображения на страницу PDF путем ручной работы с операторами PDF, а не с помощью высокоуровневых вспомогательных методов.

Шаги:

1. Создайте новый пустой 'Document'.
1. Добавьте страницу и задайте её размер (842 × 595 — альбомная A4).
1. Получите доступ к ресурсам изображений страницы (page.resources.images).
1. Загрузите файл изображения в поток и добавьте его в ресурсы.
- Метод возвращает 'image_id'.
- Ново‑добавленный объект изображения извлекается из ресурсов.
1. Определите прямоугольник, сохраняющий пропорции изображения:
1. Сформируйте последовательность операторов:
- 'GSave()' — Сохранить текущее графическое состояние.
- 'ConcatenateMatrix(matrix)' — Применить преобразование (масштабировать и центрировать изображение вертикально на странице).
- 'Do(image_id)' — Отрисовать изображение.
- 'GRestore()' — Восстановить графическое состояние.
1. Добавьте последовательность операторов в 'page.contents'.
1. Сохраните полученный PDF.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## Добавление изображения с альтернативным текстом

Этот пример показывает, как добавить изображение на страницу PDF и присвоить альтернативный текст (alt text) для соответствия требованиям доступности (например, PDF/UA).

1. Создайте новый 'Document' и добавьте страницу (842 × 595, альбомная A4).
1. Разместите изображение на странице с помощью 'page.add_image()' и прямоугольника, охватывающего всю страницу.
1. Получите доступ к ресурсам изображений страницы ('page.resources.images').
1. Определите строку альтернативного текста (например, 'Alternative text for image').
1. Получите первый объект изображения из ресурсов ('x_image = resources_images[1]').
1. Используйте 'try_set_alternative_text(alt_text, page)', чтобы назначить alt‑текст изображению.
1. Сохраните полученный PDF.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
