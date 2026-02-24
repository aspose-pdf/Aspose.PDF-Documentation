---
title: Создание ссылок в PDF‑файле с помощью Python
linktitle: Создать ссылки
type: docs
weight: 10
url: /ru/python-net/create-links/
description: В этом разделе объясняется, как создавать ссылки в вашем PDF‑документе с помощью Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как создавать ссылки в PDF
Abstract: Руководство Aspose.PDF для Python через .NET по созданию ссылок предоставляет разработчикам практические инструкции по добавлению интерактивных гиперссылок в PDF‑документы с помощью Python. Оно охватывает создание различных типов ссылок, включая открывающие внешние приложения, переходящие к определённым страницам в том же документе или открывающие другие PDF‑файлы. Документация объясняет, как использовать объекты LinkAnnotation, определять кликабельные области с помощью Rectangle и назначать действия, такие как LaunchAction или GoToRemoteAction. С чёткими примерами кода и пошаговым руководством этот ресурс помогает разработчикам улучшить навигацию и интерактивность PDF в их Python‑приложениях.
---

## Ссылки в PDF‑документах

Согласно спецификации PDF 1.7 (ISO 32000-1:2008), **Link annotation** может инициировать несколько типов действий, определяющих, что происходит при активации аннотации. Ниже приведены основные поддерживаемые действия:

1. **GoTo** – Переход к месту назначения в том же документе.
1. **GoToR** – Переход к месту назначения в другом PDF‑файле (удалённый переход).
1. **URI** – Открывает унифицированный идентификатор ресурса, обычно веб‑ссылку.
1. **Launch** – Запускает приложение или открывает файл (зависит от платформы и часто ограничено из соображений безопасности).
1. **Named** – Выполняет предопределённое действие, например переход к следующей странице или печать документа.
1. **JavaScript** – Выполняет встроенный JavaScript‑код (используется с осторожностью из‑за соображений безопасности).
1. **SubmitForm** – Отправляет данные формы по указанному URL.
1. **ResetForm** – Сбрасывает поля формы к их значениям по умолчанию.
1. **ImportData** – Импортирует данные в документ из внешнего файла.

Добавляя в документ ссылку на приложение, можно создать ссылки на приложения из документа. Это полезно, когда вы хотите, чтобы читатели совершили определённое действие в конкретный момент учебного пособия или создать документ с расширенными возможностями.

Чтобы создать ссылку на приложение с помощью 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Создание ссылки на PDF‑документ в PDF‑файле

### Использование GoToRemoteAction

Этот фрагмент кода демонстрирует, как добавить аннотацию ссылки на определённую страницу PDF‑документа с использованием библиотеки Python для работы с PDF.

1. Откройте PDF‑документ
1. Выберите вторую страницу документа (индекс 1)
1. Создайте аннотацию ссылки:
1. Разместите её в координатах (10, 580, 120, 600)
1. Окрасьте её в зелёный цвет
1. Ссылается на 'sample.pdf' на его первой странице
1. Добавьте аннотацию ссылки на страницу
1. Сохраните изменённый документ по указанному пути вывода

Чтобы создать ссылку на PDF‑документ с использованием 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Использование GoToAction

Этот код демонстрирует, как добавить аннотацию ссылки на определённую страницу PDF‑документа с использованием Aspose.PDF for Python. Ссылка отображается в виде зелёного прямоугольника с пунктирной рамкой и позволяет пользователю переходить к другой странице внутри того же PDF. Чтобы создать ссылку на PDF‑документ с помощью 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Применение GoToURIAction

Следующий пример демонстрирует, как добавить аннотацию ссылки в PDF‑документ с использованием Aspose.PDF for Python. Ссылка отображается как зелёная кликабельная область на первой странице, и при нажатии открывает документацию Aspose.PDF для Python в веб‑браузере через GoToURIAction.

Эта функция полезна для встраивания полезных внешних ссылок, документации или ссылок поддержки непосредственно в ваши PDF‑файлы.

1. Загрузите PDF‑документ. Откройте существующий PDF‑файл с помощью ap.Document.
1. Получите доступ к первой странице. Используйте document.pages[1] для доступа к первой странице (Aspose использует индексацию, начинающуюся с 1).
1. Создайте аннотацию ссылки. Создайте объект LinkAnnotation и укажите кликабельную прямоугольную область с помощью ap.Rectangle.
1. Установите внешний вид аннотации. Задайте цвет аннотации зелёным, используя link.color = ap.Color.green.
1. Назначьте действие URI. Используйте GoToURIAction, чтобы связать аннотацию с внешним URL.
1. Добавьте аннотацию на страницу. Добавьте настроенную аннотацию ссылки в коллекцию аннотаций первой страницы.
1. Сохраните изменённый документ. Сохраните обновлённый PDF‑документ по указанному пути вывода.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

