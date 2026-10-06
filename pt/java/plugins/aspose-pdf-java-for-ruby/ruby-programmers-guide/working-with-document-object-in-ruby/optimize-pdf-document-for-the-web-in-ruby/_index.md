---
title: Otimizar documento PDF para a Web em Ruby
linktitle: Otimizar documento PDF para a Web em Ruby
type: docs
weight: 70
url: /pt/java/optimize-pdf-document-for-the-web-in-ruby/
description: Simplifique PDFs para entrega na web mais rápida e redução do tamanho do arquivo usando Aspose.PDF em Ruby.
lastmod: "2026-10-06"
---
## Aspose.PDF - Otimizar PDF para Web

Para otimizar o documento PDF para a web usando **Aspose.PDF Java for Ruby**, basta invocar o método **optimize_web** do módulo В  **Optimize**.

Código Ruby

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```

## Baixar Código em Execução

DownloadВ **Otimizar PDF para Web (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
