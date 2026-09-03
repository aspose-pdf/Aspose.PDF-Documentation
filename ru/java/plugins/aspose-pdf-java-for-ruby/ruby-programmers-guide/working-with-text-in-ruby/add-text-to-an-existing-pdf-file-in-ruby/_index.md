---
title: Добавить текст в существующий PDF‑файл в Ruby
linktitle: Добавить текст в существующий PDF‑файл в Ruby
type: docs
weight: 20
url: /ru/java/add-text-to-an-existing-pdf-file-in-ruby/
description: Узнайте, как добавить текст в существующий PDF‑документ в Ruby с помощью Aspose.PDF, чтобы улучшить или обновить содержимое вашего PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF — Добавить текст

Чтобы добавить строку текста в PDF‑документ, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **AddText**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get particular page

pdf_page = doc.getPages().get_Item(1)

# create text fragment

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# set text properties

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# create TextBuilder object

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# append the text fragment to the PDF page

text_builder.appendText(text_fragment)

# Save PDF file

doc.save(data_dir + "Text_Added.pdf")

puts "Text added successfully"
```

## Скачайте работающий код

СкачатьВ **Add Text (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)


