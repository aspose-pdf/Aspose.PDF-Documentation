---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: PDFファイルを最適化し、すべての画像を縮小し、PDFのサイズを縮小し、フォントの埋め込みを解除し、ページコンテンツの再利用を有効にし、注釈を削除またはフラット化するC++を使用します。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

まず第一に、PDFの最適化はユーザーのために行います。PDFでは、ユーザーの最適化は主にPDFのサイズを減らして読み込み速度を上げることに関するものです。これは最も人気のあるタスクです。
PDFを最適化するためにいくつかの技術を使用できますが、最も重要なものは次のとおりです：

- オンライン閲覧用にページコンテンツを最適化する
- すべての画像を縮小または圧縮する
- ページコンテンツの再利用を有効にする
- 重複するストリームをマージする
- フォントの埋め込みを解除する
- 未使用のオブジェクトを削除する
- フォームフィールドのフラット化を削除する
- 注釈を削除またはフラット化する

## ウェブ用にPDFドキュメントを最適化する

PDFドキュメントのコンテンツを検索エンジンでのランキングを向上させるために最適化するタスクに直面したとき、Aspose.PDF for C++には解決策があります。

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトで入力ドキュメントを開きます。
1. [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda) メソッドを使用します。
1. Save メソッドを使用して最適化されたドキュメントを保存します。

次のコードスニペットは、PDF ドキュメントをウェブ用に最適化する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//ウェブ用に PDF ドキュメントを最適化
void OptimizeForWeb() {
    // パス名用の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名用の文字列
    String outfilename("OptimizeDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>();

    // いくつかの操作を行う（ページ、画像などを追加）
    // ...

    // ウェブ用に最適化
    document->Optimize();

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

## PDF のサイズを縮小

[OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) メソッドを使用すると、不要な情報を除去してドキュメントのサイズを縮小できます。 デフォルトでは、このメソッドは次のように動作します：

- ドキュメントページで使用されていないリソースは削除されます
- 同じリソースは1つのオブジェクトに結合されます
- 使われていないオブジェクトは削除されます

以下のスニペットは例です。ただし、このメソッドがドキュメントの縮小を保証するものではないことに注意してください。

```cpp
void ReduceSizePDF() {

    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String outfilename("ShrinkDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>();
    // いくつかの操作を行う（ページ、画像の追加など）
    // ...

    // PDFドキュメントを最適化する。ただし、このメソッドがドキュメントの縮小を保証するものではないことに注意してください
    document->OptimizeResources();

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

## 最適化戦略の管理

最適化戦略をカスタマイズすることもできます。 現在、[OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) メソッドは5つの手法を使用しています。これらの手法は、[OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/) パラメータを使用して OptimizeResources() メソッドを使用することで適用できます。

### すべての画像を縮小または圧縮する

PDFドキュメント内の画像を最適化するには、[Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization) を使用します。画像の最適化の問題を解決するために、以下のオプションがあります：画像の品質を下げるおよび/または解像度を変更する。 いずれにせよ、[ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) を適用する必要があります。次の例では、[ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) を50に減らすことで画像を縮小します。

```cpp
void CompressImage() {
    // パスの名前のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptionsを初期化する
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImagesオプションを設定する
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQualityオプションを設定する
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // OptimizationOptionsを使用してPDFドキュメントを最適化する
    document->OptimizeResources(optimizationOptions); 
    // 更新されたドキュメントを保存する
    document->Save(_dataDir + outfilename);
}
```
画像を低解像度に設定するには、[ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6)をtrueに設定し、[MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e)を対応する値に設定します。

```cpp
void ResizeImagesWithLowerResolution() {
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptionsを初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImagesオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQualityオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // ResizeImageオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // MaxResolutionオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    document->OptimizeResources(optimizationOptions);
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++は、実行時設定に対するコントロールも提供します。現在、標準と高速の2つのアルゴリズムを使用できます。実行時間を制御するには、[Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4)プロパティを設定する必要があります。

次のスニペットは、高速アルゴリズムを示しています:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptionsを初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImagesオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQualityオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // ResizeImageオプションを設定
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // 画像圧縮バージョンを高速に設定
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    document->OptimizeResources(optimizationOptions);
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### 未使用オブジェクトの削除

時々、PDFドキュメントのページで参照されていない未使用のオブジェクトを削除する必要があるかもしれません。これは、例えば、ドキュメントのページツリーからページが削除されたが、ページオブジェクト自体が削除されていない場合に発生することがあります。これらのオブジェクトを削除してもドキュメントが無効になるわけではなく、むしろ縮小されます。次のコードスニペットを確認してください:

```cpp
void RemovingUnusedObject() { 
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptionsを初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // RemoveUsedObjectオプションを設定
    optimizationOptions->set_RemoveUnusedObjects(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    document->OptimizeResources(optimizationOptions);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename); 
}
```

### 未使用ストリームの削除

時には、ドキュメントに未使用のリソースストリームが含まれていることがあります。これらのストリームはページリソース辞書から参照されているため、「未使用オブジェクト」ではありません。したがって、「未使用オブジェクトの削除」メソッドで削除されることはありません。しかし、これらのストリームはページのコンテンツで使用されることはありません。これは、画像がページから削除されたがページリソースからは削除されていない場合に発生することがあります。また、この状況は、ドキュメントからページが抽出され、ドキュメントページが「共通の」リソース、つまり同じResourcesオブジェクトを持っている場合によく発生します。リソースストリームが使用されているかどうかを判断するためにページコンテンツが分析されます。未使用のストリームは削除されます。これにより、ドキュメントのサイズが縮小されることがあります。この技法の使用は前のステップと似ています：

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### 重複ストリームのリンク

いくつかのドキュメントには、複数の重複するリソースストリーム（例えば、画像など）を含むことがあります。これは、例えばドキュメントが自分自身と連結されたときに発生することがあります。出力ドキュメントには同じリソースストリームの2つの独立したコピーが含まれています。私たちはすべてのリソースストリームを分析し、それらを比較します。ストリームが重複している場合、それらは統合され、つまり1つのコピーだけが残ります。参照は適切に変更され、オブジェクトのコピーは削除されます。場合によっては、ドキュメントサイズを減少させるのに役立ちます。

```cpp
void LinkingDuplicateStreams() {
    // パス名用の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名用の文字列
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptionsを初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // LinkDuplcateStreamsオプションを設定
    optimizationOptions->set_LinkDuplcateStreams(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    document->OptimizeResources(optimizationOptions);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

さらに、[AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8) 設定を使用できます。このプロパティが true に設定されている場合、ドキュメントを同一のページに対して最適化する際にページの内容が再利用されます。

```cpp
void AllowReusePageContent() { 
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions を初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // AllowReusePageContent オプションを設定
    optimizationOptions->set_AllowReusePageContent(true);

    // OptimizationOptions を使用して PDF ドキュメントを最適化
    document->OptimizeResources(optimizationOptions);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename); 
}
```

### フォントの埋め込み解除

個人デザインファイルのPDFバージョンを作成すると、必要なすべてのフォントのコピーがPDFファイル自体に追加されます。これが埋め込みです。このPDFがあなたのコンピュータ、友人のコンピュータ、または印刷業者のコンピュータで開かれたとしても、すべての正しいフォントがそこにあり、正しくレンダリングされます。

しかし、文書が埋め込みフォントを使用している場合、すべてのフォントデータが文書内に保存されていることを意味します。利点は、フォントがユーザーのマシンにインストールされているかどうかに関係なく、文書を表示できることです。しかし、フォントを埋め込むと文書が大きくなります。フォントの埋め込み解除メソッドは、すべての埋め込みフォントを削除します。したがって、文書のサイズは小さくなりますが、正しいフォントがインストールされていない場合、文書自体が読めなくなる可能性があります。

```cpp
void UnembedFonts() {
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 文書を開く
    auto document = MakeObject<Document>(_dataDir+infilename);

    // OptimizationOptionsを初期化
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // AllowReusePageContentオプションを設定
    optimizationOptions->set_UnembedFonts(true);

    // OptimizationOptionsを使用してPDF文書を最適化
    document->OptimizeResources(optimizationOptions);

    // 更新した文書を保存
    document->Save(_dataDir + outfilename);
}
```

最適化リソースは、これらの方法をドキュメントに適用します。これらの方法のいずれかが適用されると、ドキュメントのサイズはおそらく減少します。これらの方法のいずれも適用されない場合、ドキュメントのサイズは変わらないでしょう。それは明らかです。

## PDFドキュメントサイズを削減する追加の方法

### 注釈の削除またはフラット化

PDFドキュメントに注釈があると、そのサイズが自然に増加します。
注釈は不要な場合に削除できます。必要だが追加の編集が不要な場合は、フラット化できます。これらの技術のいずれもファイルサイズを削減します。

```cpp
void FlatteningAnnotation() {
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String infilename("OptimizeDocument.pdf");
    // 出力ファイル名のための文字列
    String outfilename("OptimizeDocument_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 注釈をフラット化
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

### フォームフィールドの削除

PDFからフォームを削除することで、ドキュメントを最適化することができます。PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを削減することができます。

```cpp
void FlatteningFormFields() {
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String infilename("OptimizeFormField.pdf");
    // 出力ファイル名の文字列
    String outfilename("OptimizeFormField_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // フォームフィールドをフラット化
    // フォームをフラット化
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outfilename);
}
```

### PDFをRGBカラースペースからグレースケールに変換する

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。 You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

PDFをRGB色空間からグレースケールに変換する必要に迫られることがあります。これにより、PDFファイルの印刷がより高速化されます。また、ファイルをグレースケールに変換すると、ドキュメントのサイズも縮小されますが、ドキュメントの品質が低下する可能性もあります。この機能は現在、Adobe AcrobatのPre-Flight機能でサポートされていますが、オフィス自動化の観点からは、Aspose.PDFがドキュメント操作のための究極のソリューションを提供します。この要件を達成するために、次のコードスニペットを使用できます。

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String infilename("OptimizeDocument.pdf");
    // 出力ファイル名の文字列
    String outfilename("Test-gray_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // PDF内の特定のページのインスタンスを取得
        auto page = document->get_Pages()->idx_get(idxPage);
        // RGB色空間の画像をグレースケール色空間に変換
        strategy->Convert(page);
    }
    // 結果のファイルを保存
    document->Save(_dataDir + outfilename); 
}
```
### FlateDecode 圧縮

Aspose.PDF for C++ は、PDF 最適化機能に対して FlateDecode 圧縮のサポートを提供します。
FlateDecode 圧縮を使用して画像を最適化するには、最適化オプションを Flate に設定します。
以下のコードスニペットは、最適化で **FlateDecode** 圧縮を使用して画像を保存する方法を示しています:

```cpp
void FlatDecodeCompression() {
 // パス名の文字列
 String _dataDir("C:\\Samples\\");

 // 入力ファイル名の文字列
 String infilename("FlateDecodeCompression.pdf");
 // 出力ファイル名の文字列
 String outfilename("FlateDecodeCompression_out.pdf");

 // ドキュメントを開く
 auto document = MakeObject<Document>(_dataDir + infilename);

 // OptimizationOptions を初期化
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // FlateDecode 圧縮を使用して画像を最適化するには、最適化オプションを Flate に設定
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // OptimizationOptions を使用してPDFドキュメントを最適化
 document->OptimizeResources(optimizationOptions);

 // 更新されたドキュメントを保存
 document->Save(_dataDir + outfilename);
}
```

### **XImageCollectionに画像を保存する**

Aspose.PDF for C++ は、FlateDecode圧縮を使用して[XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection)に新しい画像を保存する機能を提供します。このオプションを有効にするには、**ImageFilterType.Flate**フラグを使用します。以下のコードスニペットは、この機能を使用する方法を示しています:

```cpp
void StoreImageInXImageCollection() {

 // パス名の文字列
 String _dataDir("C:\\Samples\\");

 // 出力ファイル名の文字列
 String outfilename("FlateDecodeCompression_out.pdf");

 // ドキュメントを開く
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // 座標を設定
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // ConcatenateMatrix（行列を連結する）オペレーターを使用: 画像の配置方法を定義します
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```