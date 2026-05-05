---
title: Работа с действиями PDF в Python
linktitle: Действия
type: docs
weight: 20
url: /ru/python-net/actions/
description: Узнайте, как добавлять, обновлять и удалять действия документов, страниц и форм в PDF‑файлах с использованием Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Добавьте действия документов, страниц и форм в PDF‑файлы с помощью Python.
Abstract: В этой статье рассматривается, как работать с действиями в PDF‑документах с использованием библиотеки Aspose.PDF, охватывая взаимодействия на уровне документа, страницы и формы. Действия PDF — это предопределённые или настраиваемые триггеры, которые реагируют на события пользователя, обеспечивая навигацию, выполнение JavaScript, воспроизведение мультимедиа, отправку форм и многое другое. Руководство показывает, как добавлять, настраивать и удалять действия, например открывать URL‑адреса при событиях документа, создавать навигацию или эффекты масштабирования, специфичные для страниц, добавлять интерактивные кнопки для печати и навигации, динамически скрывать элементы формы и отправлять данные формы на веб‑конечные точки. С помощью подробных примеров кода на Python читатели узнают, как улучшить интерактивность PDF, оптимизировать рабочие процессы и интегрировать PDF с внешними системами, учитывая совместимость с просмотрщиками.
---

Действия в PDF — это предопределённые задачи, которые активируются взаимодействием пользователя или событиями документа. Их можно использовать для:

- Перейдите к определённой странице или внешнему файлу
- Откройте веб‑ссылку
- Воспроизвести мультимедийный контент
- Запустить JavaScript
- Отправить или сбросить форму
- Показать/скрыть поля
- Изменить уровень масштабирования или режим просмотра

Почти все действия используют встроенные параметры, но некоторые можно настроить. Например — действия JavaScript.

## Добавить действия запуска PDF

Добавьте действия запуска на основе JavaScript в PDF‑документ с помощью Python и Aspose.PDF. Он назначает действия ключевым событиям документа, таким как открытие, сохранение и печать, позволяя автоматически запускать URL‑адреса, когда эти события происходят в поддерживаемых PDF‑просмотрщиках.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## Удаление действий из PDF Document

Чтобы очистить (или удалить) действия, просто установите обработчик в `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## Добавление действий к странице в PDF-документе

Для страниц предоставляются аналогичные триггеры: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## Действия в AcroForms

### Использование навигационных действий

Стандарт PDF предусматривает определённый набор именованных действий. Значение таких действий определяется их именем.
В следующем коде мы будем использовать действия для навигации.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

Этот код добавляет кнопки навигации на каждую страницу PDF‑документа, упрощая пользователям перемещение между страницами. Он начинается с определения полных путей к файлам ввода и вывода с помощью вспомогательного метода. Список button_config определяет четыре типа навигационных кнопок — First Page, Previous Page, Next Page и Last Page — их горизонтальные позиции, предопределённые навигационные действия, которые они вызывают, и лямбда‑функцию, определяющую, должна ли каждая кнопка быть только для чтения на данной странице (например, кнопки «First Page» и «Previous Page» только для чтения на первой странице).

Затем код загружает PDF и перебирает каждую страницу. Для каждой страницы он проходит по конфигурациям кнопок, создавая прямоугольную область для каждой кнопки и инстанцируя ButtonField в этом месте. Каждой кнопке присваивается имя, её статус только для чтения устанавливается в зависимости от текущей страницы, а действие при клике назначается соответствующему навигационному действию. Затем кнопка добавляется в поля формы PDF.

После того как все кнопки добавлены ко всем страницам, изменённый документ сохраняется. Если в процессе возникают какие‑либо ошибки, они перехватываются и выводятся. Такой подход гарантирует, что каждая страница имеет одинаковый набор элементов управления навигацией, улучшая удобство использования многостраничных PDF. Одной из тонкостей является использование лямбда‑функции is_readonly_fn для отключения кнопок навигации, когда они не имеют смысла (например, "Next Page" на последней странице), что помогает избежать путаницы у пользователя.

### Использование действий печати

При работе с PDF‑формами часто возникает необходимость печатать такие PDF‑документы. Это действие можно выполнить с помощью PDF‑ридера, но иногда удобнее сделать это напрямую из документа, используя специальную кнопку.

На самом деле, это ещё один пример того, как использовать именованные действия. Мы будем использовать `PredefinedAction.FILE_PRINT` (имитируя использование пункта меню File->Print), но вы также можете использовать `PredefinedAction.PRINT` или `PredefinedAction.PRINT_DIALOG`, в зависимости от ваших собственных целей.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

Этот фрагмент кода демонстрирует, как добавить кнопку "Print" на первую страницу PDF‑документа. Он начинается с загрузки PDF из указанного пути входного файла и выбора первой страницы (document.pages[1]).

Для позиции и размера кнопки на странице определяется прямоугольная область. Затем в этой области создаётся объект ButtonField, ему присваивается имя «printButton», а значение отображаемого текста устанавливается как «Print». Кнопка настроена так, чтобы при её нажатии (точнее, при отпускании кнопки мыши) запускалось предопределённое действие «Print File», вызывающее у PDF‑просмотрщика диалог печати.

Чтобы улучшить внешний вид кнопки, создаётся рамка, которая назначается кнопке, ширина которой устанавливается равной 1 единице. Затем кнопка добавляется к полям формы PDF на первой странице. В конце изменённый документ сохраняется по пути выходного файла. Такой подход предоставляет пользователям удобный способ печати документа непосредственно из PDF. Обратите внимание, что эффективность этой функции зависит от поддержки PDF‑просмотрщиком интерактивных полей формы и предопределённых действий.

### Использование действия Hide

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

Этот фрагмент кода добавляет кнопку на первую страницу PDF, которая при щелчке скрывает все поля‑чекбоксы в документе. Он начинается с определения полных путей к входному и выходному файлам с помощью вспомогательного метода. PDF загружается, и все поля‑чекбоксы собираются путем фильтрации полей формы на предмет экземпляров `ap.CheckboxField`.

Для нового положения кнопки у верхней части страницы определяется прямоугольная область. В этом месте создаётся ButtonField с именем “HideButton” и меткой “Hide Checkboxes”. Кнопка настроена так, чтобы при её нажатии (при отпускании кнопки мыши) запускался HideAction, который скрывает все собранные флажки.

Затем кнопка добавляется в поля формы на первой странице, а изменённый PDF сохраняется в выходной файл. Если во время этого процесса возникают ошибки, они перехватываются и выводятся. Эта функция предоставляет пользователям возможность быстро скрыть все флажки в PDF, что может быть полезно для настройки внешнего вида документа или рабочего процесса.

### Применение действия отправки

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

Эта функция добавляет кнопку "Submit" на первую страницу PDF-формы, позволяя пользователям отправлять данные формы на указанный веб‑конечный пункт. Она начинается с построения полных путей к входному и выходному PDF‑файлам, затем загружает входной PDF, используя библиотеку Aspose.PDF.

A `SubmitFormAction` создаётся, чтобы определить поведение при нажатии кнопки. URL действия устанавливается с помощью a `FileSpecification` указывающий на http://localhost:3000/submit, что означает, что данные формы будут отправлены на этот URL. Свойство flags объединяет `EXPORT_FORMAT` и `SUBMIT_COORDINATES`, обеспечивая экспорт данных формы в стандартном формате и включение координат клика по кнопке в отправку.

Для позиции и размера кнопки на странице определяется прямоугольная область. ButtonField создаётся в этом месте на первой странице, ему задаётся имя "SubmitButton", а его отображаемое значение устанавливается как "Submit". Действие отправки назначается событию отпускания мыши кнопки, поэтому действие срабатывает, когда пользователь нажимает кнопку.

Наконец, кнопка добавлена к полям формы на первой странице, и изменённый PDF сохраняется в выходной файл. Если во время этого процесса возникают какие‑либо ошибки, они перехватываются и выводятся. Этот подход предоставляет удобный для пользователя способ для PDF‑пользователей отправлять данные формы напрямую на конечную точку сервера.

## Связанные темы навигации

- [Навигация и взаимодействие с PDF с помощью Python](/pdf/ru/python-net/navigation-and-interaction/)
- [Работа с закладками в PDF с использованием Python](/pdf/ru/python-net/bookmarks/)
- [Работа со ссылками в PDF с помощью Python](/pdf/ru/python-net/links/)
