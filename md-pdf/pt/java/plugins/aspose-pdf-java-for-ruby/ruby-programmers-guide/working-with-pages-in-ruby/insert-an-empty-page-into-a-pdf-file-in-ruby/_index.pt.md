---
title: Inserir uma Página Vazia em um Arquivo PDF em Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Inserir uma Página Vazia

Para inserir uma página vazia em um documento Pdf usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **InsertEmptyPage**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insira uma página vazia em um PDF

pdf.getPages().insert(1)

# Salve o arquivo de saída concatenado (o documento alvo)

pdf.save(data_dir+ "output.pdf")

puts "Página vazia adicionada com sucesso!"
```

## Baixar Código em Execução

Baixe **Inserir uma Página Vazia (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)