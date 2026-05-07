---
title: Обновить ссылки PDF в Python
linktitle: Обновить ссылки
type: docs
weight: 20
url: /ru/python-net/update-links/
description: Узнайте, как обновить внешний вид и назначения ссылок PDF в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как обновить ссылки в PDF
Abstract: Руководство Aspose.PDF for Python via .NET по обновлению ссылок проводит разработчиков через процесс изменения поведения гиперссылок внутри PDF‑документов с использованием Python. Оно объясняет, как изменить назначения ссылок, чтобы они указывали на конкретные страницы, внешние веб‑сайты или даже другие PDF‑файлы. Документация также охватывает, как настроить внешний вид аннотаций ссылок, включая цвет текста, и предоставляет практические примеры кода для каждого сценария. Если вы исправляете устаревшие URL‑адреса или улучшаете навигацию, этот ресурс предлагает понятный и эффективный подход к программному управлению ссылками.
---

## Update LinkAnnotation Text Color

В этом примере показано, как обнаружить все аннотации ссылок на первой странице PDF с помощью Aspose.PDF for Python, а затем выделить текст рядом с каждой ссылкой, изменив цвет его шрифта на красный. Для поиска и изменения близлежащего текста используется TextFragmentAbsorber с слегка расширенной областью вокруг каждого прямоугольника ссылки.

Это может быть использовано для:

- Визуальная маркировка ссылок в документе
- Повышение доступности за счёт выделения связанного контента
- Предварительная обработка PDF‑файлов перед просмотром или экспортом

Для каждой из этих ссылочных аннотаций скрипт получает её прямоугольную границу и слегка расширяет эту область, чтобы включить соседний текст, позволяя более широкую визуальную идентификацию. Затем он применяет TextFragmentAbsorber к этому расширенному участку, чтобы извлечь любые находящиеся внутри фрагменты текста. Полученные фрагменты модифицируются путем изменения их цвета шрифта на красный, эффективно отмечая окружающий текст для выделения и обзора. После применения всех этих обновлений модифицированный документ сохраняется по пути вывода, сохраняя подсвеченные аннотации и их связанный текст.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Обновить границу

Скрипт ориентируется на первую страницу Document и фильтрует все аннотации, выбирая только те, которые имеют тип LINK — они обычно представляют интерактивные элементы, такие как гиперссылки или триггеры навигации. Для каждой из этих link annotations код приводит их к типу LinkAnnotation и обновляет их свойство color до красного, визуально выделяя их, чтобы они отличались от другого контента. После того как все link annotations были изменены, обновлённый Document сохраняется в указанное место вывода, сохраняя новое оформление.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Обновить веб‑назначение

Как только пути настроены, оригинальный документ загружается с использованием библиотеки Aspose.PDF, делая его содержание доступным для модификации. Затем скрипт фокусируется на первой странице документа, отфильтровывая все аннотации и выбирая только те, которые являются ссылками, обычно представляющими кликабельные области или гиперссылки. Чтобы избежать ошибок типов и обеспечить безопасную обработку, каждая аннотация проверяется с помощью is_assignable и затем приводится к соответствующему типу LinkAnnotation. Если ссылка связана с GoToURIAction, что означает указание на веб‑адрес, скрипт обновляет этот URI, перенаправляя пользователей на "https://www.aspose.com". Наконец, после применения всех желаемых изменений, изменённый документ сохраняется по указанному пути вывода.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Связанные темы ссылок

- [Работа с PDF-ссылками в Python](/pdf/ru/python-net/links/)
- [Создайте PDF-ссылки в Python](/pdf/ru/python-net/create-links/)
- [Извлечь ссылки PDF в Python](/pdf/ru/python-net/extract-links/)