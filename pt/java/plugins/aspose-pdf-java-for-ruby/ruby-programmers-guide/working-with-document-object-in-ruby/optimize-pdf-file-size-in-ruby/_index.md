---
title: Otimizar Tamanho do Arquivo PDF em Ruby
type: docs
weight: 80
url: /pt/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Otimizar Tamanho do Arquivo PDF

Para otimizar o tamanho do arquivo de um documento PDF usando **Aspose.PDF Java for Ruby**, chame o método **optimize_filesize** do módulo **Optimize**.

Código Ruby

```java

 def optimize_filesize()

    # O caminho para o diretório dos documentos.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Abra um documento pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Otimize o tamanho do arquivo removendo objetos não utilizados

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # Salvar documento de saída

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "Tamanho do arquivo PDF otimizado, por favor verifique o arquivo de saída."

end 
```


## Baixar Código em Execução

Download **Otimizar Tamanho do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)