---

title: Конвертация PDF в HTML на Python  
linktitle: Конвертация PDF в формат HTML  
type: docs  
weight: 50  
url: ru/python-java/convert-pdf-to-html/  
lastmod: "2021-11-01"  
description: Эта тема показывает, как конвертировать файл PDF в формат HTML с использованием библиотеки Aspose.PDF для Python Java.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.8  

---

## Обзор

Эта статья объясняет, как **конвертировать PDF в HTML с использованием Python**. Она охватывает следующие темы.

_Формат_: **HTML**
- [Конвертация PDF в HTML на Python](#python-pdf-to-html)
- [Python Конвертация PDF в HTML](#python-pdf-to-html)
- [Python Как конвертировать файл PDF в HTML](#python-pdf-to-html)


## Конвертация PDF в HTML

**Aspose.PDF для Python через .NET** предоставляет множество функций для конвертации различных форматов файлов в PDF-документы и конвертации PDF-файлов в различные выходные форматы.
 Этот документ обсуждает, как преобразовать PDF файл в <abbr title="HyperText Markup Language">HTML</abbr>. Вы можете использовать всего несколько строк кода на Python для преобразования PDF в HTML. Вам может понадобиться преобразовать PDF в HTML, если вы хотите создать веб-сайт или добавить контент на онлайн-форум. Один из способов преобразования PDF в HTML — это программное использование Python.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в HTML онлайн**

Aspose.PDF для Python представляет вам бесплатное онлайн-приложение ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в HTML с помощью бесплатного приложения](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Шаги: Преобразование PDF в HTML на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) вызовом метода [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# Открыть PDF документ
document = Api.Document(documentName)

# сохранить документ в формате HTML
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## Смотрите также

Эта статья также охватывает следующие темы. Код такой же, как указано выше.

_Формат_: **HTML**
- [Python PDF в HTML Код](#python-pdf-to-html)
- [Python PDF в HTML API](#python-pdf-to-html)
- [Python PDF в HTML Программно](#python-pdf-to-html)
- [Python PDF в HTML Библиотека](#python-pdf-to-html)
- [Python Сохранить PDF как HTML](#python-pdf-to-html)
- [Python Генерировать HTML из PDF](#python-pdf-to-html)
- [Python Создать HTML из PDF](#python-pdf-to-html)

- [Python Конвертер PDF в HTML](#python-pdf-to-html)