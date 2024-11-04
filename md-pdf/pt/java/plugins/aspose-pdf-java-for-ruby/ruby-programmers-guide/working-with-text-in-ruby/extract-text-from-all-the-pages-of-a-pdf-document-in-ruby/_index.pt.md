---
title: Extrair Texto de Todas as Páginas de um Documento PDF em Ruby
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extrair Texto de Todas as Páginas

Para extrair texto de todas as páginas de um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **ExtractTextFromAllPages**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento de destino

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# criar objeto TextAbsorber para extrair texto

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# aceitar o absorvedor para todas as páginas

pdf.getPages().accept(text_absorber)

# Para extrair texto de uma página específica do documento, precisamos especificar a página em particular usando seu índice contra o método accept(..).

# aceitar o absorvedor para uma página específica do PDF

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obter o texto extraído

extracted_text = text_absorber.getText()

# criar um escritor e abrir o arquivo

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# escrever uma linha de texto no arquivo

# tw.WriteLine(extractedText);

# fechar o fluxo

writer.close()

puts "Texto extraído com sucesso. Verifique o arquivo de saída."
```


## Download Running Code

Baixe **Extrair Texto de Todas as Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)