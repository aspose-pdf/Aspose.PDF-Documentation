---
title: Ruby에서 PDF 문서의 모든 페이지에서 텍스트 추출
linktitle: Ruby에서 PDF 문서의 모든 페이지에서 텍스트 추출
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: 콘텐츠 분석에 이상적인 Ruby 및 Aspose.PDF를 사용하여 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 이해하세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 모든 페이지에서 텍스트 추출



**Aspose.PDF Java for Ruby**를 사용하여 TextrFrom 모든 페이지 PDF 문서를 추출하려면 **ExtractTextFromAllPages** 모듈을 호출하기만 하면 됩니다.



루비 코드


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

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **모든 페이지에서 텍스트 추출(Aspose.PDF)**을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
