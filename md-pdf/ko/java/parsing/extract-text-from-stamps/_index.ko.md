---
title: 스탬프에서 텍스트 추출
type: docs
weight: 60
url: /java/extract-text-from-stamps/
---

## 스탬프 주석에서 텍스트 추출

Aspose.PDF for Java를 사용하면 스탬프 주석에서 텍스트를 추출할 수 있습니다. PDF에서 스탬프 주석의 텍스트를 추출하려면 다음 단계를 사용할 수 있습니다.

1. Document 클래스 객체 생성
1. 페이지의 주석 목록에서 원하는 주석 가져오기
1. TextAbsorber 클래스의 새 객체 정의
1. TextAbsorber의 visit 메서드를 사용하여 텍스트 가져오기

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```