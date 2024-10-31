---
title: Пример Hello World на Python
linktitle: Пример Hello World
type: docs
weight: 20
url: /python-net/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF-документ с текстом Hello World, используя Aspose.PDF для Python через .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Пример "Hello World" показывает самый простой синтаксис и самую простую программу на любом языке программирования. Разработчики знакомятся с основным синтаксисом языка программирования, изучая, как вывести "Hello World" на экран устройства. Поэтому мы традиционно начнем наше знакомство с нашей библиотекой с него.

В этой статье мы создаем PDF-документ, содержащий текст "Hello World!". После установки **Aspose.PDF для Python через .NET** в вашей среде, вы можете выполнить следующий пример кода, чтобы увидеть, как работает API Aspose.PDF.

Следующий фрагмент кода выполняет следующие шаги:

1. Создайте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Добавьте [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Добавьте TextFragment в коллекцию [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) полученный PDF-документ

Следующий фрагмент кода представляет собой программу "Hello World", демонстрирующую работу Aspose.PDF для Python через .NET API.

```python

    import aspose.pdf as ap

    # Инициализировать объект документа
    document = ap.Document()
    # Добавить страницу
    page = document.pages.add()
    # Инициализировать объект textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Добавить текстовый фрагмент на новую страницу
    page.paragraphs.add(text_fragment)
    # Сохранить обновленный PDF
    document.save("output.pdf")
```