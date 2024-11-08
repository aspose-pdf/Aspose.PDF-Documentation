---
title: スタンプからテキストを抽出
type: docs
weight: 60
url: /ja/java/extract-text-from-stamps/
---

## スタンプ注釈からテキストを抽出

Aspose.PDF for Javaを使用すると、スタンプ注釈からテキストを抽出できます。PDFのスタンプ注釈からテキストを抽出するには、次の手順を使用します。

1. Documentクラスのオブジェクトを作成する
1. ページの注釈リストから目的の注釈を取得する
1. TextAbsorberクラスの新しいオブジェクトを定義する
1. TextAbsorberのvisitメソッドを使用してテキストを取得する

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