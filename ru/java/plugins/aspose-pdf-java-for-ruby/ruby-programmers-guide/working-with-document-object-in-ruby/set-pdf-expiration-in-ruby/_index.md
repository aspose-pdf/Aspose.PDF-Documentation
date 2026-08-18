---
title: Установить срок действия PDF в Ruby
linktitle: Установить срок действия PDF в Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: Реализуйте даты истечения срока действия в PDF-файлах, используя Aspose.PDF для Ruby для документов, чувствительных ко времени.
lastmod: "2026-06-09"
---
## Aspose.PDF — установка срока действия PDF

Чтобы установить срок действия PDF-документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **SetExpiration**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## Загрузите рабочий код

Загрузите **Установите срок действия PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
