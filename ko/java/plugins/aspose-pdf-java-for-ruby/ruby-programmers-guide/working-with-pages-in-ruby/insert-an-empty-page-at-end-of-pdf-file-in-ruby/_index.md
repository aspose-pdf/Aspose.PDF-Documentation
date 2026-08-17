---
title: Ruby에서 PDF 파일 끝에 빈 페이지 삽입
linktitle: Ruby에서 PDF 파일 끝에 빈 페이지 삽입
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Aspose.PDF와 함께 Ruby를 사용하여 PDF 문서 끝에 빈 페이지를 삽입하여 PDF 처리 작업에 유연성을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 끝에 빈 페이지 삽입



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서 끝에 빈 페이지를 삽입하려면 **InsertEmptyPageAtEndOfFile** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## 
실행 코드 다운로드



**PDF 파일 끝에 빈 페이지 삽입(Aspose.PDF)**В을 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
