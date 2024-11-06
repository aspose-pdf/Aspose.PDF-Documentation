---
title: 루비에서 JavaScript 추가
type: docs
weight: 10
url: ko/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - JavaScript 추가

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서에 JavaScript를 추가하려면, 간단히 **AddJavaScript** 모듈을 호출하세요.

루비 코드

```java
# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 문서 레벨에서 JavaScript 추가

# 원하는 JavaScript 문을 사용하여 JavascriptAction을 인스턴스화합니다.

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Document의 원하는 액션에 JavascriptAction 객체를 할당합니다.

doc.setOpenAction(javaScript)

# 페이지 레벨에서 JavaScript 추가

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# PDF 문서 저장

doc.save(data_dir + "JavaScript-Added.pdf")

puts "JavaScript가 성공적으로 추가되었습니다. 출력 파일을 확인하세요."
```


## 코드 실행 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **JavaScript 추가 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)