---
title: 루비에서 PDF 파일 정보 가져오기
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 정보 가져오기

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서의 파일 정보를 가져오려면, **GetPdfFileInfo** 모듈을 호출하세요.

루비 코드

```java
# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# pdf 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 문서 정보 가져오기

doc_info = doc.getInfo()

# 문서 정보 표시

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get PDF File Information (Aspose.PDF)**을 다운로드하세요.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
`