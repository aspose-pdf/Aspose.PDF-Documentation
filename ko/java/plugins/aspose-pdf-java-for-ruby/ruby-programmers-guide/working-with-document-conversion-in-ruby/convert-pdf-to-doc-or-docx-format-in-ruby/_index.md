---
title: PDF를 DOC 또는 DOCX 형식으로 변환하기 - Ruby
type: docs
weight: 30
url: /ko/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 DOC 또는 DOCX로 변환

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 DOC 또는 DOCX 형식으로 변환하려면, **PdfToDoc** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉터리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서를 엽니다

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 연결된 출력 파일을 저장합니다 (대상 문서)

pdf.save(data_dir + "output.doc")

puts "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to DOC or DOCX (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)