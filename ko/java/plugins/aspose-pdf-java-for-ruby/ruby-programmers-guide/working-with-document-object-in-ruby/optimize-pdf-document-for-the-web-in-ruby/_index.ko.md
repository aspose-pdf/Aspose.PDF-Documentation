---
title: 웹을 위한 PDF 문서 최적화 - 루비
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 웹을 위한 PDF 최적화

**Aspose.PDF Java for Ruby**를 사용하여 웹을 위한 PDF 문서를 최적화하려면, **Optimize** 모듈의 **optimize_web** 메서드를 호출하십시오.

루비 코드

```java

 def optimize_web()

    # 문서 디렉토리의 경로입니다.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # PDF 문서를 엽니다.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # 웹을 위해 최적화합니다.

    doc.optimize()

    # 출력 문서를 저장합니다.

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "웹을 위한 PDF가 최적화되었습니다. 출력 파일을 확인하십시오."

end
``` 

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Optimize PDF for Web (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)