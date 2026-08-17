---
title: Ruby의 PDF 파일에서 특정 페이지 삭제
linktitle: Ruby의 PDF 파일에서 특정 페이지 삭제
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Ruby용 Aspose.PDF를 사용하여 프로그래밍 방식으로 PDF 파일에서 특정 페이지를 제거합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 삭제



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 특정 페이지를 삭제하려면 **DeletePage** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **페이지 삭제(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
