---
title: Извлечение текста со всех страниц PDF-документа на Ruby
type: docs
weight: 30
url: /ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Извлечение текста со всех страниц

Чтобы извлечь текст со всех страниц PDF-документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **ExtractTextFromAllPages**.

Код на Ruby

```java
# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# создать объект TextAbsorber для извлечения текста

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# применить абсорбер ко всем страницам

pdf.getPages().accept(text_absorber)

# Чтобы извлечь текст с конкретной страницы документа, необходимо указать конкретную страницу, используя ее индекс в методе accept(..).

# применить абсорбер к конкретной странице PDF

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# получить извлеченный текст

extracted_text = text_absorber.getText()

# создать писателя и открыть файл

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# записать строку текста в файл

# tw.WriteLine(extractedText);

# закрыть поток

writer.close()

puts "Текст успешно извлечен. Проверьте выходной файл."
```


## Скачать Исполняемый Код

Скачайте **Извлечение Текста Со Всех Страниц (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)