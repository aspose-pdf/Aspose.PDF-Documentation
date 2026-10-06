---
title: Converter arquivo SVG para formato PDF em Ruby
linktitle: Converter arquivo SVG para formato PDF em Ruby
type: docs
weight: 60
url: /pt/java/convert-svg-file-to-pdf-format-in-ruby/
description: Aprenda como converter arquivos SVG para o formato PDF em Ruby usando Aspose.PDF para transformação de documentos precisa e escalável.
lastmod: "2026-10-06"
---
## Aspose.PDF - Converter SVG para PDF

Para converter um arquivo SVG para o formato PDF usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **SvgToPdf**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## Baixar Código em Execução

DownloadВ **Converter SVG para PDF (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
