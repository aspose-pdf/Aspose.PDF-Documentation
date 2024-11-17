---
title: 빈 페이지를 PDF 파일에 삽입하기 (Ruby)
type: docs
weight: 70
url: /ko/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 빈 페이지 삽입

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 빈 페이지를 삽입하려면, **InsertEmptyPage** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉토리의 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서 열기

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# PDF에 빈 페이지 삽입

pdf.getPages().insert(1)

# 연결된 출력 파일 저장 (대상 문서)

pdf.save(data_dir+ "output.pdf")

puts "빈 페이지가 성공적으로 추가되었습니다!"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트에서 **Insert an Empty Page (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)