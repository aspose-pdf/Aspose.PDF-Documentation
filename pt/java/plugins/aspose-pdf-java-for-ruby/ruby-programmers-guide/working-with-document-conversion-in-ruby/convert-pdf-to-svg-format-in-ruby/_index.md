---
title: Converter PDF para formato SVG em Ruby
type: docs
weight: 50
url: /pt/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para SVG

Para converter PDF para o formato SVG usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **PdfToSvg**.

Código Ruby

```java

# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instanciar um objeto de SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# não comprimir imagem SVG para arquivo Zip

save_options.CompressOutputToZipArchive = false

# Salvar a saída no formato XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "Documento foi convertido com sucesso"
```

## Baixar Código em Execução

Baixar **Converter PDF para Formato SVG (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)