---

title: 複雑なPDFの作成  
linktitle: 複雑なPDFの作成  
type: docs  
weight: 60  
url: /java/complex-pdf-example/  
description: Aspose.PDF for Javaを使用すると、画像、テキストフラグメント、テーブルを1つのドキュメントに含むより複雑なドキュメントを作成できます。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

[Hello, World](/pdf/java/hello-world-example/) の例では、JavaとAspose.PDFを使用してPDFドキュメントを作成する簡単な手順が示されました。この記事では、JavaとAspose.PDF for Javaを使用してより複雑なドキュメントを作成する方法を見ていきます。例として、架空の会社が運営する旅客フェリーサービスのドキュメントを取り上げます。  
私たちのドキュメントには、画像、2つのテキストフラグメント（ヘッダーと段落）、そしてテーブルが含まれます。このようなドキュメントを構築するために、DOMベースのアプローチを使用します。詳細は [DOM APIの基本](/pdf/java/basics-of-dom-api/) セクションで読むことができます。

ドキュメントをゼロから作成する場合、特定の手順に従う必要があります：


1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) オブジェクトをインスタンス化します。このステップでは、ページなしでメタデータを含む空のPDFドキュメントを作成します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)を追加します。これで、ドキュメントには1ページが含まれます。
1. [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)を追加します。これは、PDFオペレーターを用いた低レベルのアクションに基づく複雑な操作です。
    - ストリームから画像をロードする
    - ページリソースのImagesコレクションに画像を追加する
    - GSaveオペレーターを使用する: このオペレーターは現在のグラフィックス状態を保存します。
    - [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)オブジェクトを作成する。
    - ConcatenateMatrixオペレーターを使用する: 画像の配置方法を定義します。
    - Doオペレーターを使用する: このオペレーターは画像を描画します。
    - GRestoreオペレーターを使用する: このオペレーターはグラフィックス状態を復元します。

1. ヘッダー用の[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を作成します。ヘッダーにはArialフォントを使用し、フォントサイズは24pt、中央揃えにします。
1. ヘッダーをページの[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)に追加します。
1. 説明用の[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を作成します。説明にはArialフォントを使用し、フォントサイズは24pt、中央揃えにします。
1. (説明)をページのParagraphsに追加します。
1. テーブルを作成し、テーブルのプロパティを追加します。
1. (テーブル)をページの[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)に追加します。
1. ドキュメントを"Complex.pdf"として保存します。

```java
package com.aspose.pdf.examples;

/**
 * 複雑な例
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // ドキュメントオブジェクトを初期化
        Document document = new Document();
        // ページを追加
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // 画像を追加
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // 画像をページリソースのImagesコレクションに追加
        page.getResources().getImages().add(imageStream);

        // GSaveオペレーターを使用: このオペレーターは現在のグラフィックス状態を保存します
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Matrixオブジェクトを作成
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // ConcatenateMatrix (行列の結合) オペレーターを使用: 画像の配置方法を定義
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Doオペレーターを使用: このオペレーターは画像を描画します
        page.getContents().add(new Do(ximage.getName()));
        // GRestoreオペレーターを使用: このオペレーターはグラフィックス状態を復元します
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // ヘッダーを追加
        TextFragment header = new TextFragment("2020年秋の新しいフェリールート");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // 説明を追加
        String descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日あたり5,000枚に制限されています。フェリーサービスは半分の容量で運行しており、スケジュールが短縮されています。行列を予想してください。";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        // テーブルを追加
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("出発都市");
        headerRow.getCells().add("出発島");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```