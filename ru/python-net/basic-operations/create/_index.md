---
title: Создать PDF документ программно
linktitle: Создать PDF
type: docs
weight: 10
url: /ru/python-net/create-document/
description: Эта страница описывает, как создать PDF документ с нуля с помощью библиотеки Aspose.PDF for Python via .NET.
lastmod: "2026-05-07"
TechArticle: true 
AlternativeHeadline: Создание PDF файлов с помощью Aspose.PDF for Python
Abstract: В разработке программного обеспечения генерация PDF файлов программным способом является распространённой потребностью, особенно при создании отчётов и других документов. Написание пользовательского кода для этой задачи может быть неэффективным и занимать много времени. Вместо этого разработчики могут использовать **Aspose.PDF for Python via .NET**, надёжное решение для создания PDF файлов с помощью Python. Процесс включает создание объекта `Document`, добавление объекта `Page` в коллекцию `Pages` документа, вставку `TextFragment` в коллекцию `paragraphs` страницы и последующее сохранение документа. Пример фрагмента кода на Python демонстрирует эти шаги, показывая простоту генерации PDF файлов с использованием Aspose.PDF.
---

Для разработчиков существует множество сценариев, когда становится необходимо программно генерировать PDF‑файлы. Вам может потребоваться программно создавать PDF‑отчёты и другие PDF‑файлы в вашем программном обеспечении. Писать собственный код и функции с нуля довольно долго и неэффективно. Чтобы создать PDF‑файл с помощью Python, существует лучшее решение — **Aspose.PDF for Python via .NET**.

## Как создать PDF‑файл с использованием Python

Чтобы создать PDF‑файл с помощью Python, можно использовать следующие шаги.

1. Создайте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. Добавьте [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объект к [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) коллекция объекта Document
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) к [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) коллекция страницы
1. Сохраните полученный PDF документ

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
