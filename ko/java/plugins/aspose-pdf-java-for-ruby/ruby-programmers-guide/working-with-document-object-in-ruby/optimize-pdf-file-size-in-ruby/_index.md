---
title: Ruby에서 PDF 파일 크기 최적화
linktitle: Ruby에서 PDF 파일 크기 최적화
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
description: Ruby용 Aspose.PDF를 사용하여 품질 저하 없이 PDF 파일 크기를 줄이는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 크기 최적화



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 파일 크기를 최적화하려면 **Optimize** 모듈의 **optimize_filesize** 메서드를 호출하세요.



루비 코드


```java
 def optimize_filesize()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize the file size by removing unused objects

В В В  opt = Rjb::import('aspose.document.OptimizationOptions').new

В В В  opt.setRemoveUnusedObjects(true)

В В В  opt.setRemoveUnusedStreams(true)

В В В  opt.setLinkDuplcateStreams(true)

В В В  doc.optimizeResources(opt)

В В В  # Save output document

В В В  doc.save(data_dir + "Optimized_Filesize.pdf")

В В В  puts "Optimized PDF Filesize, please check output file."

endВ
```

## 
실행 코드 다운로드



아래 언급된 소셜 코딩 사이트에서 В **PDF 파일 크기 최적화(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
