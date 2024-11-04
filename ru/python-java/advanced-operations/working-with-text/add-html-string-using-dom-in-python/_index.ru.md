---
title: Добавление HTML строки с использованием DOM в Python
type: docs
weight: 10
url: /python-java/add-html-string-using-dom-in-python/
---

Чтобы добавить HTML строку в PDF документ с использованием **Aspose.PDF Java для Python**, просто вызовите модуль **AddHtml**.

```python

# Создать объект Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Таблица</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Установить информацию о полях
title.setMargin(margin)

# Добавить HTML фрагмент в коллекцию параграфов страницы
page.getParagraphs().add(title)

# Сохранить PDF файл
doc.save(self.dataDir + 'html.output.pdf')

print "HTML успешно добавлен"
```

**Скачать Исполняемый Код**

Скачать **Добавить HTML (Aspose.PDF)** с любого из перечисленных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)