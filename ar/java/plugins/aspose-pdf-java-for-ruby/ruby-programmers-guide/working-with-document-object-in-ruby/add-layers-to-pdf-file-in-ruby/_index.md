---
title: إضافة طبقات إلى ملف PDF في روبي
linktitle: إضافة طبقات إلى ملف PDF في روبي
type: docs
weight: 20
url: /java/add-layers-to-pdf-file-in-ruby/
description: تعرف على كيفية إضافة طبقات إلى ملف PDF في Ruby باستخدام Aspose.PDF لتحسين بنية المستند والتحكم في الرؤية.
lastmod: "2026-06-09"
---
## Aspose.PDF - إضافة طبقات

<ins> لإضافة طبقات في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **AddLayers**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

doc = Rjb::import('com.aspose.pdf.Document').new

page = doc.getPages().add()

operator = Rjb::import('com.aspose.pdf.Operator')

layer = Rjb::import('com.aspose.pdf.Layer').new("oc1", "Red Line")

layer.getContents().add(operator.SetRGBColorStroke(1, 0, 0))

layer.getContents().add(operator.MoveTo(500, 700))

layer.getContents().add(operator.LineTo(400, 700))

layer.getContents().add(operator.Stroke())

page.setLayers(Rjb::import('java.util.ArrayList').new)

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc2", "Green Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 1, 0))

layer.getContents().add(operator.MoveTo(500, 750))

layer.getContents().add(operator.LineTo(400, 750))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc3", "Blue Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 0, 1))

layer.getContents().add(operator.MoveTo(500, 800))

layer.getContents().add(operator.LineTo(400, 800))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

# Save PDF Document

doc.save(data_dir + "Layers-Added.pdf")

puts "Added Layers Successfully, please check the output file."
```

## تحميل كود التشغيل

تنزيلВ **إضافة طبقات (Aspose.PDF)**В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)
