---
title: 埋め込まれた画像の解像度と寸法をC++で取得する
linktitle: 解像度と寸法の取得
type: docs
weight: 40
url: ja/cpp/get-resolution-and-dimensions-of-embedded-images/
description: このセクションでは、埋め込まれた画像の解像度と寸法を取得する方法を示します
lastmod: "2021-12-18"
---

このトピックでは、Aspose.PDF名前空間の演算子クラスを使用して、画像を抽出せずに解像度と寸法の情報を取得する機能を提供する方法を説明します。

これを達成するためのさまざまな方法があります。この記事では、`arraylist`と[画像配置クラス](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement)を使用する方法を説明します。

1. まず、ソースPDFファイル（画像を含む）を読み込みます。
1. 次に、ドキュメント内の画像名を保持するためのArrayListオブジェクトを作成します。
1. Page.Resources.Imagesプロパティを使用して画像を取得します。
1. 画像のグラフィックス状態を保持するためのスタックオブジェクトを作成し、異なる画像状態を追跡するために使用します。
1. 現在の変換を定義するConcatenateMatrixオブジェクトを作成します。また、任意のコンテンツのスケーリング、回転、スキューイングをサポートしています。新しい行列を以前のものと連結します。変換をゼロから定義することはできませんが、既存の変換を変更することのみが可能です。  
1. ConcatenateMatrixを使用して行列を変更できるため、元の画像状態に戻す必要がある場合もあります。[GSaveオペレーター](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/)と[GRestoreオペレーター](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/)を使用してください。これらのオペレーターはペアとなっているため、一緒に呼び出す必要があります。たとえば、複雑な変換を使用してグラフィック作業を行い、最終的に変換を初期状態に戻す場合、アプローチは次のようになります：

次のコードスニペットは、PDFドキュメントから画像を抽出することなく、画像の寸法と解像度を取得する方法を示しています。

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // ソースPDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // 画像のデフォルト解像度を定義
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // 画像名を保持する配列リストオブジェクトを定義
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // スタックにオブジェクトを挿入
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // ドキュメントの最初のページにあるすべてのオペレーターを取得
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // GSave/GRestoreオペレーターを使用して、変換を以前に設定された状態に戻す
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // 現在の変換行列を定義するConcatenateMatrixオブジェクトをインスタンス化
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // リソースからオブジェクトを描画するDoオペレーターを作成。これはフォームオブジェクトと画像オブジェクトを描画します。
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // 前の状態を保存し、現在の状態をスタックの上にプッシュ
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // 現在の状態を破棄し、前の状態を復元
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // 現在の行列を状態行列で乗算
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // これは画像描画オペレーターの場合
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // 最初のPDFページの画像を保持するXImageオブジェクトを作成
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // 画像の寸法を取得
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // 画像の高さと幅の情報を取得
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // 上記の情報に基づいて解像度を計算
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // 各画像の寸法と解像度情報を表示
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```