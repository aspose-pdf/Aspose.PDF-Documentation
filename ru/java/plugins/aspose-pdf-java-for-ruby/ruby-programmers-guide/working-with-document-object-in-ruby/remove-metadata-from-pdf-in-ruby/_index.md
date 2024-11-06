---
title: Удаление метаданных из PDF на Ruby
type: docs
weight: 90
url: ru/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Удаление метаданных

Чтобы удалить метаданные из PDF документа с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **RemoveMetadata**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# сохранить обновленный документ с новой информацией

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Метаданные успешно удалены, пожалуйста, проверьте выходной файл."
```

## Скачать работающий код

Скачать **Remove Metadata (Aspose.PDF)** можно с любого из нижеупомянутых сайтов для совместной разработки:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)