---
title: Получить информацию о PDF файле в Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить информацию о PDF файле

Чтобы получить информацию о файле PDF документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetPdfFileInfo**.

Ruby Код

```java
# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Получить информацию о документе

doc_info = doc.getInfo()

# Показать информацию о документе

puts "Автор:-" + doc_info.getAuthor().to_s

puts "Дата создания:-" + doc_info.getCreationDate().to_string

puts "Ключевые слова:-" + doc_info.getKeywords().to_s

puts "Дата изменения:-" + doc_info.getModDate().to_string

puts "Тема:-" + doc_info.getSubject().to_s

puts "Заголовок:-" + doc_info.getTitle().to_s
```

## Скачать выполняемый код

Скачайте **Получить информацию о PDF файле (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)

```ruby
=begin
Этот пример показывает, как получить информацию о PDF-файле.
=end

require 'java'
require File.dirname(__FILE__) + '/asposepdfjava.jar'

include_class 'com.aspose.pdf.Document'

def get_pdf_file_info()
    # Загрузите существующий PDF-документ
    document = Document.new("input.pdf")

    # Получите информацию о документе
    info = document.get_info

    # Показать информацию
    puts "Заголовок: " + info.get_title
    puts "Автор: " + info.get_author
    puts "Субъект: " + info.get_subject
    puts "Ключевые слова: " + info.get_keywords
    puts "Создатель: " + info.get_creator
    puts "Производитель: " + info.get_producer
    puts "Дата создания: " + info.get_creation_date.to_s
    puts "Дата модификации: " + info.get_mod_date.to_s
end
```

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)