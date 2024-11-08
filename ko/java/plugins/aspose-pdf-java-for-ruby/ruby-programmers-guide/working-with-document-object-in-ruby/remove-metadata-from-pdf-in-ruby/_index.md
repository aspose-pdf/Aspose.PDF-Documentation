---
title: PDF에서 메타데이터 제거하기 in Ruby
type: docs
weight: 90
url: /ko/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 메타데이터 제거하기

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서에서 메타데이터를 제거하려면, **RemoveMetadata** 모듈을 호출하십시오.

Ruby 코드

```java
# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# 새로운 정보로 문서 업데이트를 저장합니다.

doc.save(data_dir + "Remove_Metadata.pdf")

puts "메타데이터가 성공적으로 제거되었습니다. 출력 파일을 확인하십시오."
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Remove Metadata (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)