---
title: 埋め込み画像の解像度と寸法を取得する
linktitle: 解像度と寸法を取得
type: docs
weight: 40
url: /java/get-resolution-and-dimensions-of-embedded-images/
description: このセクションでは、埋め込み画像の解像度と寸法を取得する方法の詳細を示します
lastmod: "2021-06-05"
---

このトピックでは、Aspose.PDF 名前空間のオペレータクラスを使用して画像を抽出せずに解像度と寸法情報を取得する機能を提供する方法を説明します。

これを達成するためのさまざまな方法があります。この記事では、`arraylist` と [Image placement classes](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement) を使用する方法を説明します。

1. まず、ソース PDF ファイル（画像を含む）を読み込みます。
1. 次に、ドキュメント内の画像の名前を保持するための ArrayList オブジェクトを作成します。
1. Page.Resources.Images プロパティを使用して画像を取得します。
1. 画像のグラフィックス状態を保持するスタックオブジェクトを作成し、異なる画像状態を追跡するために使用します。

1. 現在の変換を定義するConcatenateMatrixオブジェクトを作成します。これにより、スケーリング、回転、傾斜を含む任意のコンテンツをサポートします。新しいマトリックスを前のものと連結します。最初から変換を定義することはできませんが、既存の変換を変更することはできます。

1. ConcatenateMatrixでマトリックスを変更できるため、元の画像状態に戻す必要がある場合もあります。GSaveとGRestoreオペレーターを使用します。これらのオペレーターは対になっているため、一緒に呼び出す必要があります。たとえば、複雑な変換を伴うグラフィックス作業を行い、最終的な変換を初期状態に戻す場合、アプローチは次のようになります:

```java
// いくつかのテキストを描画
GSave

ConcatenateMatrix  // オペレーターの後にコンテンツを回転

// グラフィックス作業

ConcatenateMatrix // オペレーターの後に（前の回転を持つ）コンテンツをスケーリング

// その他のグラフィックス作業

GRestore

// いくつかのテキストを描画
```

その結果、テキストは通常の形で描画されますが、テキストオペレーターの間にいくつかの変換が実行されます。
 画像を表示したりフォームオブジェクトや画像を描画するためには、Doオペレーターを使用する必要があります。

また、画像の幅と高さを取得するために使用できる、WidthとHeightという2つのプロパティを提供するXImageというクラスもあります。

1. 画像の解像度を計算するための計算を行います。
1. 画像名と共にコマンドプロンプトに情報を表示します。

以下のコードスニペットは、PDFドキュメントから画像を抽出せずに画像の寸法と解像度を取得する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // ソースPDFファイルをロード
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // 画像のデフォルト解像度を定義
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // 画像名を保持する配列リストオブジェクトを定義
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // スタックにオブジェクトを挿入
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // ドキュメントの最初のページのすべてのオペレーターを取得
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // GSave/GRestoreオペレーターを使用して変換を以前に設定された状態に戻す
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // 現在の変換マトリックスを定義するConcatenateMatrixオブジェクトをインスタンス化
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // リソースからオブジェクトを描画するDoオペレーターを作成。フォームオブジェクトや画像オブジェクトを描画
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // 以前の状態を保存し、現在の状態をスタックのトップにプッシュ
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // 現在の状態を破棄して以前の状態を復元
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // 現在のマトリックスと状態マトリックスを掛け合わせる
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // これは画像描画オペレーターの場合
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // 最初のPDFページの画像を保持するXImageオブジェクトを作成
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // 画像の寸法を取得
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // 画像の高さと幅の情報を取得
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // 上記の情報に基づいて解像度を計算
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // 各画像の寸法と解像度の情報を表示
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // 出力ドキュメントを保存
                doc.save(_dataDir);
            }
        }
    }
}
```