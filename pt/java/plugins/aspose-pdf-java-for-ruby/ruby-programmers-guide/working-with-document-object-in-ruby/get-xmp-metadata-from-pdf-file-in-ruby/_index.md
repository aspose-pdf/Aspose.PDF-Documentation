---
title: Obter Metadados XMP de Arquivo PDF em Ruby
type: docs
weight: 60
url: /pt/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Metadados XMP

Para obter Metadados XMP de um documento Pdf usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **GetXMPMetadata**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obter propriedades

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Baixar Código em Execução

Baixe **Obter Metadados XMP (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)