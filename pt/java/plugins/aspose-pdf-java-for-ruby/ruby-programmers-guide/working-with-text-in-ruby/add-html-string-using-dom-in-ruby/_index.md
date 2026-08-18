---
title: Adicionar String HTML usando DOM em Ruby
linktitle: Adicionar String HTML usando DOM em Ruby
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: Descubra como adicionar uma string HTML a um documento PDF usando a API DOM em Ruby com Aspose.PDF para geração de conteúdo dinâmico.
lastmod: "2026-06-09"
---
## Aspose.PDF - Adicionar HTML

Para adicionar uma string HTML em um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **AddHtml**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## Baixar código em execução

Baixe **Adicione HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
