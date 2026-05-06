---
title: Извлечение маркированного контента из PDF на Python
linktitle: Извлечь маркированный контент
type: docs
weight: 20
url: /ru/python-net/extract-tagged-content-from-tagged-pdfs/
description: Узнайте, как извлечь маркированный контент PDF в Python с помощью Aspose.PDF for Python via .NET, включая доступ к маркированному контенту, корневой структуре и элементам дочерней структуры.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

В этой статье вы узнаете, как извлечь маркированный контент из PDF‑документов с помощью Python.

Используйте эти примеры, когда вам нужно проверить Tagged PDF, прочитать дерево логической структуры или убедиться, что Structure Elements созданы правильно для рабочих процессов по обеспечению доступности.

## Получение содержимого Tagged PDF

Чтобы получить содержимое PDF Document с Tagged Text, Aspose.PDF предлагает [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) свойство [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.

Создайте продвинутый, полностью помеченный PDF Document со структурированным и иерархическим Table of Contents (TOC):

1. Создайте новый объект Document.
1. Обратитесь к свойству tagged_content.
1. Установите заголовок документа, используя 'set_title()'.
1. Установите язык документа, используя 'set_language()'.
1. Сохраните документ.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Получение корневой структуры

Tagged PDFs содержат логическое дерево структуры, которое определяет семантическую структуру документа. StructTreeRoot представляет корень этого логического дерева, в то время как RootElement предоставляет интерфейс для взаимодействия с элементом верхнего уровня структуры документа.

Следующий фрагмент кода показывает, как получить корневую структуру Tagged PDF Document:

1. Создайте новый документ Tagged PDF.
1. Получите доступ к тегированному содержимому и задайте метаданные.
1. Получите доступ к StructTreeRoot и RootElement.
1. Сохраните тегированный PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Доступ к дочерним элементам

Tagged PDFs содержат логическое дерево структуры, определяющее семантическую иерархию документа (заголовки, абзацы, формы, списки и т.д.). Доступ к этим структурным элементам и их изменение позволяют вам:

- Проверьте метаданные, такие как title, language, actual_text, и свойства, связанные с доступностью
- Обновите свойства для улучшения доступности или локализации
- Программно изменить логическую структуру документа для соответствия требованиям PDF/UA

 Следующий фрагмент кода показывает, как получить доступ к дочерним элементам Tagged PDF Document:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Связанные темы Tagged PDF

- [Создать Tagged PDF](/pdf/ru/python-net/create-tagged-pdf/) чтобы создать доступные помеченные документы перед проверкой их структуры.
- [Настройка свойств Structure Elements](/pdf/ru/python-net/setting-structure-elements-properties/) обновить семантические свойства после извлечения элементов структуры.
- [Работа с таблицами в Tagged PDF](/pdf/ru/python-net/working-with-table-in-tagged-pdfs/) для рабочих процессов доступности тегированных таблиц.