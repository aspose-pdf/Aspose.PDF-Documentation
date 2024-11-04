---
title: Converter arquivo SVG para formato PDF em Ruby
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter SVG para PDF

Para converter arquivo SVG para formato PDF usando **Aspose.PDF Java for Ruby**, simplesmente invoque o módulo **SvgToPdf**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto LoadOption usando opção de carregamento SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Criar objeto de documento

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Salvar a saída no formato XLS

pdf.save(data_dir + "SVG.pdf")

puts "Documento foi convertido com sucesso"
```

## Baixar Código em Execução

Baixe **Converter SVG para PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)