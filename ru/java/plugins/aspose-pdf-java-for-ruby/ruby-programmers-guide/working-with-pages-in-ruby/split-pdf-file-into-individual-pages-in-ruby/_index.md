---
title: Разделение PDF файла на отдельные страницы в Ruby
type: docs
weight: 80
url: /ru/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Разделение страниц

Чтобы разделить PDF документ на отдельные страницы с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **SplitAllPages**.

Код на Ruby

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Цикл по всем страницам

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# создать новый объект Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# получить страницу по определенному индексу из коллекции страниц

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# сохранить вновь созданный PDF файл

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Процесс разделения успешно завершен!"
```


## Скачать работающий код

Скачайте **Split Pages (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)