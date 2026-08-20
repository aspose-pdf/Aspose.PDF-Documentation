---
title: Ruby에서 PDF 파일을 개별 페이지로 분할
linktitle: Ruby에서 PDF 파일을 개별 페이지로 분할
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
description: Ruby 및 Aspose.PDF를 사용하여 PDF 파일을 개별 페이지로 분할하는 방법을 이해하여 콘텐츠를 더 쉽게 관리하고 추출할 수 있습니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 분할 페이지



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 개별 페이지로 분할하려면 **SplitAllPages** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **Split Pages(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
