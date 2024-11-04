---
title: Atualizar Dimensões da Página em Ruby
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Atualizar Dimensões da Página

Para atualizar as dimensões da página usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **UpdatePageDimensions**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obter a coleção de páginas

page_collection = pdf.getPages()

# obter uma página específica

pdf_page = page_collection.get_Item(1)

# definir o tamanho da página como A4 (11.7 x 8.3 in) e no Aspose.PDF, 1 polegada = 72 pontos

# portanto, as dimensões do A4 em pontos serão (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# salvar o arquivo PDF recém-gerado

pdf.save(data_dir + "output.pdf")

puts "Dimensões atualizadas com sucesso!"
```

## Baixar Código em Execução

Baixe **Update Page Dimensions (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)

```ruby
# Este exemplo demonstra como atualizar as dimensões da página em um documento PDF
require 'java'
require 'asposepdfjava'

module Asposepdfjava
  module UpdatePageDimensions
    def initialize()
        # Carregar um documento PDF existente
        pdf_document = Rjb::import('com.aspose.pdf.Document').new("input.pdf")

        # Obter a página desejada
        page = pdf_document.getPages().get_Item(1)

        # Atualizar as dimensões da página
        page.setPageSize(300, 300)

        # Salvar o documento PDF atualizado
        pdf_document.save("output.pdf")
    end
  end
end