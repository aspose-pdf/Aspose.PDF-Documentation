---
title: 루비에서 PDF 파일 크기 최적화
type: docs
weight: 80
url: /ko/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 크기 최적화

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 파일 크기를 최적화하려면, **Optimize** 모듈의 **optimize_filesize** 메소드를 호출하세요.

루비 코드

```java

 def optimize_filesize()

    # 문서 디렉토리 경로입니다.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # PDF 문서를 엽니다.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # 사용되지 않는 객체를 제거하여 파일 크기를 최적화합니다.

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # 출력 문서 저장

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "최적화된 PDF 파일 크기입니다. 출력 파일을 확인하세요."

end 
```

## 실행 코드 다운로드

Download **PDF 파일 크기 최적화 (Aspose.PDF)** 아래 언급된 소셜 코딩 사이트 중 어느 곳에서나 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)