---
title: Obter contagem de páginas de PDF em Ruby
linktitle: Obter contagem de páginas de PDF em Ruby
type: docs
weight: 40
url: /pt/java/get-page-count-of-pdf-in-ruby/
description: Recupere o número total de páginas em um documento PDF programaticamente usando Ruby com Aspose.PDF.
lastmod: "2026-10-06"
---
## Aspose.PDF - obter contagem de páginas

Para obter a contagem de páginas de um documento Pdf usando **Aspose.PDF Java for Ruby**, simplesmente invoque o módulo **GetNumberOfPages**.

Código Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Baixar o exemplo de código

Baixar **Obter Contagem de Páginas (Aspose.PDF)** de qualquer dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
