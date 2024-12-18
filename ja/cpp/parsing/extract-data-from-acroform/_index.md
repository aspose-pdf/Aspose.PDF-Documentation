---
title: AcroFormからデータを抽出する
linktitle: AcroFormからデータを抽出する
type: docs
weight: 50
url: /ja/cpp/extract-data-from-acroform/
description: Aspose.PDFを使用すると、PDFファイルからフォームフィールドデータを簡単に抽出できます。AcroFormsからデータを抽出し、XMLまたはFDF形式に保存する方法を学びます。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントからフォームフィールドを抽出する

Aspose.PDF for C++を使用すると、フォームフィールドを作成し、フォームフィールドに入力するだけでなく、PDFファイルからフォームフィールドデータやフォームフィールド情報を抽出することも簡単にできます。

以下のコード例では、PDF内の各ページを反復処理して、PDF内のすべてのAcroFormsおよびフォームフィールド値に関する情報を抽出する方法を示しています。このコード例は、事前にフォームフィールドの名前を知らないことを前提としています。

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名の文字列
    String infilename("StudentInfoFormElectronic.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // すべてのフィールドから値を取得
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "フィールド名 :" << formField->get_PartialName() << std::endl;
        std::cout << "値 : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルからXMLへのデータ抽出

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) クラスを使用すると、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートできます。XMLにデータをエクスポートするには、まずFormクラスのオブジェクトを作成し、次にFileStreamオブジェクトを使用してExportXmlメソッドを呼び出す必要があります。次にFileStreamオブジェクトを閉じ、Formオブジェクトを破棄する必要があります。

次のコードスニペットは、データをXMLファイルにエクスポートする方法を示しています。

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // データをエクスポート
    form->ExportXml(fdfOutputStream);

    // ファイルストリームを閉じる
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルからFDFへのデータのエクスポート

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) クラスは、ExportFdfメソッドを使用してPDFファイルからFDFファイルにデータをエクスポートすることを可能にします。データをFDFにエクスポートするためには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportFdfメソッドを呼び出す必要があります。その後、FormクラスのSaveメソッドを使用してPDFファイルを保存することができます。

以下のコードスニペットは、データをFDFファイルにエクスポートする方法を示しています。

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名の文字列
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // データのエクスポート
    form->ExportFdf(fdfOutputStream);

    // ファイルストリームを閉じる
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルからXFDFへのデータのエクスポート

Aspose PDF for C++の[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form)クラスを使用すると、ExportXfdfメソッドを使用してPDFファイルからXFDFファイルにデータをエクスポートできます。XFDFにデータをエクスポートするためには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXfdfメソッドを呼び出す必要があります。

最後に、FormクラスのSaveメソッドを使用してPDFファイルを保存することができます。

以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名の文字列
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // データのエクスポート
    form->ExportXfdf(fdfOutputStream);

    // ファイルストリームを閉じる
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```