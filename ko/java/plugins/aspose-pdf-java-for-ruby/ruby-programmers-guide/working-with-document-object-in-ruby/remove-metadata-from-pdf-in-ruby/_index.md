---
title: Ruby의 PDF에서 메타데이터 제거
linktitle: Ruby의 PDF에서 메타데이터 제거
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: Ruby용 Aspose.PDF를 사용하여 PDF 파일에서 민감하거나 원치 않는 메타데이터를 프로그래밍 방식으로 삭제하세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 메타데이터 제거



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 메타데이터를 제거하려면 **RemoveMetadata** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## 
실행 코드 다운로드



아래 언급된 소셜 코딩 사이트에서 В **메타데이터 제거(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
