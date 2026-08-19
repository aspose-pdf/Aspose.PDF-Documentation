---
title: Извлечение текста со всех страниц PDF‑документа на Ruby
linktitle: Извлечение текста со всех страниц PDF‑документа на Ruby
type: docs
weight: 30
url: /ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: Поймите, как извлекать текст со всех страниц PDF‑документа с помощью Ruby и Aspose.PDF, идеально для анализа содержимого.
lastmod: "2026-08-19"
---
## Aspose.PDF — Извлечение текста со всех страниц

Чтобы извлечь TextrFrom All the Pages Pdf document с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **ExtractTextFromAllPages**.

Ruby‑код

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

## Скачать выполняемый код

Скачать **Extract Text From All the Pages (Aspose.PDF)** из любых из перечисленных ниже социальных сайтов для программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)

