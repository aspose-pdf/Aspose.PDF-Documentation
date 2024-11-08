---
title: スタンプからテキストを抽出 
linktitle: スタンプからテキストを抽出
type: docs
weight: 60
url: /ja/cpp/extract-text-from-stamps/
---

## スタンプ注釈からテキストを抽出

Aspose.PDF for C++ を使用すると、スタンプ注釈からテキストを抽出できます。PDF のスタンプ注釈からテキストを抽出するには、次の手順を使用します。

1. Document クラスオブジェクトを作成する
1. ページの注釈リストから目的の注釈を取得する
1. TextAbsorber クラスの新しいオブジェクトを定義する
1. TextAbsorber の visit メソッドを使用してテキストを取得する

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // パス名の文字列
      String _dataDir("C:\\Samples\\Parsing\\");

      // ファイル名の文字列
      String infilename("ExtractStampText.pdf");

      auto document = MakeObject<Document>(_dataDir + infilename);

      auto item = document->get_Pages()->idx_get(1)->get_Annotations()->idx_get(1);
      if (item->get_AnnotationType() == Annotations::AnnotationType::Stamp) {
            auto annot = System::DynamicCast<Aspose::Pdf::Annotations::StampAnnotation>(item);
            auto ta = MakeObject<TextAbsorber>();
            auto ap = annot->get_Appearance()->idx_get(u"N");
            ta->Visit(ap);
            Console::WriteLine(ta->get_Text());
      }
}
```
```