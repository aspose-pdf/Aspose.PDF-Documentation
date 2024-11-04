---
title: Ruby에서 PDF 만료 설정
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 만료 설정

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 만료를 설정하려면, **SetExpiration** 모듈을 호출하십시오.

Ruby 코드

```java
# 문서 디렉토리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('파일이 만료되었습니다. 새로운 파일이 필요합니다.');")

doc.setOpenAction(javascript)

# 새 정보로 문서 업데이트 저장

doc.save(data_dir + "set_expiration.pdf")

puts "문서 정보가 업데이트되었습니다. 출력 파일을 확인하십시오."
```


## 실행 코드 다운로드

**Set PDF Expiration (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)