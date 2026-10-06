---
title: Extrair texto de todas as páginas de um documento PDF em Ruby
linktitle: Extrair texto de todas as páginas de um documento PDF em Ruby
type: docs
weight: 30
url: /pt/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: Entenda como extrair texto de todas as páginas de um documento PDF usando Ruby e Aspose.PDF, ideal para análise de conteúdo.
lastmod: "2026-10-06"
---
## Aspose.PDF - extrair texto de todas as páginas

Para extrair TextrFrom All the Pages Pdf document usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **ExtractTextFromAllPages**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## Baixar o exemplo de código

Baixar **Extrair Texto de Todas as Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
