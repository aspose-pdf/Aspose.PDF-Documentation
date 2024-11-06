---
title: Converter PDF para formato DOC ou DOCX em Ruby
type: docs
weight: 30
url: pt/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para DOC ou DOCX

Para converter um documento PDF para o formato DOC ou DOCX usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **PdfToDoc**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Salvar o arquivo de saída concatenado (o documento alvo)

pdf.save(data_dir + "output.doc")

puts "Documento foi convertido com sucesso"
```

## Baixar Código em Execução

Baixe **Converter PDF para DOC ou DOCX (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)