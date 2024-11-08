---
title: Ruby에서 PDF 파일에서 XMP 메타데이터 가져오기
type: docs
weight: 60
url: /ko/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - XMP 메타데이터 가져오기

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 XMP 메타데이터를 가져오려면, **GetXMPMetadata** 모듈을 호출하십시오.

Ruby 코드

```java
# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 속성 가져오기

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get XMP Metadata (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)