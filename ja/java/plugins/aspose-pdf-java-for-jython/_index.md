---
title: Aspose.PDF Java for Jython
type: docs
weight: 60
url: ja/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## 紹介

### Jythonとは何ですか？

Jythonは、明快さと表現力を兼ね備えたPythonのJava実装です。Jythonは商用および非商用のどちらの利用も自由であり、ソースコードと共に配布されています。JythonはJavaを補完するものであり、特に次のタスクに適しています。

- **埋め込みスクリプティング** - JavaプログラマーはJythonライブラリをシステムに追加することで、エンドユーザーがアプリケーションに機能を追加する簡単または複雑なスクリプトを書くことができます。
- **インタラクティブな実験** - JythonはJavaパッケージや実行中のJavaアプリケーションと対話するために使用できるインタラクティブなインタープリターを提供します。これにより、プログラマーはJythonを使用して任意のJavaシステムを実験およびデバッグすることができます。
- **迅速なアプリケーション開発** - Pythonプログラムは通常、同等のJavaプログラムよりも2-10倍短いです。
 これはプログラマーの生産性の向上に直接つながります。PythonとJavaのシームレスな相互作用により、開発中および製品の出荷時に、開発者は2つの言語を自由に組み合わせることができます。

### Aspose.PDF for Java

Aspose.PDF for Javaは、JavaアプリケーションがAdobe Acrobatを使用せずにPDFドキュメントを読み書きおよび操作できるようにするPDFドキュメント作成コンポーネントです。

Aspose.PDF for Javaは手頃な価格のコンポーネントであり、驚くべき機能の豊富さを提供します。これには、PDF圧縮オプション、テーブルの作成と操作、グラフのサポート、画像機能、広範なハイパーリンク機能、拡張されたセキュリティ制御、カスタムフォントの処理が含まれます。

Aspose.PDF for Javaを使用すると、提供されるAPIとXMLテンプレートを通じて直接PDFファイルを作成できます。Aspose.PDF for Javaを使用することで、アプリケーションに短時間でPDF機能を追加することも可能になります。

### Aspose.PDF Java for Jython

Aspose.PDF Java for Jythonは、JythonでのAspose.PDF for Java APIの使用例を示す/提供するプロジェクトです。
## システム要件とサポートされているプラットフォーム

### システム要件

以下は、Aspose.PDF Java for Jythonを使用するためのシステム要件です：

- Java 1.5以上がインストールされていること
- Aspose.PDFコンポーネントをダウンロード済み
- Jython 2.7.0

### サポートされているプラットフォーム

以下はサポートされているプラットフォームです：

- Aspose.PDF 15.4以上
- Java IDE (Eclipse, NetBeans ...)

## ダウンロード、インストール、使用法

### ダウンロード

実行例の以下のリリースはGitHubからダウンロードできます：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Aspose.PDF for Javaコンポーネントをダウンロード：

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### インストール

- ダウンロードしたAspose.PDF for Javaのjarファイルを"lib"ディレクトリに配置します。
- _*init*_.pyファイル内の"your-lib"をダウンロードしたjarファイル名に置き換えます。

### 使用法

以下の例のコードを使用して、Pdfをdocドキュメントに変換できます：

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # 対象ドキュメントを開く
        pdf = Document(dataDir + 'input1.pdf')

        # 結合された出力ファイル（対象ドキュメント）を保存
        pdf.save(dataDir + "output.doc")

        print "ドキュメントは正常に変換されました"


if __name__ == '__main__':       

    PdfToDoc()
```


## サポート、拡張、貢献

### サポート

Aspose の最初の日から、私たちはお客様に良い製品を提供するだけでは不十分であることを理解していました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの癖が原因で必要なことができないときの苛立ちを理解しています。私たちは問題を解決するためにここにいます、問題を作り出すためではありません。

このため、無料のサポートを提供しています。製品を購入したか評価版を使用しているかに関わらず、当社の製品を使用するすべての人が私たちの注目と尊敬を受けるに値します。

Aspose.PDF Java for Jython に関連する問題や提案は、以下のいずれかのプラットフォームを使用してログに記録できます。

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 拡張と貢献

Aspose.PDF Java for Jython はオープンソースであり、そのソースコードは以下にリストされている主要なソーシャルコーディングウェブサイトで入手できます。
 開発者は、ソースコードをダウンロードし、新機能の提案や追加、既存機能の改善を行うことで貢献することが奨励されています。他の人もそれから利益を得ることができるように。

### ソースコード

以下の場所のいずれかから最新のソースコードを取得できます

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)