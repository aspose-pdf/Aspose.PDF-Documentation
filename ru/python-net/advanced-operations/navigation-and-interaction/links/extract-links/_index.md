---
title: Извлечение ссылок PDF в Python
linktitle: Извлечь ссылки
type: docs
weight: 30
url: /ru/python-net/extract-links/
description: Узнайте, как извлекать аннотации ссылок и гиперссылки из PDF‑документов с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как извлечь ссылки из PDF
Abstract: Руководство Aspose.PDF for Python via .NET по извлечению ссылок объясняет, как программно получать аннотации гиперссылок из PDF‑документов с помощью Python. Документация включает практические примеры кода и подчёркивает, как эту функцию можно использовать для таких задач, как аудит ссылок, анализ навигации или создание интерактивных возможностей документа. Независимо от того, работаете ли вы с одностраничными PDF или обрабатываете большие партии, это руководство предлагает ясный и эффективный подход к извлечению гиперссылок.
---

## Извлечь ссылки из PDF‑файла

Этот пример демонстрирует, как перебрать все аннотации‑ссылки на первой странице PDF с использованием Aspose.PDF for Python. Он фильтрует аннотации, чтобы определить те, которые имеют тип LinkAnnotation, безопасно приводит их тип и затем выводит их индекс страницы и прямоугольную позицию на странице.

Это может использоваться для отладки, аналитики или автоматических обновлений существующих аннотаций‑ссылок в PDF.

1. Загрузите PDF‑документ. Используйте ap.Document(path_infile) для открытия файла.
1. Получите доступ к аннотациям первой страницы. Используйте document.pages[1].annotations для получения всех аннотаций.
1. Фильтруйте только типы LinkAnnotation. Проверьте поле annotation_type каждой аннотации.
1. Преобразуйте и обработайте LinkAnnotation. Используйте is_assignable() и cast() для безопасного доступа к свойствам LinkAnnotation.
1. Выведите детали аннотации. Выведите индекс страницы и прямоугольник (местоположение) каждой ссылки.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## Извлечь гиперссылки из PDF‑файла

Этот код демонстрирует, как извлечь все объекты LinkAnnotation с первой страницы PDF‑документа с использованием Aspose.PDF for Python, а затем определить те, которые содержат действие GoToURIAction. Для каждой такой ссылки он выводит номер страницы и целевой URI.

Это полезно для таких задач, как:

- Аудит внешних ссылок в PDF
- Извлечение URL‑адресов документации или поддержки
- Обнаружение битых или устаревших гиперссылок

1. Загрузите PDF‑документ. Откройте файл с помощью ap.Document.
1. Получите все аннотации ссылок с первой страницы. Отфильтруйте аннотации, оставив только те, у которых тип AnnotationType.LINK.
1. Проверьте тип и приведите к LinkAnnotation. Убедитесь, что каждая аннотация действительно является LinkAnnotation, прежде чем обращаться к её свойствам.
1. Проверьте тип действия ссылки. Отфильтруйте ссылки, использующие GoToURIAction (т.е. ссылки на веб‑URL).
1. Извлеките и выведите URI и индекс страницы. Используйте .uri для получения внешней ссылки и .page_index для контекста.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Связанные темы ссылок

- [Работа с PDF-ссылками в Python](/pdf/ru/python-net/links/)
- [Создайте PDF-ссылки в Python](/pdf/ru/python-net/create-links/)
- [Обновить ссылки в PDF с помощью Python](/pdf/ru/python-net/update-links/)