---
title: Ruby에서 PDF 파일 정보 얻기
linktitle: Ruby에서 PDF 파일 정보 얻기
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: Ruby에서 Aspose.PDF를 사용하여 프로그래밍 방식으로 PDF 파일에서 메타데이터 및 세부 정보를 추출합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 정보 얻기



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 파일 정보를 얻으려면 **GetPdfFileInfo** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 
실행 코드 다운로드



다운로드В **PDF 파일 정보(Aspose.PDF)**В를 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
