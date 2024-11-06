---
title: Добавить HTML строку с использованием DOM в Ruby
type: docs
weight: 10
url: ru/java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление HTML

Чтобы добавить HTML строку в PDF документ, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **AddHtml**.

Ruby Код

```java
# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Создание объекта Document

doc = Rjb::import('com.aspose.pdf.Document').new

# Добавление страницы в коллекцию страниц PDF файла

page = doc.getPages().add()

# Создание HtmlFragment с HTML содержимым

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Таблица</i></b></fontsize>")

# Установка MarginInfo для деталей полей

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Установка информации о полях

title.setMargin(margin)

# Добавление HTML фрагмента в коллекцию параграфов страницы

page.getParagraphs().add(title)

# Сохранение PDF файла

doc.save(data_dir + "html.output.pdf")

puts "HTML добавлен успешно"
```


## Загрузка Исполняемого Кода

Скачайте **Add HTML (Aspose.PDF)** с любого из нижеупомянутых социальных кодинг-сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)