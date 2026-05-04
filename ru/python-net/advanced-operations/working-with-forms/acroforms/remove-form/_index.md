---
title: Удалить формы из PDF в Python
linktitle: Удалить формы
type: docs
weight: 70
url: /python-net/remove-form/
description: Удалить объекты форм со страниц PDF, используя Aspose.PDF for Python via .NET, включая полную очистку и целевое удаление.
lastmod: "2026-04-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить формы из PDF с помощью Aspose.PDF for Python via .NET
Abstract: В этой статье представлены два подхода к удалению элементов форм из PDF‑документов с использованием Aspose.PDF for Python via .NET. Первый метод очищает все объекты форм на выбранной странице, тогда как второй метод удаляет только соответствующие ресурсы формы Typewriter. Эти примеры помогают при очистке форм, подготовке шаблонов и процессах нормализации документов.
---

## Удалить все формы со страницы

Этот код удаляет все объекты формы со страницы, указанной `page_num` и сохраняет обновлённый документ.

1. Загрузите PDF-документ.
1. Получить доступ к ресурсам страницы.
1. Очистить объекты формы.
1. Сохранить обновлённый документ.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Удалить конкретный тип формы

Следующий пример проходит по объектам форм на заданной странице PDF, определяет аннотации форм‑пишущих машинок, удаляет их и затем сохраняет обновлённый PDF, используя Aspose.PDF for Python via .NET.

1. Загрузите PDF-документ.
1. Получить доступ к формам страницы.
1. Итерировать формы.
1. Проверить наличие форм‑пишущих машинок.
1. Удалить соответствующую форму.
1. Сохранить обновлённый документ.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Связанные темы

- [Создать AcroForm](/pdf/ru/python-net/create-form/)
- [Заполнить AcroForm](/pdf/ru/python-net/fill-form/)
- [Изменение AcroForm](/pdf/ru/python-net/modifying-form/)
- [Размещение форм](/pdf/ru/python-net/posting-form/)
