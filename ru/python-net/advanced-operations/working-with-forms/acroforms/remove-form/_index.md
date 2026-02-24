---
title: Удалить формы из PDF на Python
linktitle: Удалить формы
type: docs
weight: 70
url: /ru/python-net/remove-form/
description: Удалить текст на основе подтипа/формы с помощью библиотеки Aspose.PDF для Python через .NET. Удалить все формы из PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить формы из PDF с помощью Aspose.PDF для Python через .NET
Abstract: В этом документе представлено два подхода на Python для удаления элементов форм из PDF‑файлов с использованием Aspose.PDF для Python через .NET. Первый метод демонстрирует, как очистить все объекты форм на конкретной странице, получив доступ к её словарю ресурсов и вызвав метод clear() у коллекции форм. Второй метод предоставляет более целенаправленное решение, перебирая аннотации форм, определяя формы‑печатающие машинки и избирательно удаляя их на основе их атрибутов. Оба метода завершаются сохранением обновлённого PDF в указанный путь вывода, предлагая гибкие варианты очистки форм и улучшения документов в автоматических рабочих процессах.
---

## Удалить все формы из PDF

Этот код удаляет все элементы форм с первой страницы PDF‑документа, а затем сохраняет изменённый документ в указанный путь вывода.

1. Загрузить PDF‑документ.
1. Доступ к ресурсам страницы.
1. Очистить объекты форм.
1. Сохранить обновлённый документ.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Удалить указанную форму

Следующий пример перебирает объекты форм на заданной странице PDF, определяет аннотации форм‑типперов, удаляет их и затем сохраняет обновлённый PDF с использованием Aspose.PDF для Python через .NET.

1. Загрузить PDF‑документ.
1. Доступ к формам страницы.
1. Перебрать формы.
1. Проверить наличие форм‑типперов.
1. Удалить найденную форму.
1. Сохранить обновлённый документ.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
