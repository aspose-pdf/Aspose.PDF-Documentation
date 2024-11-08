---
title: Добавление текста в существующий PDF файл на Ruby
type: docs
weight: 20
url: /ru/java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление текста

Чтобы добавить текстовую строку в PDF документ, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **AddText**.

Код на Ruby

```java

# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Создание объекта Document

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# получить конкретную страницу

pdf_page = doc.getPages().get_Item(1)

# создать текстовый фрагмент

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# установить свойства текста

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# создать объект TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# добавить текстовый фрагмент на страницу PDF

text_builder.appendText(text_fragment)

# Сохранить PDF файл

doc.save(data_dir + "Text_Added.pdf")

puts "Текст успешно добавлен"
```


## Скачать Исполняемый Код

Скачать **Add Text (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)