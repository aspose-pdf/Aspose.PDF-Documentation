---
title: Ruby에서 PDF 만료 설정
linktitle: Ruby에서 PDF 만료 설정
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: 시간에 민감한 문서의 경우 Ruby용 Aspose.PDF를 사용하여 PDF에 만료 날짜를 구현하세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 만료 설정



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 만료를 설정하려면 **SetExpiration** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 만료 설정(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
