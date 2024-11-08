---
title: Converter HTML para Formato PDF em Ruby
type: docs
weight: 10
url: /pt/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter HTML para Formato PDF

Para converter HTML para formato PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **HtmlToPdf**.

Código Ruby

```java

# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Carregar arquivo HTML

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Salvar o arquivo de saída concatenado (o documento de destino)

pdf.save(data_dir + "html.pdf")

puts "Documento foi convertido com sucesso"
```

## Baixar Código em Execução

Baixe **Converter HTML para Formato PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)