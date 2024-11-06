---
title: 루비에서 PDF 파일의 특정 페이지 삭제
type: docs
weight: 20
url: ko/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 삭제

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에서 특정 페이지를 삭제하려면, **DeletePage** 모듈을 호출하십시오.

루비 코드

```java
# 문서 디렉토리의 경로를 설정합니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서를 엽니다.

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 특정 페이지를 삭제합니다.

pdf.getPages().delete(2)

# 새로 생성된 PDF 파일을 저장합니다.

pdf.save(data_dir + "output.pdf")

puts "페이지가 성공적으로 삭제되었습니다!"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Delete Page (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)