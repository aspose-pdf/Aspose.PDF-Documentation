---
title: RubyでPDFからメタデータを削除
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - メタデータの削除

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントからメタデータを削除するには、単に**RemoveMetadata**モジュールを呼び出します。

Ruby コード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# 新しい情報で更新されたドキュメントを保存します

doc.save(data_dir + "Remove_Metadata.pdf")

puts "メタデータが正常に削除されました。出力ファイルを確認してください。"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Remove Metadata (Aspose.PDF)**をダウンロードします:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)