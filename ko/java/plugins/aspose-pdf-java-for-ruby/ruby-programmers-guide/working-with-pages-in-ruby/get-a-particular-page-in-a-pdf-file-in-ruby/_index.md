---
title: Ruby에서 PDF 파일의 특정 페이지 가져오기
linktitle: Ruby에서 PDF 파일의 특정 페이지 가져오기
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Ruby 및 Aspose.PDF를 사용하여 PDF 문서의 개별 페이지에 액세스하고 조작합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 가져오기



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 특정 페이지를 얻으려면 **GetPage** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **Get Page(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
