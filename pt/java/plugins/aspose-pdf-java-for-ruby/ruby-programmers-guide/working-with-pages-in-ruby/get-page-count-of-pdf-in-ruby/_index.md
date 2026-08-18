---
title: Obtenha a contagem de páginas do PDF em Ruby
linktitle: Obtenha a contagem de páginas do PDF em Ruby
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: Recupere o número total de páginas em um documento PDF programaticamente usando Ruby com Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obter contagem de páginas

Para obter a contagem de páginas do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **GetNumberOfPages**.

Código Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Baixar código em execução

Baixe **Obter contagem de páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
