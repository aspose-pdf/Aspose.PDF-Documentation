---
title: PDF를 Excel 워크북으로 변환하기 (Ruby)
type: docs
weight: 40
url: ko/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 Excel 워크북으로 변환하기

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 Excel 워크북으로 변환하려면, **PdfToExcel** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서를 엽니다

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Excel 저장 옵션 객체를 인스턴스화합니다

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# XLS 형식으로 출력 저장

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to DOC or DOCX (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)