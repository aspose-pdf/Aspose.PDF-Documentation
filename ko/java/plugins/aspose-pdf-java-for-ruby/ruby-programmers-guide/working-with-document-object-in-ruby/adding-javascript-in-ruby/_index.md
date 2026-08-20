---
title: Ruby에 JavaScript 추가하기
linktitle: Ruby에 JavaScript 추가하기
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
description: 상호작용 및 자동화를 위해 Ruby에서 Aspose.PDF를 사용하여 PDF에서 JavaScript 기능을 활성화합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - JavaScript 추가



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 JavaScript를 추가하려면 **AddJavaScript** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## 
실행 코드 다운로드



아래 언급된 소셜 코딩 사이트 중 하나에서 В **JavaScript 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
