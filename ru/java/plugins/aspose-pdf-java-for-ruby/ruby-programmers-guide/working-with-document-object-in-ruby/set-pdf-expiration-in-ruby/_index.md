---
title: Установить срок действия PDF в Ruby
type: docs
weight: 110
url: ru/java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Установить срок действия PDF

Чтобы установить срок действия PDF-документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **SetExpiration**.

Ruby Код

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF-документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('Файл устарел. Вам нужен новый.');")

doc.setOpenAction(javascript)

# сохранить обновленный документ с новой информацией

doc.save(data_dir + "set_expiration.pdf")

puts "Обновите информацию документа, пожалуйста, проверьте выходной файл."
```


## Скачать Исполняемый Код

Скачайте **Установить истечение срока действия PDF (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов для разработчиков:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)