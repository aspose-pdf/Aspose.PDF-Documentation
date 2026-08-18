---
title: Obtenha metadados XMP de arquivo PDF em Ruby
linktitle: Obtenha metadados XMP de arquivo PDF em Ruby
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Acesse e manipule metadados XMP em documentos PDF usando Ruby com Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obtenha metadados XMP

Para obter metadados XMP de um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **GetXMPMetadata**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Baixar código em execução

Baixe **Obtenha metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
