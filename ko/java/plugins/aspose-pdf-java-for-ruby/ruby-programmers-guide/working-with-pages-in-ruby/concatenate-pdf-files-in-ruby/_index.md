---
title: 루비에서 PDF 파일 연결
type: docs
weight: 10
url: ko/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 연결

**Aspose.PDF Java for Ruby**를 사용하여 PDF 파일을 연결하려면, **ConcatenatePdfFiles** 모듈을 호출하십시오.

루비 코드

```java
# 문서 디렉토리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서 열기

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 소스 문서 열기

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# 소스 문서의 페이지를 대상 문서에 추가

pdf1.getPages().add(pdf2.getPages())

# 연결된 출력 파일 저장 (대상 문서)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "새 문서가 저장되었습니다. 출력 파일을 확인해 주세요."
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 연결 (Aspose.PDF)**을 다운로드하십시오.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)