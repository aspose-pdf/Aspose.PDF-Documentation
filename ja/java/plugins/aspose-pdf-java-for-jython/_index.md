---
title: Jython 用 Aspose.PDF Java
linktitle: Jython 用 Aspose.PDF Java
type: docs
weight: 60
url: /ja/java/aspose-pdf-java-for-jython/
description: "Aspose.PDF for Java の機能を Jython と組み合わせることで、Python ベースの Java 環境で PDF ファイルを簡単に操作できます。"
lastmod: "2026-10-06"
---
## はじめに

### Jython とは何ですか？

Jython は、表現力と明快さを兼ね備えた Python の Java 実装です。Jython は商用・非商用を問わず無料で利用でき、ソースコードが配布されています。Jython は Java と相補的であり、特に次のタスクに適しています。

- **Embedded scripting** - Java プログラマーは、システムに Jython ライブラリを追加して、エンドユーザーが簡単なスクリプトや複雑なスクリプトを書き、アプリケーションに機能を追加できるようにできます。
- **インタラクティブな実験** - Jython は、Java パッケージや実行中の Java アプリケーションと対話できるインタラクティブインタプリタを提供します。これにより、プログラマは Jython を使用して任意の Java システムを実験およびデバッグできます。
- **迅速なアプリケーション開発** - Python プログラムは、同等の Java プログラムに比べて通常 2〜10 倍短くなります。これはプログラマの生産性向上に直結します。Python と Java のシームレスな相互作用により、開発中および製品出荷時に両言語を自由に組み合わせて使用できます。

### Aspose.PDF for Java

Aspose.PDF for Java は、Adobe Acrobat を使用せずに Java アプリケーションが PDF ドキュメントを読み取り、書き込み、操作できる PDF ドキュメント作成コンポーネントです。

Aspose.PDF for Java は、手頃な価格で提供されるコンポーネントであり、豊富な機能を備えています。これらの機能には、PDF 圧縮オプション、テーブルの作成と操作、グラフサポート、画像機能、広範なハイパーリンク機能、拡張されたセキュリティ制御、およびカスタムフォントの処理が含まれます。

Aspose.PDF for Java を使用すると、提供された API および XML テンプレートを通じて PDF ファイルを直接作成できます。また、Aspose.PDF for Java を活用することで、アプリケーションにすぐに PDF 機能を追加することも可能です。

### Jython 用 Aspose.PDF Java

Aspose.PDF Java for Jython は、Jython における Aspose.PDF for Java API の使用例を示す／提供するプロジェクトです。

## システム要件およびサポートプラットフォーム

### システム要件

以下は、Aspose.PDF Java for Jython を使用するためのシステム要件です。

- Java 1.5 以降がインストールされていること
- ダウンロードした Aspose.PDF コンポーネント
- Jython 2.7.0

### サポートされているプラットフォーム

以下はサポートされているプラットフォームです。

- Aspose.PDF 15.4 以降。
- Java IDE（Eclipse、NetBeans ...）

## ダウンロード、インストール、使用

### ダウンロード

以下の実行例のリリースは、GitHub からダウンロード可能です。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Aspose.PDF for Java コンポーネントをダウンロードしてください。

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### インストール

- ダウンロードした Aspose.PDF for Java の JAR ファイルを "lib" ディレクトリに配置してください。
- "your-lib" を、ダウンロードした JAR ファイル名に置き換えて、_init_.py ファイルに記述してください。

### 使用

次のサンプルコードを使用して、Pdf を doc ドキュメントに変換できます。

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## サポート、拡張、および貢献

### サポート

Aspose は創業当初から、優れた製品を提供するだけでは不十分であると認識していました。優れたサービスの提供も不可欠です。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合によって、やりたいことが実行できなくなる苛立ちを理解しています。私たちの使命は、問題を解決することであって、問題を生み出すことではありません。

そのため、無料サポートを提供しています。製品の購入の有無や評価版の利用の有無にかかわらず、すべてのユーザーに完全な注意と敬意を払うべきだと考えています。

以下のプラットフォームのいずれかを使用して、Aspose.PDF Java for Jython に関連する問題や提案を記録してください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 拡張と貢献

Aspose.PDF Java for Jython はオープンソースであり、そのソースコードは以下の主要なソーシャルコーディングサイトで入手可能です。開発者はソースコードをダウンロードし、新機能の提案や追加、既存機能の改善を通じて貢献することが奨励されています。これにより、他のユーザーもその恩恵を受けることができます。

### ソースコード

最新のソースコードは、以下のいずれかの場所から取得してください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
