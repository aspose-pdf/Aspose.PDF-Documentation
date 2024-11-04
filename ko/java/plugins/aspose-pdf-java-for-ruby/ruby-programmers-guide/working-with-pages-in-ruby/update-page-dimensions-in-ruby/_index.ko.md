---
title: Update Page Dimensions in Ruby
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 크기 업데이트

**Aspose.PDF Java for Ruby**를 사용하여 페이지 크기를 업데이트하려면, **UpdatePageDimensions** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉토리의 경로

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서 열기

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 페이지 컬렉션 가져오기

page_collection = pdf.getPages()

# 특정 페이지 가져오기

pdf_page = page_collection.get_Item(1)

# 페이지 크기를 A4(11.7 x 8.3 인치)로 설정하고 Aspose.PDF에서는 1인치 = 72포인트

# 따라서 A4 크기는 포인트로 (842.4, 597.6)입니다.

pdf_page.setPageSize(597.6,842.4)

# 새로 생성된 PDF 파일 저장

pdf.save(data_dir + "output.pdf")

puts "크기 업데이트 성공!"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Update Page Dimensions (Aspose.PDF)**를 다운로드하세요.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)

```ruby
# 페이지 크기 업데이트
require 'java'
require File.dirname(__FILE__) + '/../../lib/asposepdfjava'

include Asposepdfjava

begin
    # 문서 객체 초기화
    pdf_document = Rjb::import('com.aspose.pdf.Document').new("example.pdf")

    # 페이지 수 얻기
    page_count = pdf_document.getPages().size()
    
    # 각 페이지 크기 업데이트
    (1..page_count).each do |i|
        page = pdf_document.getPages().get_Item(i)
        
        # 페이지 크기 설정
        page.setPageSize(400, 400)
    end

    # 업데이트된 문서 저장
    pdf_document.save("updated_example.pdf")
    
rescue Exception => e
    puts "문서 업데이트 중 오류 발생: #{e}"
end
`