---
title: Ruby에서 PDF 파일 정보 설정
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 정보 설정

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서 정보를 업데이트하려면, **SetPdfFileInfo** 모듈을 호출하십시오.

Ruby 코드

```java

# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 문서 정보를 가져옵니다.

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF 정보")

doc_info.setTitle("PDF 문서 정보 설정")

# 새로운 정보로 문서 업데이트 저장

doc.save(data_dir + "Updated_Information.pdf")

puts "문서 정보가 업데이트되었습니다. 출력 파일을 확인하십시오."
```


## 실행 코드 다운로드

다음의 소셜 코딩 사이트 중 하나에서 **Set PDF File Information (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)