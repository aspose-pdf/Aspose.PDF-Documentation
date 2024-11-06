---
title: Добавление слоев в PDF файл на Ruby
type: docs
weight: 20
url: ru/java/add-layers-to-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление слоев

<ins> Чтобы добавить слои в PDF документ с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **AddLayers**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

doc = Rjb::import('com.aspose.pdf.Document').new

page = doc.getPages().add()

operator = Rjb::import('com.aspose.pdf.Operator')

layer = Rjb::import('com.aspose.pdf.Layer').new("oc1", "Красная линия")

layer.getContents().add(operator.SetRGBColorStroke(1, 0, 0))

layer.getContents().add(operator.MoveTo(500, 700))

layer.getContents().add(operator.LineTo(400, 700))

layer.getContents().add(operator.Stroke())

page.setLayers(Rjb::import('java.util.ArrayList').new)

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc2", "Зеленая линия")

layer.getContents().add(operator.SetRGBColorStroke(0, 1, 0))

layer.getContents().add(operator.MoveTo(500, 750))

layer.getContents().add(operator.LineTo(400, 750))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc3", "Синяя линия")

layer.getContents().add(operator.SetRGBColorStroke(0, 0, 1))

layer.getContents().add(operator.MoveTo(500, 800))

layer.getContents().add(operator.LineTo(400, 800))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

# Сохранить PDF документ

doc.save(data_dir + "Layers-Added.pdf")

puts "Слои успешно добавлены, пожалуйста, проверьте выходной файл."
```


## Скачать Исполняемый Код

Скачайте **Add Layers (Aspose.PDF)** с любого из перечисленных ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)