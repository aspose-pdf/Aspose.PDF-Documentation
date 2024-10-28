---
title: Adicionar Texto a um arquivo PDF existente em Ruby
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar Texto

Para adicionar uma string de texto em um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **AddText**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto Document

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obter página específica

pdf_page = doc.getPages().get_Item(1)

# criar fragmento de texto

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# definir propriedades do texto

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# criar objeto TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# adicionar o fragmento de texto à página PDF

text_builder.appendText(text_fragment)

# Salvar arquivo PDF

doc.save(data_dir + "Text_Added.pdf")

puts "Texto adicionado com sucesso"
```


## Download Running Code

Baixe **Add Text (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)