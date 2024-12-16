---

title: PDFでのXFAフォームの操作  
linktitle: XFAフォーム  
type: docs  
weight: 20  
url: /ja/java/xfa-forms/  
description: Aspose.PDF for Javaを使用して、ゼロからフォームを作成したり、PDFドキュメントのフォームフィールドに入力したり、フォームからデータを抽出したり、既存のフォームにフィールドを追加または削除したりできます。  
lastmod: "2021-06-05"  
sitemap:  
 changefreq: "weekly"  
 priority: 0.7  

---

XFAはXML Forms Architectureの略です。これは1999年にウェブフォームでの使用を目的に初めて開発された一連の独自のXML仕様であり、その後PDFでも利用可能になりました。

## 動的XFAフォームを標準のAcroFormに変換

動的フォームはXFAとして知られるXML仕様に基づいています。「XML Forms Architecture」です。動的XFAフォームを標準のAcroformに変換することもできます。フォームに関する情報（PDFに関する限り）は非常に曖昧で、フィールドが存在すること、プロパティ、およびJavaScriptイベントがあることを指定しますが、レンダリングは指定しません。XFAフォームのオブジェクトは、ドキュメントをロードする時に描画されます。

現在、PDFはデータとPDFフォームを統合するための2つの異なる方法をサポートしています。

- AcroForms（アクロバットフォームとも呼ばれる）は、PDF 1.2 フォーマット仕様で導入されました。

- Adobe XML Forms Architecture (XFA) フォームは、オプション機能として PDF 1.5 フォーマット仕様で導入されました。（XFA 仕様は PDF 仕様に含まれておらず、参照されているだけです。）

XFA フォームのページを抽出または操作することはできません。なぜなら、フォームの内容はアプリケーションが XFA フォームを表示またはレンダリングしようとする際に、実行時に生成されるからです。Aspose.PDF には、XFA フォームを標準的な AcroForms に変換する機能があります。

```java
// 動的な XFA フォームを読み込む
Document document = new Document("XFAform.pdf");
// フォームフィールドのタイプを標準的な AcroForm に設定する
document.getForm().setType(FormType.Standard);
// 結果の PDF を保存する
document.save("Standard_AcroForm.pdf");
```