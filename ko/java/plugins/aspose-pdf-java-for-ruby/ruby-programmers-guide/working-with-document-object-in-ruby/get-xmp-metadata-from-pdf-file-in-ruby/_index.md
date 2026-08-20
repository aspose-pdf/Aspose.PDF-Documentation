---
title: Ruby의 PDF 파일에서 XMP 메타데이터 가져오기
linktitle: Ruby의 PDF 파일에서 XMP 메타데이터 가져오기
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Aspose.PDF와 함께 Ruby를 사용하여 PDF 문서의 XMP 메타데이터에 액세스하고 조작합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - XMP 메타데이터 가져오기



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 XMP 메타데이터를 얻으려면 **GetXMPMetadata** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드****XMP 메타데이터(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
