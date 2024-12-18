---
title: 루비에서 PDF 파일을 개별 페이지로 분할
type: docs
weight: 80
url: /ko/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 분할

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 개별 페이지로 분할하려면, **SplitAllPages** 모듈을 호출하십시오.

루비 코드

```java

# 문서 디렉토리 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서 열기

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 모든 페이지를 순회하기

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# 새 Document 객체 생성

new_document = Rjb::import('com.aspose.pdf.Document').new

# Page Collection의 특정 인덱스에서 페이지 가져오기

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 새로 생성된 PDF 파일 저장

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "분할 프로세스가 성공적으로 완료되었습니다!"
```


## 실행 코드 다운로드

**Split Pages (Aspose.PDF)**를 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)