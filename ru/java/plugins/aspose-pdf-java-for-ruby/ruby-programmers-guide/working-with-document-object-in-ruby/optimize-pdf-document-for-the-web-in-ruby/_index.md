---
title: Оптимизация PDF документа для веб в Ruby
type: docs
weight: 70
url: ru/java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Оптимизация PDF для Веб

Чтобы оптимизировать PDF-документ для веба с использованием **Aspose.PDF Java for Ruby**, просто вызовите метод **optimize_web** модуля **Optimize**.

Код на Ruby

```java

 def optimize_web()

    # Путь к директории документов.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Открыть PDF-документ.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Оптимизация для веб

    doc.optimize()

    #Сохранить выходной документ

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "PDF оптимизирован для веба, пожалуйста, проверьте выходной файл."

end
``` 

## Скачать Исполняемый Код

Скачайте **Optimize PDF for Web (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)