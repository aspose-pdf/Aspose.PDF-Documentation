---
title: Obter uma Página Específica em um Arquivo PDF em Ruby
type: docs
weight: 30
url: pt/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Página

Para obter uma Página Específica em um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **GetPage**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obter a página no índice específico da Coleção de Páginas

pdf_page = pdf.getPages().get_Item(1)

# criar um novo objeto Documento

new_document = Rjb::import('com.aspose.pdf.Document').new

# adicionar página à coleção de páginas do novo objeto de documento

new_document.getPages().add(pdf_page)

# salvar o arquivo PDF recém-gerado

new_document.save(data_dir + "output.pdf")

puts "Processo concluído com sucesso!"
```

## Baixar Código em Execução

Baixe **Get Page (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)