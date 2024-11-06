---
title: Ruby에서 PDF 파일의 특정 페이지 가져오기
type: docs
weight: 30
url: ko/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 가져오기

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 특정 페이지를 가져오려면 **GetPage** 모듈을 호출하십시오.

Ruby 코드

```java
# 문서 디렉토리의 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서 열기

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 페이지 컬렉션의 특정 인덱스에 있는 페이지 가져오기

pdf_page = pdf.getPages().get_Item(1)

# 새로운 Document 객체 생성

new_document = Rjb::import('com.aspose.pdf.Document').new

# 새 문서 객체의 페이지 컬렉션에 페이지 추가

new_document.getPages().add(pdf_page)

# 새로 생성된 PDF 파일 저장

new_document.save(data_dir + "output.pdf")

puts "프로세스가 성공적으로 완료되었습니다!"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get Page (Aspose.PDF)**를 다운로드하십시오.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)