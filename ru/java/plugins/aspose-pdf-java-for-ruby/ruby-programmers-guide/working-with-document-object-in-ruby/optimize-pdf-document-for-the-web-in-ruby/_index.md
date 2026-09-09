---
title: Оптимизация PDF‑документа для веба на Ruby
linktitle: Оптимизация PDF‑документа для веба на Ruby
type: docs
weight: 70
url: /ru/java/optimize-pdf-document-for-the-web-in-ruby/
description: Оптимизируйте PDF‑файлы для более быстрой доставки в веб и уменьшения размера файла с помощью Aspose.PDF на Ruby.
lastmod: "2026-08-19"
---
## Aspose.PDF — Оптимизация PDF для веба

Чтобы оптимизировать PDF‑документ для веба с помощью **Aspose.PDF Java for Ruby**, просто вызовите метод **optimize_web** модуля **Optimize**.

Код Ruby

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

## Скачайте исполняемый код

СкачатьВ **Оптимизировать PDF для Web (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)


