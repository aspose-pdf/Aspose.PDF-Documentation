---
title: PDF/A を PDF 形式に変換
linktitle: PDF/A を PDF 形式に変換
type: docs
weight: 110
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDF を使用して PDF/A ファイルを C++ ライブラリで PDF ドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A ドキュメントを PDF に変換

PDF/A ドキュメントを PDF に変換することは、元のドキュメントから<abbr title="Portable Document Format Archive
">PDF/A</abbr>制限を削除することを意味します。クラス [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) には、入力/ソースファイルから PDF 準拠情報を削除するためのメソッド 'RemovePdfaCompliance' があります。
入力ファイルを[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)した後。

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // PDF/A 準拠情報を削除
    document->RemovePdfaCompliance();

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

この情報は、ドキュメントに変更を加えた場合（例: ページを追加する）にも削除されます。次の例では、ページを追加した後、出力ドキュメントはPDF/Aの準拠性を失います。

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // 新しい（空の）ページを追加すると、PDF/Aの準拠情報が削除されます。

    document->get_Pages()->Add();
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```