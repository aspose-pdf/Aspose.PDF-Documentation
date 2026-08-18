---
title: Оптимизация PDF-документа для Интернета в Ruby
linktitle: Оптимизация PDF-документа для Интернета в Ruby
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: Оптимизируйте PDF-файлы для более быстрой доставки через Интернет и уменьшения размера файлов с помощью Aspose.PDF в Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF — Оптимизация PDF для Интернета

Чтобы оптимизировать PDF-документ для Интернета с помощью **Aspose.PDF Java for Ruby**, просто вызовите метод **optimize_web** модуля **Optimize**.

Рубиновый код

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## Загрузите рабочий код

Загрузите **Оптимизацию PDF для Интернета (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
