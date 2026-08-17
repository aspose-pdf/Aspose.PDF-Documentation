---
title: Ruby에서 페이지 차원 업데이트
linktitle: Ruby에서 페이지 차원 업데이트
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
description: 정확한 페이지 서식 지정을 위해 Aspose.PDF와 함께 Ruby를 사용하여 PDF 문서의 페이지 크기를 업데이트하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 크기 업데이트



**Aspose.PDF Java for Ruby**를 사용하여 페이지 차원을 업데이트하려면 **UpdatePageDimensions** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## 
실행 코드 다운로드



아래 언급된 소셜 코딩 사이트에서 В **업데이트 페이지 크기(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
