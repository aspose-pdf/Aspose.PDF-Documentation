---
title: Ruby에서 PDF 파일 정보 설정
linktitle: Ruby에서 PDF 파일 정보 설정
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: Ruby를 사용하여 제목, 작성자, 키워드와 같은 PDF 메타데이터를 프로그래밍 방식으로 정의하고 업데이트합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 정보 설정



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서 정보를 업데이트하려면 **SetPdfFileInfo** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 정보 설정(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
