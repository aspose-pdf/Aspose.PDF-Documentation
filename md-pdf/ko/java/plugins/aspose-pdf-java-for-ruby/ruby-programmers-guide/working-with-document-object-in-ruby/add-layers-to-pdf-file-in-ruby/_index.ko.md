---
title: 루비에서 PDF 파일에 레이어 추가
type: docs
weight: 20
url: /java/add-layers-to-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 레이어 추가

<ins> **Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서에 레이어를 추가하려면, **AddLayers** 모듈을 호출하십시오.

루비 코드

```java
# 문서 디렉토리의 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

doc = Rjb::import('com.aspose.pdf.Document').new

page = doc.getPages().add()

operator = Rjb::import('com.aspose.pdf.Operator')

layer = Rjb::import('com.aspose.pdf.Layer').new("oc1", "Red Line")

layer.getContents().add(operator.SetRGBColorStroke(1, 0, 0))

layer.getContents().add(operator.MoveTo(500, 700))

layer.getContents().add(operator.LineTo(400, 700))

layer.getContents().add(operator.Stroke())

page.setLayers(Rjb::import('java.util.ArrayList').new)

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc2", "Green Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 1, 0))

layer.getContents().add(operator.MoveTo(500, 750))

layer.getContents().add(operator.LineTo(400, 750))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc3", "Blue Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 0, 1))

layer.getContents().add(operator.MoveTo(500, 800))

layer.getContents().add(operator.LineTo(400, 800))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

# PDF 문서 저장

doc.save(data_dir + "Layers-Added.pdf")

puts "레이어가 성공적으로 추가되었습니다. 출력 파일을 확인하십시오."
```


## 코드 실행 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **레이어 추가 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)