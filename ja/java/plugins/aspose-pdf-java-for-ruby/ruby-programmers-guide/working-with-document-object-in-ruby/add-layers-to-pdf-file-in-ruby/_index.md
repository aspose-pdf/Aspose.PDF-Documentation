---
title: "Ruby での PDF ファイルへのレイヤーの追加"
linktitle: "Ruby での PDF ファイルへのレイヤーの追加"
type: docs
weight: 20
url: /ja/java/add-layers-to-pdf-file-in-ruby/
description: "Aspose.PDF を使用して、Ruby で PDF ファイルにレイヤーを追加する方法を学び、文書構造と表示制御を向上させましょう。"
lastmod: "2026-10-06"
---
## Aspose.PDF でのレイヤーの追加

<ins> Pdfドキュメントにレイヤーを追加するには、**Aspose.PDF Java for Ruby** を使用して、単に **AddLayers** モジュールを呼び出します。

Ruby コード

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

## 実行中のコードのダウンロード

ダウンロード **Add Layers (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行ってください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)
