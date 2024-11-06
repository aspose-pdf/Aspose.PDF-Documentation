---
title: Преобразование PDF в DOC или DOCX формат на Ruby
type: docs
weight: 30
url: ru/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование PDF в DOC или DOCX

Чтобы преобразовать PDF документ в DOC или DOCX формат, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToDoc**.

Код на Ruby

```java

# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Сохранить объединенный выходной файл (целевой документ)

pdf.save(data_dir + "output.doc")

puts "Документ был успешно преобразован"
```

## Скачать Рабочий Код

Скачайте **Преобразование PDF в DOC или DOCX (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)