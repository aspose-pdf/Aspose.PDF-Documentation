---
title: Установить срок действия PDF в Ruby
linktitle: Установить срок действия PDF в Ruby
type: docs
weight: 110
url: /ru/java/set-pdf-expiration-in-ruby/
description: Реализуйте даты истечения срока действия в PDF, используя Aspose.PDF for Ruby, для документов с ограниченным сроком действия.
lastmod: "2026-08-19"
---
## Aspose.PDF - Установить срок действия PDF

Чтобы установить срок действия PDF‑документа, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **SetExpiration**.

Код Ruby

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

## Скачайте работающий код

Скачать **Set PDF Expiration (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)


