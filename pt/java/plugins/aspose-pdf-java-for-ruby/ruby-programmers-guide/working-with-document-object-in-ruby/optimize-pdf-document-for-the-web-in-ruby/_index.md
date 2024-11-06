---
title: Otimizar Documento PDF para a Web em Ruby
type: docs
weight: 70
url: pt/java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Otimizar PDF para Web

Para otimizar um documento PDF para a web usando **Aspose.PDF Java for Ruby**, simplesmente invoque o método **optimize_web** do módulo **Optimize**.

Código Ruby

```java

 def optimize_web()

    # O caminho para o diretório de documentos.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Abra um documento pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Otimizar para web

    doc.optimize()

    # Salvar documento de saída

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "PDF otimizado para a Web, por favor verifique o arquivo de saída."

end
``` 

## Baixar Código em Execução

Baixe **Optimize PDF for Web (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)