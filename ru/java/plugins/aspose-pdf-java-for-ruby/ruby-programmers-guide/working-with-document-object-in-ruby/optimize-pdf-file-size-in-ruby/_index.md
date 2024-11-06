---
title: Оптимизация размера PDF-файла в Ruby
type: docs
weight: 80
url: ru/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Оптимизация размера PDF-файла

Чтобы оптимизировать размер PDF-документа с использованием **Aspose.PDF Java для Ruby**, вызовите метод **optimize_filesize** модуля **Optimize**.

Код на Ruby

```java

 def optimize_filesize()

    # Путь к директории с документами.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Открыть PDF-документ.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Оптимизировать размер файла, удаляя неиспользуемые объекты

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # Сохранить выходной документ

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "Оптимизирован размер PDF, пожалуйста, проверьте выходной файл."

end 
```


## Скачать выполняемый код

Download **Оптимизация размера PDF файла (Aspose.PDF)** с любого из нижеупомянутых сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)