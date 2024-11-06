---
title: Объединение PDF файлов в Ruby
type: docs
weight: 10
url: ru/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Объединение PDF файлов

Чтобы объединить PDF файлы с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **ConcatenatePdfFiles**.

Код на Ruby

```java
# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Открыть исходный документ

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Добавить страницы исходного документа в целевой документ

pdf1.getPages().add(pdf2.getPages())

# Сохранить объединенный выходной файл (целевой документ)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "Новый документ сохранен, пожалуйста, проверьте выходной файл"
```

## Скачать исполняемый код

Скачать **Объединение PDF файлов (Aspose.PDF)** с любого из нижеупомянутых социальных кодировочных сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)

```ruby
# Этот скрипт демонстрирует, как объединить несколько PDF файлов в один.
require 'asposepdfjava'

module Asposepdfjava
  module ConcatenatePdfFiles
    def initialize()
      # Создать объект класса AsposePDF
      pdfEditor = Rjb::import('com.aspose.pdf.facades.PdfFileEditor')

      # Путь к файлам PDF, которые нужно объединить
      inputFile1 = "input1.pdf"
      inputFile2 = "input2.pdf"
      outputFile = "output.pdf"

      # Объединить файлы PDF
      pdfEditor.concatenate(inputFile1, inputFile2, outputFile)

      puts "Файлы успешно объединены в #{outputFile}"
    end
  end
end