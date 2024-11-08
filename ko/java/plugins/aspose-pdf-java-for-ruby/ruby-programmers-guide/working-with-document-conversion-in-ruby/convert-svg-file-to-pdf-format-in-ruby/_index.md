---
title: 루비에서 SVG 파일을 PDF 형식으로 변환
type: docs
weight: 60
url: /ko/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - SVG를 PDF로 변환

**Aspose.PDF Java for Ruby**를 사용하여 SVG 파일을 PDF 형식으로 변환하려면, **SvgToPdf** 모듈을 호출하세요.

루비 코드

```java

# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# SVG 로드 옵션을 사용하여 LoadOption 객체를 인스턴스화합니다.

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# 문서 객체를 만듭니다.

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# 출력을 XLS 형식으로 저장합니다.

pdf.save(data_dir + "SVG.pdf")

puts "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Convert SVG to PDF (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)