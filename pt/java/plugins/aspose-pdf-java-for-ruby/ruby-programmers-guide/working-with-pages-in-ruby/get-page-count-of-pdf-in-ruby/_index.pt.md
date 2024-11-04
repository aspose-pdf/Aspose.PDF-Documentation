---
title: Obter Contagem de Páginas de PDF em Ruby
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Contagem de Páginas

Para obter a contagem de páginas de um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **GetNumberOfPages**.

Código Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Criar documento PDF

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Contagem de Páginas:" + page_count.to_s
```

## Baixar Código em Execução

Baixe **Obter Contagem de Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)