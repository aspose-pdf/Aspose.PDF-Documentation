---
title: Добавление HTML строки с использованием DOM в Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
keywords: html dom python, python html dom library
description: Объясняет, как добавить HTML строку в DOM с использованием Python с библиотекой формата файла PDF
---

## Добавление HTML строки в PDF DOM с использованием Python
Чтобы добавить HTML строку в Pdf документ с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **AddHtml**.

```python

# Создание объекта Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Таблица</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Установка информации о полях
title.setMargin(margin)

# Добавление HTML фрагмента в коллекцию абзацев страницы
page.getParagraphs().add(title)

# Сохранение PDF файла
doc.save(self.dataDir + 'html.output.pdf')

print "HTML добавлен успешно"
```

**Скачать работающий код**

Скачайте **Add HTML (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)