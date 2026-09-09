---
title: Ruby에서 웹용 PDF 문서 최적화
linktitle: Ruby에서 웹용 PDF 문서 최적화
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: Ruby에서 Aspose.PDF를 사용하여 더 빠른 웹 제공과 파일 크기 감소를 위해 PDF를 간소화하세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 웹용 PDF 최적화



**Aspose.PDF Java for Ruby**를 사용하여 웹용 PDF 문서를 최적화하려면 **Optimize** 모듈의 **optimize_web** 메소드를 호출하기만 하면 됩니다.

루비 코드


```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서**웹용 PDF 최적화(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
