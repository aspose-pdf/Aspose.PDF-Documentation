---
title: Insira uma Página Vazia no Final do Arquivo PDF em Ruby
type: docs
weight: 60
url: /pt/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insira uma Página Vazia no Final do Arquivo PDF

Para inserir uma página vazia no final do documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **InsertEmptyPageAtEndOfFile**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insira uma página vazia em um PDF

pdf.getPages().add()

# Salve o arquivo de saída concatenado (o documento alvo)

pdf.save(data_dir+ "output.pdf")

puts "Página vazia adicionada com sucesso!"
```

## Baixar Código em Execução

Baixe **Insira uma Página Vazia no Final do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)