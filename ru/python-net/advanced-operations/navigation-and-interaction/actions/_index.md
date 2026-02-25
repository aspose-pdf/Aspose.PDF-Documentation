---
title: Работа с действиями в PDF‑документе
linktitle: Действия
type: docs
weight: 20
url: /ru/python-net/actions/
description: Изучите, как извлекать и управлять метаданными PDF, такими как автор и название, в Python с помощью Aspose.PDF.
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Работа с действиями в PDF‑документе с использованием Python
Abstract: В этой статье рассматривается работа с действиями в PDF‑документах с использованием библиотеки Aspose.PDF, охватывающая взаимодействия на уровне документа, страницы и формы. Действия PDF — это предопределённые или настраиваемые триггеры, реагирующие на пользовательские события, позволяющие выполнять навигацию, запуск JavaScript, воспроизведение мультимедиа, отправку форм и многое другое. Руководство демонстрирует, как добавлять, настраивать и удалять действия, такие как открытие URL при событиях документа, создание навигации или эффектов масштабирования на конкретных страницах, добавление интерактивных кнопок для печати и навигации, динамическое скрытие элементов формы и отправка данных формы на веб‑конечные точки. С помощью подробных примеров кода на Python читатели узнают, как улучшить интерактивность PDF, оптимизировать рабочие процессы и интегрировать PDF с внешними системами, учитывая совместимость с различными просмотрщиками.
---

Действия в PDF — это предопределённые задачи, которые запускаются при взаимодействии пользователя или событиях документа. Они могут использоваться для:

- Перейти к определённой странице или внешнему файлу
- Открыть веб‑ссылку
- Воспроизвести мультимедийный контент
- Выполнить JavaScript
- Отправить или сбросить форму
- Показать/скрыть поля
- Изменить уровень масштабирования или режим просмотра

Почти все действия используют встроенные параметры, но некоторые могут быть настроены. Например, действия JavaScript.

## Действия уровня документа

### Добавление действий в PDF‑документ

PDF‑документы поддерживают несколько действий уровня документа, включая код, который выполняется при открытии документа или в ответ на определённые события. Используйте свойство `open_action` для действий при открытии; остальные действия управляются в коллекции `actions`.

Рассмотрим, как использовать `open_action`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

В этом примере мы вызываем метод `launchURL` из объекта `app` и открываем веб‑сайт (для демонстрационных целей).

Другие действия могут быть добавлены тем же способом, но с небольшими изменениями:

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

Вы можете добавить действия для следующих событий: `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

Этот фрагмент кода демонстрирует, как прикрепить JavaScript‑действия к различным событиям уровня документа в PDF. Сначала он загружает существующий PDF‑документ из указанного пути входного файла. Свойство `document.open_action` устанавливается в JavaScript‑действие, которое открывает URL при открытии документа, заставляя просмотрщик PDF открыть `http://localhost:3000/open` в браузере пользователя.

Затем два дополнительных JavaScript‑действия назначаются событиям `before_saving` и `before_printing` документа. Эти действия срабатывают, когда пользователь пытается сохранить или распечатать документ, соответственно, каждый раз открывая в браузере разный URL (`/save` или `/print`). Это может быть полезно для отслеживания взаимодействий пользователей или интеграции с веб‑ориентированными рабочими процессами.

### Удаление действий из PDF‑документа

Чтобы очистить (или удалить) действия, просто установите обработчик в `None`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## Действия уровня страницы

### Добавление действий на страницу в PDF‑документе

Для страниц предоставляются аналогичные триггеры: `on_open`, `on_close`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

Мы добавляем два действия на эту страницу. Сначала создаётся действие "GoTo", которое срабатывает при открытии страницы. Это действие использует явное назначение, чтобы перейти к левому верхнему углу страницы с определённым уровнем масштабирования. Затем прикрепляется JavaScript‑действие, которое выполняется при закрытии страницы, заставляя просмотрщик PDF открыть определённый URL в браузере. В конце изменённый документ сохраняется по указанному пути вывода.

Тонкость, на которую следует обратить внимание, — это индексация страниц: использование неверного индекса может привести к неожиданному поведению или ошибкам. Кроме того, использование JavaScript‑действий в PDF может не поддерживаться всеми просмотрщиками PDF, поэтому эта функция может не работать везде.

### Удаление действий со страницы PDF

Используйте `remove_actions` для удаления действия со страницы.

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## Действия в AcroForms

### Использование действий навигации

Стандарт PDF предусматривает определённый набор именованных действий. Значение таких действий определяется их именем.
В следующем коде мы будем использовать действия для навигации.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

Этот код добавляет кнопки навигации на каждую страницу PDF‑документа, упрощая пользователям перемещение между страницами. Он начинается с определения полных путей к входному и выходному файлам с помощью вспомогательного метода. Список `button_config` описывает четыре типа навигационных кнопок — «Первая страница», «Предыдущая страница», «Следующая страница» и «Последняя страница» — вместе с их горизонтальными позициями, предопределёнными действиями навигации, которые они вызывают, и лямбда‑функцией, определяющей, должна ли каждая кнопка быть доступной только для чтения на данной странице (например, кнопки «Первая страница» и «Предыдущая страница» недоступны для редактирования на первой странице).

Затем код загружает PDF и проходит по каждой странице. Для каждой страницы он перебирает конфигурации кнопок, создавая прямоугольную область для каждой кнопки и создавая объект `ButtonField` в этом месте. Каждой кнопке присваивается имя, её статус только для чтения устанавливается в зависимости от текущей страницы, а действие по клику назначается соответствующему навигационному действию. После этого кнопка добавляется в поля формы PDF.

После того как все кнопки добавлены ко всем страницам, изменённый документ сохраняется. Если в процессе возникают ошибки, они перехватываются и выводятся. Такой подход гарантирует, что каждая страница имеет одинаковый набор навигационных элементов, улучшая удобство использования многостраничных PDF. Одним из нюансов является использование лямбда‑функции `is_readonly_fn` для отключения навигационных кнопок, когда их использование не имеет смысла (например, «Следующая страница» на последней странице), что помогает избежать путаницы у пользователей.

### Использование действий печати

При работе с PDF‑формами часто возникает необходимость печати таких PDF‑документов. Это действие можно выполнить с помощью PDF‑ридера, но иногда удобнее сделать это непосредственно из документа, используя специальную кнопку.

Фактически, это ещё один пример использования именованных действий. Мы будем использовать `PredefinedAction.FILE_PRINT` (симулируя пункт меню File→Print), но также можно использовать `PredefinedAction.PRINT` или `PredefinedAction.PRINT_DIALOG` в зависимости от ваших целей.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

Этот фрагмент кода демонстрирует, как добавить кнопку «Print» на первую страницу PDF‑документа. Он начинается с загрузки PDF из указанного входного пути файла и выбора первой страницы (document.pages[1]).

Для позиции и размера кнопки на странице определяется прямоугольная область. Затем создаётся ButtonField в этом месте, ему присваивается имя «printButton», а отображаемое значение устанавливается как «Print». Кнопка настроена так, чтобы при её нажатии (а именно при отпускании кнопки мыши) запускалось предопределённое действие «Print File», вызывая у просмотрщика PDF диалог печати.

Чтобы улучшить внешний вид кнопки, создаётся граница и назначается кнопке, ширина которой установлена в 1 единицу. Затем кнопка добавляется в поля формы PDF на первой странице. Наконец изменённый документ сохраняется по пути выходного файла. Этот подход предоставляет пользователям удобный способ печати документа напрямую из PDF. Обратите внимание, что эффективность этой функции зависит от поддержки просмотрщиком PDF интерактивных полей формы и предопределённых действий.

### Использование действия Hide

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

Этот фрагмент кода добавляет кнопку на первую страницу PDF, которая при нажатии скрывает все поля‑чекбоксы в документе. Он начинается с получения полного пути входного и выходного файлов с помощью вспомогательного метода. PDF загружается, и все поля‑чекбоксы собираются путём фильтрации полей формы для экземпляров `ap.CheckboxField`.

Для позиции новой кнопки в верхней части страницы определяется прямоугольная область. В этом месте создаётся ButtonField, названный «HideButton», с меткой «Hide Checkboxes». Кнопка настроена так, чтобы при её нажатии (при отпускании кнопки мыши) запускалось HideAction, которое скрывает все собранные чекбоксы.

Затем кнопка добавляется в поля формы на первой странице, и изменённый PDF сохраняется в выходной файл. Если во время этого процесса возникают ошибки, они перехватываются и выводятся. Эта функция предоставляет пользователям возможность быстро скрыть все чекбоксы в PDF, что может быть полезно для настройки внешнего вида документа или рабочего процесса.

### Применение действия Submit

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

Эта функция добавляет кнопку «Submit» на первую страницу PDF‑формы, позволяя пользователям отправлять данные формы на указанный веб‑конечный пункт. Она начинается с построения полных путей для входного и выходного PDF‑файлов, затем загружает входной PDF с помощью библиотеки Aspose.PDF.

Создаётся `SubmitFormAction`, определяющий поведение при нажатии кнопки. URL действия устанавливается с помощью `FileSpecification`, указывающего на http://localhost:3000/submit, что означает отправку данных формы по этому URL. Свойство flags комбинирует `EXPORT_FORMAT` и `SUBMIT_COORDINATES`, обеспечивая экспорт данных формы в стандартном формате и включение координат щелчка кнопки в отправку.

Для позиции и размера кнопки на странице определяется прямоугольная область. В этом месте на первой странице создаётся ButtonField, ему даётся имя «SubmitButton», а отображаемое значение устанавливается как «Submit». Действие отправки назначается событию отпускания мыши кнопки, поэтому действие срабатывает, когда пользователь нажимает кнопку.

Наконец кнопка добавляется в поля формы на первой странице, и изменённый PDF сохраняется в выходной файл. Если при этом возникают ошибки, они перехватываются и выводятся. Этот подход предоставляет пользователям PDF удобный способ отправлять данные формы напрямую на серверный конечный пункт.

