---
title: Adicionar String HTML usando DOM em Ruby
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar HTML

Para adicionar uma string HTML em um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **AddHtml**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto Document

doc = Rjb::import('com.aspose.pdf.Document').new

# Adicionar uma página à coleção de páginas do arquivo PDF

page = doc.getPages().add()

# Instanciar HtmlFragment com conteúdo HTML

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# definir MarginInfo para detalhes de margem

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Definir informações de margem

title.setMargin(margin)

# Adicionar Fragmento HTML à coleção de parágrafos da página

page.getParagraphs().add(title)

# Salvar arquivo PDF

doc.save(data_dir + "html.output.pdf")

puts "HTML adicionado com sucesso"
```


## Download Running Code

Baixe **Adicionar HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)