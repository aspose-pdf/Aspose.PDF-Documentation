---
title: Создать ссылки PDF в Python
linktitle: Создать ссылки
type: docs
weight: 10
url: /ru/python-net/create-links/
description: Узнайте, как создавать внутренние, внешние и удалённые ссылки PDF в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как создавать ссылки в PDF
Abstract: Руководство Aspose.PDF for Python via .NET по созданию ссылок предоставляет разработчикам практические инструкции по добавлению интерактивных гиперссылок в PDF‑документы с использованием Python. Оно охватывает создание различных типов ссылок, включая те, которые запускают внешние приложения, переходят к определённым страницам внутри того же документа или открывают другие PDF‑файлы. Документация объясняет, как использовать объекты LinkAnnotation, определять кликабельные области с помощью Rectangle и назначать действия, такие как LaunchAction или GoToRemoteAction. С ясными примерами кода и пошаговым руководством этот ресурс помогает разработчикам улучшить навигацию и интерактивность PDF в их приложениях на Python.
---

## Ссылки в PDF‑документах

Согласно спецификации PDF 1.7 (ISO 32000-1:2008), **Link annotation** может инициировать несколько типов действий, определяющих, что происходит при активации аннотации. Ниже перечислены поддерживаемые основные действия:

1. **GoTo** – Переходит к месту назначения в том же документе.
1. **GoToR** – Переходит к месту назначения в другом PDF‑файле (удалённый переход).
1. **URI** – Открывает универсальный идентификатор ресурса, как правило, веб‑ссылку.
1. **Launch** – Запускает приложение или открывает файл (зависит от платформы и часто ограничено по соображениям безопасности).
1. **Named** – Выполняет предопределённое действие, например переход к следующей странице или печать документа.
1. **JavaScript** – Выполняет встроенный код JavaScript (используется с осторожностью из‑за проблем безопасности).
1. **SubmitForm** – Отправляет данные формы на указанный URL.
1. **ResetForm** – Сбрасывает поля формы до их значений по умолчанию.
1. **ImportData** – Импортирует данные в документ из внешнего файла.

Добавив ссылку на приложение в документ, можно создавать ссылки на приложения из документа. Это полезно, когда вы хотите, чтобы читатели выполнили определённое действие в конкретном месте руководства, например, или создали документ с расширенными возможностями.

Чтобы создать ссылку на приложение с 'LaunchAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## Создать ссылку на документ PDF в PDF‑файле

### Использование GoToRemoteAction

Этот фрагмент кода демонстрирует, как добавить аннотацию ссылки на конкретную страницу PDF‑документа с использованием библиотеки PDF для Python.

1. Откройте PDF‑документ
1. Выберите вторую страницу документа (индекс 1)
1. Создайте аннотацию ссылки:
1. Размещено в координатах (10, 580, 120, 600)
1. Окрашен в зеленый
1. Ссылается на 'sample.pdf' на первой странице
1. Добавьте аннотацию ссылки на страницу
1. Сохраните измененный документ по пути выходного файла

Чтобы создать ссылку на PDF‑документ, используя 'GoToRemoteAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Использование GoToAction

Этот код демонстрирует, как добавить аннотацию ссылки на конкретную страницу PDF‑документа с использованием Aspose.PDF for Python. Ссылка отображается в виде зеленого прямоугольника с пунктирной рамкой и позволяет пользователю переходить на другую страницу внутри того же PDF. Чтобы создать ссылку в PDF‑документе с использованием 'GoToAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Применение GoToURIAction

Следующий пример демонстрирует, как добавить аннотацию ссылки в PDF-документ с помощью Aspose.PDF for Python. Ссылка отображается как зеленая кликабельная область на первой странице, и при нажатии открывает документацию Aspose.PDF for Python в веб-браузере через GoToURIAction.

Эта функция полезна для встраивания полезных внешних ссылок, документации или ссылок на поддержку непосредственно в ваши PDF-файлы.

1. Загрузите PDF‑документ. Откройте существующий PDF‑файл, используя ap.Document.
1. Получите доступ к первой странице. Используйте document.pages[1] для доступа к первой странице (Aspose использует индексацию, начинающуюся с 1).
1. Создайте аннотацию ссылки. Создайте объект LinkAnnotation и укажите кликабельную прямоугольную область с помощью ap.Rectangle.
1. Установите внешний вид аннотации. Установить цвет аннотации на зеленый, используя link.color = ap.Color.green.
1. Назначьте действие URI. Использовать GoToURIAction, чтобы связать аннотацию с внешним URL.
1. Добавьте аннотацию на страницу. Добавить настроенную ссылочную аннотацию в коллекцию аннотаций первой страницы.
1. Сохраните измененный документ. Сохранить обновленный PDF‑документ по указанному пути вывода.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Связанные темы ссылок

- [Работа с PDF-ссылками в Python](/pdf/ru/python-net/links/)
- [Извлечь ссылки из PDF с помощью Python](/pdf/ru/python-net/extract-links/)
- [Обновить ссылки в PDF с помощью Python](/pdf/ru/python-net/update-links/)