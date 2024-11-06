---
title: 모든 페이지에서 PDF 문서의 텍스트 추출하기 - 루비
type: docs
weight: 30
url: ko/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 모든 페이지에서 텍스트 추출

**Aspose.PDF Java for Ruby**를 사용하여 모든 페이지에서 PDF 문서의 텍스트를 추출하려면, **ExtractTextFromAllPages** 모듈을 호출하세요.

루비 코드

```java
# 문서 디렉터리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서를 엽니다.

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 텍스트를 추출하기 위한 TextAbsorber 객체를 생성합니다.

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# 모든 페이지에 대해 absorber를 허용합니다.

pdf.getPages().accept(text_absorber)

# 문서의 특정 페이지에서 텍스트를 추출하려면, accept(..) 메서드에 대해 인덱스를 사용하여 특정 페이지를 지정해야 합니다.

# 특정 PDF 페이지에 대해 absorber를 허용합니다.

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 추출된 텍스트를 가져옵니다.

extracted_text = text_absorber.getText()

# 작성자를 생성하고 파일을 엽니다.

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# 파일에 한 줄의 텍스트를 씁니다.

# tw.WriteLine(extractedText);

# 스트림을 닫습니다.

writer.close()

puts "텍스트가 성공적으로 추출되었습니다. 출력 파일을 확인하세요."
```


## Download Running Code

다음의 소셜 코딩 사이트에서 **Extract Text From All the Pages (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)