---
title: Повернуть страницы PDF в Python
linktitle: Поворот страниц PDF
type: docs
weight: 110
url: /python-net/rotate-pages/
description: Узнайте, как вращать страницы PDF и менять ориентацию страниц в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как вращать страницы в PDF с помощью Python
Abstract: В этой статье представлено руководство о том, как программно обновлять или менять ориентацию страниц в существующем PDF‑файле с использованием Python. С помощью Aspose.PDF for Python via .NET пользователи могут легко переключаться между альбомной и книжной ориентацией, регулируя свойства MediaBox страницы. В статье включён фрагмент кода на Python, демонстрирующий, как проходить по страницам PDF‑документа, изменять размеры и позиции их MediaBox и при необходимости корректировать CropBox. Кроме того, объясняется, как установить угол поворота страниц с помощью метода ‘rotate’, чтобы достичь нужной ориентации. Процесс завершается сохранением обновлённого PDF‑файла.
---

Эта тема описывает, как программно обновлять или менять ориентацию страниц в существующем PDF‑файле с помощью Python.

Используйте эту страницу, когда нужно переключать страницы между портретной и альбомной ориентацией или применять углы поворота к существующему PDF‑контенту.

## Изменить ориентацию страницы

Эта функция вращает каждую страницу PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) на 90 градусов по часовой стрелке с помощью Aspose.PDF for Python.
Это полезно для исправления проблем с ориентацией страниц, например сканированных документов, расположенных боком. Исходный PDF остаётся неизменным, а повернутая версия сохраняется как новый файл.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Изменить размер страницы PDF в Python](/pdf/ru/python-net/change-page-size/)
- [Обрезать страницы PDF в Python](/pdf/ru/python-net/crop-pages/)
- [Получать и устанавливать свойства страниц PDF в Python](/pdf/ru/python-net/get-and-set-page-properties/)